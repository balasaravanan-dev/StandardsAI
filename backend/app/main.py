"""
StandardsAI - FastAPI Backend
AI-Powered Recommendation Engine for Indian Standards

Features:
- Semantic Search (Hybrid BM25 + Vector)
- Dependency Resolution (Graph Traversal)
- Tender Audit (The Killer Feature)
- Certification Flagging
"""

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import json
from pathlib import Path
import tempfile
import os

# Import services
from app.services.search import HybridSearch, SearchResult
from app.services.graph import StandardsGraph, get_graph
from app.services.audit import TenderAuditor, AuditResult

app = FastAPI(
    title="StandardsAI API",
    description="""
    AI-Powered Recommendation Engine for Identifying Applicable Indian Standards

    ## Features
    - **Semantic Search**: Find standards by product description
    - **Dependency Resolution**: Get complete standards package with all dependencies
    - **Tender Audit**: Upload tender documents and check for compliance issues
    - **Certification Flagging**: Automatic detection of mandatory certifications
    """,
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============ MODELS ============

class RecommendRequest(BaseModel):
    query: str
    language: str = "en"
    include_allied: bool = True
    include_certifications: bool = True
    max_results: int = 10


class StandardResponse(BaseModel):
    is_number: str
    title: str
    scope: str
    relevance_score: float
    is_latest: bool = True
    mandatory_certification: bool = False
    amendments: Optional[str] = None
    match_reasons: Optional[List[str]] = None


class RecommendResponse(BaseModel):
    query_understood: str
    context_detected: Dict[str, bool]
    primary_standards: List[StandardResponse]
    allied_standards: List[StandardResponse]
    certifications: List[Dict]
    total_found: int


class AuditRequest(BaseModel):
    text: str


class AuditResponse(BaseModel):
    total_references: int
    valid_count: int
    error_count: int
    warning_count: int
    errors: List[Dict]
    warnings: List[Dict]
    valid_standards: List[Dict]
    summary: str


class GraphRequest(BaseModel):
    standard_id: str
    depth: int = 3
    include_allied: bool = True


class GraphResponse(BaseModel):
    root: str
    root_details: Optional[Dict]
    total_dependencies: int
    flat_list: List[str]
    tree: Dict
    visualization: Dict
    certifications: List[Dict]


# ============ DATA LOADING ============

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "sample_standards.json"


def load_standards():
    if DATA_PATH.exists():
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"standards": [], "relationships": [], "certifications": []}


STANDARDS_DB = load_standards()

# Initialize services
search_engine = HybridSearch(STANDARDS_DB.get("standards", []))
graph_engine = StandardsGraph(
    STANDARDS_DB.get("standards", []),
    STANDARDS_DB.get("relationships", [])
)
auditor = TenderAuditor(STANDARDS_DB)


# ============ ENDPOINTS ============

@app.get("/")
async def root():
    return {
        "message": "StandardsAI API",
        "version": "2.0.0",
        "features": [
            "Semantic Search",
            "Dependency Resolution",
            "Tender Audit",
            "Certification Flagging"
        ],
        "docs": "/docs"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "standards_loaded": len(STANDARDS_DB.get("standards", [])),
        "relationships_loaded": len(STANDARDS_DB.get("relationships", []))
    }


