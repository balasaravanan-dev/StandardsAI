# System Architecture

Technical deep-dive into StandardsAI's architecture and algorithms.

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Core Insight](#core-insight)
3. [Data Flow](#data-flow)
4. [Algorithms](#algorithms)
5. [Technology Stack](#technology-stack)
6. [File Structure](#file-structure)
7. [Data Model](#data-model)

---

## Architecture Overview

```
                         ┌─────────────────────────────────────────────┐
                         │              USER INTERFACES                │
                         │  Streamlit UI │ REST API │ Browser Extension│
                         └──────────────────────┬──────────────────────┘
                                                │
                         ┌──────────────────────▼──────────────────────┐
                         │              FASTAPI APPLICATION            │
                         │                                             │
                         │  ┌─────────────────────────────────────┐   │
                         │  │         API LAYER (main.py)         │   │
                         │  │  /recommend │ /audit │ /graph       │   │
                         │  └─────────────────────────────────────┘   │
                         │                     │                       │
                         │  ┌─────────────────┬┴─────────────────┐    │
                         │  │                 │                  │    │
                         │  ▼                 ▼                  ▼    │
                         │ ┌──────┐      ┌──────┐         ┌──────┐   │
                         │ │Search│      │Audit │         │Graph │   │
                         │ │Engine│      │Engine│         │Engine│   │
                         │ └──────┘      └──────┘         └──────┘   │
                         │                                             │
                         └──────────────────────┬──────────────────────┘
                                                │
                         ┌──────────────────────▼──────────────────────┐
                         │              DATA LAYER                     │
                         │                                             │
                         │  ┌─────────────────────────────────────┐   │
                         │  │       sample_standards.json          │   │
                         │  │  • 15 standards with metadata        │   │
                         │  │  • 8 relationships                   │   │
                         │  │  • 3 certification schemes           │   │
                         │  └─────────────────────────────────────┘   │
                         │                                             │
                         └─────────────────────────────────────────────┘
```

---

## Core Insight

> **"This is a GRAPH problem, not a text problem."**

### What This Means

| Traditional AI Approach | Our Graph-Centric Approach |
|------------------------|---------------------------|
| LLM for everything | LLM only for understanding input |
| Vector search alone | Hybrid search + graph traversal |
| No relationships | Full dependency resolution |
| Hallucination risk | Closed-set grounding (zero hallucinations) |
| Black box | Traceable paths |

### Where AI Is Used vs Not Used

| Function | AI Used? | Actual Approach |
|----------|----------|-----------------|
| Understanding input | YES | NER + classification |
| Graph traversal | NO | BFS algorithm |
| Version checking | NO | Database lookup |
| Certification check | NO | Rule engine |
| Explanation | YES | Template + LLM |

---

## Data Flow

### 1. Search Request Flow

```
User Query: "cement for coastal construction"
                │
                ▼
┌──────────────────────────────────┐
│ 1. CONTEXT EXTRACTION            │
│    • coastal: true               │
│    • construction: true          │
└──────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│ 2. HYBRID SEARCH                 │
│    • BM25: keyword matching      │
│    • Semantic: similarity        │
│    • RRF: fusion                 │
└──────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│ 3. CONTEXT BOOST                 │
│    • +10% for marine/corrosion   │
│    • Re-sort by boosted score    │
└──────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│ 4. GRAPH EXPANSION               │
│    • Get dependencies            │
│    • Add allied standards        │
└──────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│ 5. CERTIFICATION CHECK           │
│    • Query certification DB      │
│    • Flag mandatory certs        │
└──────────────────────────────────┘
                │
                ▼
        Response JSON
```

### 2. Audit Request Flow

```
Tender Text: "IS 456:1978, IS 269:2015"
                │
                ▼
┌──────────────────────────────────┐
│ 1. REGEX EXTRACTION              │
│    Pattern: IS\s*(\d+):\d{4}     │
│    Found: ["IS 456:1978",        │
│            "IS 269:2015"]        │
└──────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│ 2. WITHDRAWN CHECK               │
│    IS 456:1978 → WITHDRAWN       │
│    IS 269:2015 → VALID           │
└──────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│ 3. DEPENDENCY CHECK              │
│    IS 269:2015 requires:         │
│    • IS 4031 → NOT FOUND         │
│    • IS 4032 → NOT FOUND         │
└──────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│ 4. AMENDMENT CHECK               │
│    IS 269:2015 Amd 1 (2019)      │
│    → NOT REFERENCED              │
└──────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│ 5. CERTIFICATION CHECK           │
│    IS 269:2015 → BIS Mark req.   │
│    → NOT MENTIONED               │
└──────────────────────────────────┘
                │
                ▼
        Audit Report JSON
```

---

## Algorithms

### 1. Hybrid Search (search.py)

```python
def hybrid_search(query, top_k=10):
    # Step 1: BM25 Search (keyword matching)
    bm25_results = bm25_search(query, top_k * 2)
    
    # Step 2: Semantic Search (similarity)
    semantic_results = semantic_search(query, top_k * 2)
    
    # Step 3: Reciprocal Rank Fusion
    k = 60  # RRF constant
    rrf_scores = {}
    
    for doc_id in all_results:
        bm25_rank = bm25_ranks.get(doc_id, 1000)
        semantic_rank = semantic_ranks.get(doc_id, 1000)
        
        rrf_scores[doc_id] = (
            0.5 * (1 / (k + bm25_rank)) +
            0.5 * (1 / (k + semantic_rank))
        )
    
    return sorted(rrf_scores, reverse=True)[:top_k]
```

**Why RRF?**
- Combines rankings without needing normalized scores
- Robust to outliers
- Better than simple score averaging

### 2. Dependency Resolution (graph.py)

```python
def resolve_dependencies(standard_id, depth=3):
    visited = set()
    queue = deque([(standard_id, 0)])
    tree = {"id": standard_id, "children": []}
    
    while queue:
        current_id, current_depth = queue.popleft()
        
        if current_id in visited or current_depth >= depth:
            continue
        
        visited.add(current_id)
        
        # Get normative references
        refs = standards[current_id].normative_references
        
        for ref in refs:
            if ref in standards:
                queue.append((ref, current_depth + 1))
                # Add to tree
    
    return {
        "tree": tree,
        "flat_list": list(visited),
        "total_dependencies": len(visited) - 1
    }
```

**Algorithm:** Breadth-First Search (BFS)
- Guarantees shortest path
- Level-by-level traversal
- Prevents cycles via visited set

### 3. Tender Audit (audit.py)

```python
def audit(text):
    # Step 1: Extract references
    pattern = r'IS\s*(\d+(?:-\d+)?):?(\d{4})?'
    matches = re.findall(pattern, text)
    
    errors = []
    warnings = []
    
    for is_num, year in matches:
        full_id = f"IS {is_num}:{year}"
        
        # Step 2: Check if withdrawn
        if full_id in withdrawn_db:
            errors.append({
                "standard": full_id,
                "message": f"WITHDRAWN in {withdrawn_db[full_id]['year']}",
                "suggestion": f"Use {withdrawn_db[full_id]['superseded_by']}"
            })
            continue
        
        # Step 3: Check dependencies
        if full_id in standards_db:
            for dep in standards_db[full_id].normative_references:
                if dep not in text:
                    errors.append({
                        "standard": full_id,
                        "message": f"Requires {dep} but not found"
                    })
        
        # Step 4: Check amendments
        # Step 5: Check certifications
    
    return AuditResult(errors, warnings)
```

---

## Technology Stack

### Current (Demo)

| Component | Technology | Purpose |
|-----------|------------|---------|
| Backend | FastAPI | REST API server |
| Frontend | Streamlit | Demo UI |
| Data | JSON | Standards database |
| Search | BM25 + Jaccard | Hybrid retrieval |
| Graph | In-memory dict | Dependency resolution |

### Production (Proposed)

| Component | Technology | Purpose |
|-----------|------------|---------|
| Backend | FastAPI | REST API server |
| Frontend | Next.js | Production UI |
| Database | PostgreSQL | Primary storage |
| Vector | pgvector | Embedding search |
| Graph | Apache AGE | Graph queries |
| Embeddings | sentence-transformers | Local embeddings |
| LLM | Ollama + Llama 3.1 | Self-hosted |

### Why Single Database (PostgreSQL)?

```
PostgreSQL 15 with Extensions
├── Tables (standards, users, logs)
├── pgvector (vector similarity search)
└── Apache AGE (graph traversal)

Benefits:
✓ Single backup
✓ Single security audit
✓ Single NIC approval
✓ Simpler operations
```

---

## File Structure

```
backend/
├── app/
│   ├── main.py                 # FastAPI application
│   │   ├── RecommendRequest    # Request models
│   │   ├── AuditRequest        # Request models
│   │   ├── /api/v1/recommend   # Search endpoint
│   │   ├── /api/v1/audit/text  # Audit endpoint
│   │   └── /api/v1/graph/{id}  # Graph endpoint
│   │
│   └── services/
│       ├── search.py           # HybridSearch class
│       │   ├── bm25_search()   # Keyword search
│       │   ├── semantic_search() # Similarity search
│       │   └── hybrid_search() # RRF fusion
│       │
│       ├── graph.py            # StandardsGraph class
│       │   ├── resolve_dependencies()
│       │   ├── check_completeness()
│       │   └── to_vis_format()
│       │
│       └── audit.py            # TenderAuditor class
│           ├── extract_standards()
│           ├── audit()
│           └── _check_dependencies()

frontend/
└── app.py                      # Streamlit application
    ├── Tab 1: Search
    ├── Tab 2: Tender Audit
    ├── Tab 3: Dependency Graph
    └── Tab 4: About

data/
└── sample_standards.json       # Standards database
    ├── standards[]             # 15 standards
    ├── relationships[]         # 8 relationships
    └── certifications[]        # 3 certification schemes
```

---

## Data Model

### Standard

```json
{
  "is_number": "IS 269:2015",
  "title": "Ordinary Portland Cement - Specification",
  "scope": "Covers the chemical, physical requirements...",
  "department": "Civil Engineering",
  "category": "Cement",
  "year": 2015,
  "latest_amendment": "Amd 1 (2019)",
  "status": "current",
  "mandatory_certification": true,
  "normative_references": ["IS 4031 series", "IS 4032", "IS 650"],
  "keywords": ["OPC cement", "Portland cement", "construction"]
}
```

### Relationship

```json
{
  "source": "IS 269:2015",
  "target": "IS 455:2015",
  "type": "allied_standard",
  "description": "Alternative cement type"
}
```

### Certification

```json
{
  "type": "BIS_PRODUCT_CERTIFICATION",
  "name": "ISI Mark",
  "description": "Mandatory for products under BIS scheme",
  "applicable_standards": ["IS 269:2015", "IS 455:2015", ...]
}
```

---

## Scalability Considerations

### Current Limitations

- In-memory data (15 standards)
- No persistent storage
- Single-threaded search

### Scaling Path

| Scale | Solution |
|-------|----------|
| 1,000 standards | PostgreSQL + pgvector |
| 10,000 standards | Add caching (Redis) |
| 100,000 queries/day | Horizontal scaling (K8s) |
| Full BIS catalog | Distributed processing |

---

## Security Design

### Data Sovereignty

```
┌─────────────────────────────────────────┐
│           GOVERNMENT DATA FLOW          │
│                                         │
│  User Input ──► Local Processing ──►    │
│      │                   │              │
│      │    NO EXTERNAL    │              │
│      │      API CALLS    │              │
│      ▼                   ▼              │
│  Embeddings         LLM Inference       │
│  (local)            (self-hosted)       │
│                                         │
│  ✓ Zero data leaves India               │
│  ✓ CERT-In compliant                    │
│  ✓ NIC Cloud deployable                 │
└─────────────────────────────────────────┘
```

### Input Validation

- Query sanitization
- SQL injection prevention (parameterized queries)
- File upload validation (PDF only)
- Rate limiting (production)

---

## Next Steps

- [API.md](API.md) - Complete API reference
- [DEMO_SCRIPT.md](DEMO_SCRIPT.md) - Video presentation guide
