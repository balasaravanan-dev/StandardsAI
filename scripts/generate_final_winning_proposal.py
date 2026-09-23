"""
FINAL WINNING PROPOSAL - Consolidated Document
Everything in one place: Orchestration, Feasibility, Novelty, Gap Analysis
"""

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

OUTPUT_DIR = r"C:\Users\balak\Downloads\SIH\docs"


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Table Grid'
    hdr_cells = table.rows[0].cells
    for i, header in enumerate(headers):
        hdr_cells[i].text = header
        hdr_cells[i].paragraphs[0].runs[0].bold = True
    for row_data in rows:
        row_cells = table.add_row().cells
        for i, cell_data in enumerate(row_data):
            row_cells[i].text = str(cell_data)
    doc.add_paragraph()


def create_final_proposal():
    doc = Document()

    # ========== TITLE ==========
    title = doc.add_heading("STANDARDSAI — WINNING PROPOSAL", 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    subtitle = doc.add_paragraph("AI-Powered Recommendation Engine for Indian Standards")
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

    info = doc.add_paragraph()
    run = info.add_run("SIH 2024 | Problem ID: 26108 | Ministry of Consumer Affairs\n")
    run.italic = True
    run2 = info.add_run("Final Consolidated Document — All Research & Architecture")
    run2.bold = True
    info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph()

    # ========== EXECUTIVE SUMMARY ==========
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    doc.add_paragraph(
        "StandardsAI is an AI-powered recommendation ENGINE that integrates with procurement portals "
        "(GeM, CPPP) to help procurement officers identify the correct Indian Standards for tender "
        "specifications. Unlike basic search tools, StandardsAI treats standards as a KNOWLEDGE GRAPH "
        "with dependencies, versions, and certification requirements — enabling dependency resolution, "
        "tender auditing, and compliance checking in under 2 seconds."
    )

    doc.add_heading("The One-Liner", level=2)
    doc.add_paragraph(
        "\"We didn't build a chatbot that guesses which standards might be relevant. We built a "
        "STANDARDS DEPENDENCY RESOLVER — a knowledge graph of 22,000+ Indian Standards that resolves "
        "normative references, detects outdated versions, checks certification requirements, and "
        "audits tender documents. The AI understands your input; the graph gives you the correct answer.\""
    )

    # ========== THE CORE INSIGHT ==========
    doc.add_heading("1. THE CORE INSIGHT", level=1)

    doc.add_paragraph(
        "This is a GRAPH problem, not a text problem. Most teams will build an LLM wrapper. "
        "But standards have STRUCTURED RELATIONSHIPS — normative references, supersession chains, "
        "amendments, certification linkages. The right architecture treats the KNOWLEDGE GRAPH "
        "AS THE ENGINE and uses AI only where it genuinely adds value."
    )

    ai_usage = [
        ("Graph traversal", "NO", "Cypher queries, not LLM prompts"),
        ("Version checking", "NO", "Database lookup"),
        ("Certification check", "NO", "Rule engine vs QCO table"),
        ("Conflict detection", "NO", "Constraint algorithms"),
        ("Understanding input", "YES", "NER + classification"),
        ("Explanation generation", "YES", "LLM for human-readable output"),
    ]
    add_table(doc, ["Function", "Needs AI?", "Why"], ai_usage)

    # ========== GAP ANALYSIS ==========
    doc.add_heading("2. GAP ANALYSIS", level=1)

    doc.add_heading("Current Tools and Their Limitations", level=2)
    gaps = [
        ("BIS Website", "Keyword search only", "No semantic understanding, no graph"),
        ("GeM Portal", "Hardcoded standards per category", "No dynamic recommendation"),
        ("CPPP Portal", "Manual standard lookup", "Zero intelligence layer"),
        ("ChatGPT/Claude", "General knowledge", "Hallucinations, outdated data, no graph"),
    ]
    add_table(doc, ["Tool", "What It Does", "Gap"], gaps)

    doc.add_heading("The 6 Core Gaps We Fill", level=2)
    core_gaps = [
        ("1. Semantic Gap", "Keyword → Semantic understanding", "NER + ICS classification + embeddings"),
        ("2. Context Gap", "Generic → Environment-aware", "Extract location, application, constraints"),
        ("3. Graph Gap", "Isolated → Dependencies", "Knowledge graph with transitive resolution"),
        ("4. Lifecycle Gap", "Static → Version tracking", "Amendments, supersession, withdrawal"),
        ("5. Certification Gap", "Manual → Auto-flagging", "QCO/CRS/Hallmarking database"),
        ("6. Integration Gap", "Standalone → Portal-integrated", "API + Browser extension"),
    ]
    add_table(doc, ["Gap", "From → To", "Our Solution"], core_gaps)

    # ========== NOVELTY RANKING ==========
    doc.add_heading("3. NOVELTY RANKING BY FEASIBILITY", level=1)

    doc.add_heading("Tier 1: HIGH Feasibility — MUST Demo", level=2)
    tier1 = [
        ("1", "Tender Audit Mode", "HIGH", "Regex + graph lookup", "KILLER FEATURE"),
        ("2", "Dependency Resolution", "HIGH", "Graph algorithms", "Visual wow factor"),
        ("3", "Version Validation", "HIGH", "Database lookup", "Trust builder"),
        ("4", "Certification Flagging", "HIGH", "Rule engine", "Government loves this"),
        ("5", "Hybrid Search", "HIGH", "BM25 + embeddings", "Better than keyword"),
    ]
    add_table(doc, ["Rank", "Innovation", "Feasibility", "Implementation", "Impact"], tier1)

    doc.add_heading("Tier 2: MEDIUM Feasibility — Nice to Have", level=2)
    tier2 = [
        ("6", "ICS Classification", "MEDIUM", "BERT classifier or rules"),
        ("7", "Cross-Encoder Re-ranking", "MEDIUM", "Pre-trained models"),
        ("8", "Amendment Tracking", "MEDIUM", "Gazette parsing"),
        ("9", "Context-Aware Boost", "MEDIUM", "Feature engineering"),
    ]
    add_table(doc, ["Rank", "Innovation", "Feasibility", "Notes"], tier2)

    doc.add_heading("Tier 3: LOW Feasibility — Post-Hackathon", level=2)
    tier3 = [
        ("10", "Clause-Level Matching", "LOW", "Needs full standard texts"),
        ("11", "Domain Embeddings", "LOW", "Needs training data"),
        ("12", "Browser Extension", "LOW", "Chrome store approval time"),
    ]
    add_table(doc, ["Rank", "Innovation", "Feasibility", "Blocker"], tier3)

    # ========== ORCHESTRATION PIPELINE ==========
    doc.add_heading("4. ORCHESTRATION PIPELINE", level=1)

    doc.add_paragraph("Complete request flow from user input to final response:")

    pipeline = [
        ("Stage 1", "Input Processing", "100ms", "Language detection, translation, normalization"),
        ("Stage 2", "Entity Extraction", "200ms", "NER for product, material, application, environment"),
        ("Stage 3", "Classification", "150ms", "ICS code mapping, category detection"),
        ("Stage 4", "Candidate Retrieval", "300ms", "BM25 + Vector + Graph query → Hybrid fusion"),
        ("Stage 5", "Re-ranking", "400ms", "Cross-encoder scoring, context boost"),
        ("Stage 6", "Graph Engine", "200ms", "Dependency resolution, version check, certification"),
        ("Stage 7", "Validation", "100ms", "Closed-set grounding, confidence thresholding"),
        ("Stage 8", "Explanation", "500ms", "LLM generates human-readable justification"),
    ]
    add_table(doc, ["Stage", "Name", "Time", "Operations"], pipeline)

    doc.add_paragraph("TOTAL PROCESSING TIME: < 2 seconds")
    doc.add_paragraph()

    doc.add_heading("Where AI Is Used vs Not Used", level=2)
    ai_stages = [
        ("Input Processing", "Minimal", "Translation only"),
        ("Entity Extraction", "Yes", "NER model"),
        ("Classification", "Yes", "BERT classifier"),
        ("Candidate Retrieval", "Partial", "Embeddings for vector search"),
        ("Re-ranking", "Yes", "Cross-encoder"),
        ("Graph Engine", "NO", "Pure algorithms — THE CORE"),
        ("Validation", "NO", "Rules and thresholds"),
        ("Explanation", "Yes", "LLM for output"),
    ]
    add_table(doc, ["Stage", "AI Used?", "Notes"], ai_stages)

    # ========== TECHNICAL ARCHITECTURE ==========
    doc.add_heading("5. TECHNICAL ARCHITECTURE", level=1)

    doc.add_heading("Technology Stack", level=2)
    stack = [
        ("Frontend", "Next.js 14 + TypeScript + Tailwind"),
        ("Backend", "FastAPI (Python 3.11+)"),
        ("Knowledge Graph", "Neo4j Community Edition"),
        ("Vector Store", "ChromaDB (MVP) → Qdrant (production)"),
        ("Search", "Elasticsearch (BM25)"),
        ("Embeddings", "BAAI/bge-base-en-v1.5"),
        ("Re-ranker", "ms-marco-MiniLM-L-6-v2"),
        ("LLM", "Claude API / Groq + Llama 3.1"),
        ("Translation", "Bhashini API"),
        ("Deployment", "Docker + Railway → NIC Cloud"),
    ]
    add_table(doc, ["Layer", "Technology"], stack)

    doc.add_heading("Integration Architecture", level=2)
    integration = [
        ("REST API", "Primary interface for portal integration", "OpenAPI 3.0 spec"),
        ("Browser Extension", "Chrome extension for GeM/CPPP", "Content script injection"),
        ("Document Upload", "Tender PDF audit endpoint", "Multipart form upload"),
        ("Webhook", "Async notification for long operations", "POST callback"),
    ]
    add_table(doc, ["Method", "Description", "Details"], integration)

    # ========== DEMO SCENARIOS ==========
    doc.add_heading("6. DEMO SCENARIOS", level=1)

    doc.add_heading("Demo 1: Simple Query", level=2)
    doc.add_paragraph("Input: \"Stainless steel utensils for government canteen\"")
    doc.add_paragraph("Output:")
    demo1 = [
        "✓ IS 9235:2020 — Stainless Steel Utensils (Primary)",
        "  └── IS 6911:2017 — SS Plate/Sheet (Dependency)",
        "  └── IS 6603:2001 — Chemical Composition (Dependency)",
        "  └── IS 6912:2003 — Terminology (Dependency)",
        "⚠️ Certification Required: BIS Mark (QCO 2018)",
        "📋 Amendment: IS 9235 Amd 1 (2022) — check clause 4.2.1",
    ]
    for line in demo1:
        doc.add_paragraph(line, style='List Bullet')

    doc.add_heading("Demo 2: Tender Audit", level=2)
    doc.add_paragraph("Input: Upload tender_cement_supply.pdf")
    doc.add_paragraph("Output:")
    demo2 = [
        "❌ IS 456:1978 — WITHDRAWN (Superseded by IS 456:2000)",
        "❌ IS 269 references IS 4031 — NOT FOUND in tender",
        "⚠️ IS 12269:2013 — Amendment 2 (2020) not referenced",
        "✓ IS 383:2016 — Current, valid",
        "❌ BIS Mark certification — NOT MENTIONED (mandatory for cement)",
        "━━━━━━━━━━━━━━━━━━━━━━━━",
        "3 ERRORS, 2 WARNINGS — Tender needs revision",
    ]
    for line in demo2:
        doc.add_paragraph(line, style='List Bullet')

    doc.add_heading("Demo 3: Hindi Query", level=2)
    doc.add_paragraph("Input: \"सरकारी कैंटीन के लिए स्टेनलेस स्टील के बर्तन\"")
    doc.add_paragraph("Output: Same as Demo 1 (Bhashini translates, results in Hindi)")

    # ========== MARKET OPPORTUNITY ==========
    doc.add_heading("7. MARKET OPPORTUNITY", level=1)

    market = [
        ("Total BIS Standards", "22,000+"),
        ("Annual Government Procurement", "₹20+ lakh crore"),
        ("Potential Users", "300,000+ procurement officers"),
        ("Time Saved per Tender", "2-4 hours → 3 seconds"),
        ("Competitors", "ZERO with AI + graph approach"),
    ]
    add_table(doc, ["Metric", "Value"], market)

    # ========== WHY THIS WINS ==========
    doc.add_heading("8. WHY THIS WINS", level=1)

    wins = [
        ("Verifiable", "Every recommendation has a traceable graph path"),
        ("Testable", "Precision/Recall metrics, not vibes"),
        ("Government-Ready", "Auditable evidence chain, data sovereignty"),
        ("Novel", "First standards dependency resolver — like npm for IS"),
        ("Practical", "Tender Audit Mode solves REAL problem"),
        ("Scalable", "Graph algorithms, not LLM-per-query cost"),
    ]
    add_table(doc, ["Dimension", "Our Advantage"], wins)

    # ========== MVP CHECKLIST ==========
    doc.add_heading("9. MVP CHECKLIST (36 Hours)", level=1)

    doc.add_heading("MUST HAVE", level=2)
    must = [
        "[ ] Knowledge graph with 500+ standards + relationships",
        "[ ] Dependency resolution (graph traversal)",
        "[ ] Version validation (current/withdrawn check)",
        "[ ] Certification flagging (QCO lookup)",
        "[ ] Tender Audit endpoint (PDF upload → compliance report)",
        "[ ] Hybrid search (BM25 + vector)",
        "[ ] Basic web UI for demo",
        "[ ] 3-4 compelling demo scenarios",
    ]
    for item in must:
        doc.add_paragraph(item)

    doc.add_heading("SHOULD HAVE", level=2)
    should = [
        "[ ] ICS classification (rules-based is fine)",
        "[ ] Cross-encoder re-ranking",
        "[ ] Hindi language support (Bhashini)",
        "[ ] Graph visualization (D3.js/vis.js)",
    ]
    for item in should:
        doc.add_paragraph(item)

    doc.add_heading("COULD HAVE", level=2)
    could = [
        "[ ] Browser extension prototype",
        "[ ] Amendment tracking",
        "[ ] Clause-level evidence",
    ]
    for item in could:
        doc.add_paragraph(item)

    # ========== TEAM ALLOCATION ==========
    doc.add_heading("10. TEAM ALLOCATION (6 Members)", level=1)

    team = [
        ("ML Engineer", "NER pipeline, embeddings, re-ranker", "Hours 0-24"),
        ("Backend Dev 1", "FastAPI, Neo4j graph, search", "Hours 0-24"),
        ("Backend Dev 2", "Tender audit, PDF parsing, validation", "Hours 8-24"),
        ("Frontend Dev", "Next.js UI, graph visualization", "Hours 12-30"),
        ("Data Engineer", "BIS scraping, data processing, QCO database", "Hours 0-16"),
        ("Presenter", "Demo scenarios, pitch deck, video backup", "Hours 20-36"),
    ]
    add_table(doc, ["Role", "Responsibilities", "Timeline"], team)

    # ========== CLOSING ==========
    doc.add_heading("11. CLOSING STATEMENT", level=1)

    doc.add_paragraph(
        "StandardsAI is not an incremental improvement over existing tools. It's the FIRST system "
        "that treats Indian Standards as a structured knowledge graph rather than a text search problem. "
        "The dependency resolver, tender audit mode, and certification flagging are features that "
        "NO existing tool provides — and they solve problems that cost the government crores in "
        "procurement disputes every year."
    )

    doc.add_paragraph()
    final = doc.add_paragraph(
        "The AI understands your input. The graph gives you the correct answer. "
        "That's why this solution will win."
    )
    final.runs[0].bold = True

    # Save
    doc.save(os.path.join(OUTPUT_DIR, "FINAL_WINNING_PROPOSAL.docx"))
    print("Created: FINAL_WINNING_PROPOSAL.docx")


if __name__ == "__main__":
    create_final_proposal()
    print("\n✓ Final Winning Proposal created!")