@app.post("/api/v1/recommend", response_model=RecommendResponse)
async def recommend_standards(request: RecommendRequest):
    """
    Recommend Indian Standards based on product description.

    Uses hybrid search (BM25 + semantic) with context detection.
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    # Search with context
    results, context = search_engine.search_with_context(
        request.query,
        top_k=request.max_results
    )

    # Split into primary and allied
    primary = results[:5] if len(results) >= 5 else results
    allied = []

    if request.include_allied:
        # Get allied standards from graph
        primary_ids = [r.is_number for r in primary]
        for std_id in primary_ids:
            deps = graph_engine.resolve_dependencies(std_id, depth=1)
            for dep_id in deps.get("flat_list", [])[1:]:  # Skip root
                if dep_id not in primary_ids:
                    std = graph_engine.get_standard(dep_id)
                    if std:
                        allied.append(SearchResult(
                            is_number=std["is_number"],
                            title=std["title"],
                            scope=std["scope"],
                            score=75.0,
                            match_reasons=["Dependency of primary standard"]
                        ))

    # Get certifications
    certs = []
    if request.include_certifications:
        all_ids = [r.is_number for r in primary + allied]
        for cert in STANDARDS_DB.get("certifications", []):
            for std_id in all_ids:
                if std_id in cert.get("applicable_standards", []):
                    certs.append({
                        "type": cert["type"],
                        "name": cert["name"],
                        "mandatory": True,
                        "applicable_to": std_id
                    })
                    break

    return RecommendResponse(
        query_understood=request.query,
        context_detected=context,
        primary_standards=[
            StandardResponse(
                is_number=r.is_number,
                title=r.title,
                scope=r.scope,
                relevance_score=r.score,
                match_reasons=r.match_reasons,
                mandatory_certification=any(
                    r.is_number in c.get("applicable_standards", [])
                    for c in STANDARDS_DB.get("certifications", [])
                ),
                amendments=next(
                    (s.get("latest_amendment") for s in STANDARDS_DB["standards"]
                     if s["is_number"] == r.is_number), None
                )
            )
            for r in primary
        ],
        allied_standards=[
            StandardResponse(
                is_number=r.is_number,
                title=r.title,
                scope=r.scope,
                relevance_score=r.score,
                match_reasons=r.match_reasons
            )
            for r in allied[:5]
        ],
        certifications=certs,
        total_found=len(results)
    )


@app.post("/api/v1/audit/text", response_model=AuditResponse)
async def audit_text(request: AuditRequest):
    """
    Audit tender text for standards compliance.

    THE KILLER FEATURE - Finds:
    - Withdrawn/superseded standards
    - Missing dependencies
    - Missing amendments
    - Missing certification requirements
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    result = auditor.audit(request.text)

    # Build summary
    if result.error_count == 0 and result.warning_count == 0:
        summary = "All standards references are valid and complete."
    else:
        summary = f"Found {result.error_count} errors and {result.warning_count} warnings that need attention."

    return AuditResponse(
        total_references=result.total_references,
        valid_count=result.valid_count,
        error_count=result.error_count,
        warning_count=result.warning_count,
        errors=[
            {
                "standard": e.standard,
                "message": e.message,
                "suggestion": e.suggestion
            }
            for e in result.errors
        ],
        warnings=[
            {
                "standard": w.standard,
                "message": w.message,
                "suggestion": w.suggestion
            }
            for w in result.warnings
        ],
        valid_standards=[
            {"is_number": s["is_number"], "title": s["title"]}
            for s in result.valid_standards
        ],
        summary=summary
    )


@app.post("/api/v1/audit/pdf", response_model=AuditResponse)
async def audit_pdf(file: UploadFile = File(...)):
    """
    Audit a PDF tender document for standards compliance.
    """
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    try:
        import fitz  # PyMuPDF

        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name

        # Extract text
        doc = fitz.open(tmp_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()

        # Clean up
        os.unlink(tmp_path)

        # Audit
        result = auditor.audit(text)

        # Build summary
        if result.error_count == 0 and result.warning_count == 0:
            summary = "All standards references are valid and complete."
        else:
            summary = f"Found {result.error_count} errors and {result.warning_count} warnings."

        return AuditResponse(
            total_references=result.total_references,
            valid_count=result.valid_count,
            error_count=result.error_count,
            warning_count=result.warning_count,
            errors=[
                {"standard": e.standard, "message": e.message, "suggestion": e.suggestion}
                for e in result.errors
            ],
            warnings=[
                {"standard": w.standard, "message": w.message, "suggestion": w.suggestion}
                for w in result.warnings
            ],
            valid_standards=[
                {"is_number": s["is_number"], "title": s["title"]}
                for s in result.valid_standards
            ],
            summary=summary
        )

    except ImportError:
        raise HTTPException(status_code=500, detail="PyMuPDF not installed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/v1/graph", response_model=GraphResponse)
async def get_dependency_graph(request: GraphRequest):
    """
    Get dependency graph for a standard.

    Like npm/pip - resolves full dependency tree.
    """
    result = graph_engine.resolve_dependencies(
        request.standard_id,
        depth=request.depth,
        include_allied=request.include_allied
    )

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    # Get certifications
    certs = graph_engine.get_certification_requirements(request.standard_id)

    # Convert to visualization format
    vis_format = graph_engine.to_vis_format(result["tree"])

    return GraphResponse(
        root=result["root"],
        root_details=result.get("root_details"),
        total_dependencies=result["total_dependencies"],
        flat_list=result["flat_list"],
        tree=result["tree"],
        visualization=vis_format,
        certifications=certs
    )


@app.get("/api/v1/graph/{standard_id}")
async def get_graph_simple(standard_id: str, depth: int = 2):
    """
    Simple GET endpoint for dependency graph.
    """
    result = graph_engine.resolve_dependencies(standard_id, depth=depth)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result


@app.get("/api/v1/standards")
async def list_standards():
    """List all standards in the database."""
    return {
        "total": len(STANDARDS_DB.get("standards", [])),
        "standards": [
            {
                "is_number": s["is_number"],
                "title": s["title"],
                "category": s.get("category"),
                "mandatory_certification": s.get("mandatory_certification", False)
            }
            for s in STANDARDS_DB.get("standards", [])
        ]
    }


@app.get("/api/v1/standards/{is_number}")
async def get_standard(is_number: str):
    """Get details of a specific standard."""
    std = graph_engine.get_standard(is_number)
    if std:
        return std
    raise HTTPException(status_code=404, detail="Standard not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
