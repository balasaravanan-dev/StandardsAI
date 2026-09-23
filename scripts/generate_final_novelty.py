"""
Generate FINAL NOVELTY document - Graph-Centric Approach
This is the WINNING strategy - Knowledge Graph as the engine, not LLM
"""

from docx import Document
from docx.shared import Pt
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


def create_final_novelty():
    doc = Document()

    # Title
    title = doc.add_heading("NOVELTY & WINNING APPROACH", 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    subtitle = doc.add_paragraph("Standards Dependency Resolver — A Graph-Centric Architecture")
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

    info = doc.add_paragraph()
    info.add_run("SIH 2024 | Problem ID: 26108 | This Is a GRAPH Problem, Not a Text Problem").italic = True
    info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph()

    # ===========================================
    doc.add_heading("THE CORE INSIGHT", level=1)
    # ===========================================

    doc.add_paragraph(
        "Most teams will build an LLM wrapper — take text in, generate text out. "
        "But standards have STRUCTURED RELATIONSHIPS: normative references, supersession chains, "
        "amendments, certification linkages. The right architecture treats the KNOWLEDGE GRAPH "
        "AS THE ENGINE and uses AI only where it genuinely adds value."
    )

    doc.add_heading("What Doesn't Need AI", level=2)
    no_ai = [
        ("Graph traversal", "Finding normative references is Cypher queries, not LLM prompts"),
        ("Version checking", "Is IS 456:2000 current? Database lookup, not AI"),
        ("Certification checking", "Is cement under QCO? Rule engine, not LLM"),
        ("Conflict detection", "Version constraints are algorithms, not predictions"),
        ("Amendment tracking", "Temporal queries in graph DB, not text generation"),
    ]
    add_table(doc, ["Function", "Why AI Is Overkill"], no_ai)

    doc.add_heading("Where AI Actually Adds Value", level=2)
    yes_ai = [
        ("Understanding messy input", "NER to extract 'stainless steel kitchen plates' → material + product"),
        ("ICS classification", "Multi-label classifier to map description → standard categories"),
        ("Semantic retrieval", "Embeddings for initial candidate retrieval"),
        ("Explanation generation", "LLM writes human-readable justification (last step, not core)"),
    ]
    add_table(doc, ["Function", "Why AI Helps"], yes_ai)

    # ===========================================
    doc.add_heading("THE 7 GENUINELY NOVEL IDEAS", level=1)
    # ===========================================

    # Idea 1
    doc.add_heading("1. Standards Dependency Resolver (like npm/pip)", level=2)

    doc.add_paragraph("Think of standards like software packages with dependencies:")
    doc.add_paragraph(
        "IS 9235:2020 (Stainless Steel Utensils)\n"
        "├── REQUIRES IS 6911:2017 (SS Plate, Sheet & Strip)\n"
        "│   ├── REQUIRES IS 6603:2001 (Chemical Composition)\n"
        "│   └── REQUIRES IS 1586:2000 (Mechanical Testing)\n"
        "├── REQUIRES IS 6912:2003 (Terminology)\n"
        "├── CERTIFICATION: BIS Mark MANDATORY (QCO 2018)\n"
        "└── SUPERSEDES IS 9235:1979"
    )

    doc.add_paragraph("What makes this novel:")
    novel1 = [
        "System resolves the FULL dependency tree — every normative reference, transitively",
        "Detects VERSION CONFLICTS — tender references old version but standard requires new",
        "Checks COMPLETENESS — 'You included IS 9235 but forgot IS 6911, which it requires'",
        "NO LLM does this — it's graph traversal + version constraint solving",
        "Same algorithm that package managers (npm, pip, cargo) use",
    ]
    for item in novel1:
        doc.add_paragraph(item, style='List Bullet')

    # Idea 2
    doc.add_heading("2. Tender Audit Mode (THE KILLER FEATURE)", level=2)

    doc.add_paragraph("Upload an existing tender → system audits it for compliance:")
    doc.add_paragraph(
        "AUDIT RESULTS for Tender #GEM/2024/B/4851023\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "⚠️  IS 4825:1968 — WITHDRAWN. Superseded by IS 4825:2020\n"
        "❌  IS 9235:2020 references IS 6911:2017 — NOT FOUND in tender\n"
        "❌  BIS Mark certification required (QCO) — NOT MENTIONED\n"
        "✅  IS 6603:2001 — Current, valid\n"
        "⚠️  IS 1570:2018 — Amendment 2 (2022) not referenced\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "3 errors, 2 warnings found"
    )

    doc.add_paragraph("Why this is the killer feature:")
    killer = [
        "This is a VALIDATION/LINTING tool, not a search tool",
        "Like a compiler for tender documents — finds errors BEFORE procurement failures",
        "Regex + NER extracts standard references → graph lookup validates each one",
        "ZERO LLM needed for core audit logic — pattern matching + graph queries",
        "Massive real-world impact: catches errors that cost crores in delays",
    ]
    for item in killer:
        doc.add_paragraph(item, style='List Bullet')

    # Idea 3
    doc.add_heading("3. ICS Code Classification → Narrowed Graph Search", level=2)

    doc.add_paragraph("Instead of generic vector similarity, do STRUCTURED CLASSIFICATION first:")

    flow = [
        ("Step 1: NER extracts", "material: stainless steel, product: plates, context: kitchen"),
        ("Step 2: Classify to ICS", "97.040.60 (Kitchen equipment), 77.140.20 (Stainless steels)"),
        ("Step 3: Query graph", "Standards under ICS 97.040.60 ∩ material=stainless steel"),
        ("Step 4: Rank", "By specification overlap (not vector similarity)"),
    ]
    add_table(doc, ["Step", "Output"], flow)

    doc.add_paragraph("Why this beats semantic search:")
    beats = [
        "Semantic search is trivial: 'IS 9235 is about SS utensils, query mentions SS, 0.89 similarity'",
        "ICS classification NARROWS SEARCH SPACE structurally — far fewer false positives",
        "Train a multi-label classifier on ICS codes (well-defined problem with labeled data)",
        "The classifier becomes your DOMAIN-SPECIFIC AI, not a generic embedding",
    ]
    for item in beats:
        doc.add_paragraph(item, style='List Bullet')

    # Idea 4
    doc.add_heading("4. Amendment Chain Compilation", level=2)

    doc.add_paragraph("Standards get amended repeatedly. Show CONSOLIDATED requirements:")
    doc.add_paragraph(
        "IS 9235:2020 — Consolidated View\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Base: Published 2020\n"
        "  └── Amd 1 (2021): Changed clause 4.2.1 (thickness tolerance)\n"
        "  └── Amd 2 (2023): Added Table 3A (new grade requirements)\n\n"
        "Section 4.2.1 — Thickness ← MODIFIED by Amd 1\n"
        "  Original: ±0.05mm\n"
        "  Amended:  ±0.03mm ← CURRENT REQUIREMENT\n\n"
        "⚠️ If your spec says ±0.05mm, it's based on pre-amendment version"
    )

    doc.add_paragraph("Why this is novel:")
    amend = [
        "Nobody builds amendment timelines for Indian Standards",
        "This is a TEMPORAL VERSIONING problem — model each standard as version history with diffs",
        "Genuinely useful — amendments are separate documents and easy to miss",
    ]
    for item in amend:
        doc.add_paragraph(item, style='List Bullet')

    # Idea 5
    doc.add_heading("5. Specification-to-Clause Matching (Sub-Document Level)", level=2)

    doc.add_paragraph("Don't just say 'IS 9235 is relevant.' Show EXACTLY which clauses match:")

    clause_match = [
        ("'18/8 grade stainless steel'", "IS 9235, Clause 4.1: Material shall be austenitic grade (18% Cr, 8% Ni minimum)"),
        ("'food-grade safe'", "IS 9235, Clause 5.3: Migration limits for food contact"),
        ("'corrosion resistant'", "IS 9235, Clause 6.2: Salt spray test per IS 6911, Annex B"),
    ]
    add_table(doc, ["Your Requirement", "Matched Standard Clause"], clause_match)

    doc.add_paragraph("Why this is novel:")
    clause = [
        "SUB-DOCUMENT matching, not document-level retrieval",
        "Chunk standards at clause/section level",
        "Evidence is auditable — officer sees exactly WHY standard was recommended",
        "Difference between 'Google for standards' and 'intelligent standards advisory'",
    ]
    for item in clause:
        doc.add_paragraph(item, style='List Bullet')

    # Idea 6
    doc.add_heading("6. Closed-Set Grounding — Zero Hallucinated Standard Numbers", level=2)

    doc.add_paragraph("The structural guarantee:")
    closed = [
        "LLM output is validated against database BEFORE shown to user",
        "System ABSTAINS when confidence is low instead of guessing",
        "Every standard number in output exists in our graph — provably",
        "Most teams do prompt engineering ('please don't hallucinate')",
        "We do it STRUCTURALLY — impossible to output a fake IS number",
    ]
    for item in closed:
        doc.add_paragraph(item, style='List Bullet')

    # Idea 7
    doc.add_heading("7. Quantified Evaluation with Methodology", level=2)

    metrics = [
        ("Precision@K", "Of top K recommendations, how many are correct?"),
        ("Recall@K", "Of all correct standards, how many did we find?"),
        ("Citation accuracy", "Does the clause actually say what we claim?"),
        ("Hallucination rate", "Should be 0% with closed-set grounding"),
        ("Latency", "Sub-3-second response time"),
    ]
    add_table(doc, ["Metric", "What It Measures"], metrics)

    doc.add_paragraph(
        "Why this wins: Virtually no team will present real accuracy numbers with methodology. "
        "We will — makes us look professional and trustworthy."
    )

    # ===========================================
    doc.add_heading("REVISED ARCHITECTURE", level=1)
    # ===========================================

    doc.add_paragraph("Graph-Centric, Not LLM-Centric:")

    arch = [
        ("Document Parser + NER", "Extract entities from input (minimal AI)"),
        ("ICS Code Classifier", "Multi-label classifier (fine-tuned BERT, not LLM)"),
        ("Hybrid Retrieval", "BM25 + Vector search for candidates"),
        ("KNOWLEDGE GRAPH ENGINE", "THE CORE — dependency resolution, version validation, certification check"),
        ("Reranker + Explainer", "Cross-encoder + LLM (ONLY place LLM is used)"),
        ("Structured Output", "Standards + Dependency tree + Audit warnings + Evidence"),
    ]
    add_table(doc, ["Component", "Function"], arch)

    doc.add_paragraph()
    doc.add_paragraph(
        "The LLM is GARNISH, not the ENTRÉE. The knowledge graph does the real work."
    ).bold = True

    # ===========================================
    doc.add_heading("THE ONE-LINER FOR JUDGES", level=1)
    # ===========================================

    doc.add_paragraph(
        "\"We didn't build a chatbot that guesses which standards might be relevant. "
        "We built a STANDARDS DEPENDENCY RESOLVER — a knowledge graph of 20,000+ Indian Standards "
        "that resolves normative references, detects outdated versions, checks certification requirements, "
        "and audits tender documents for compliance gaps. The AI understands your input; the graph gives "
        "you the correct answer.\""
    )

    # ===========================================
    doc.add_heading("WHY THIS IS UNKILLABLE IN JUDGING", level=1)
    # ===========================================

    unkillable = [
        ("Can you SHOW it?", "Black box", "Visual graph traversal"),
        ("Can you VERIFY it?", "No — hallucinations", "Every path is traceable"),
        ("Can you TEST it?", "Vibes-based", "Precision/Recall metrics"),
        ("Handles edge cases?", "Fails silently", "Explicit 'I don't know'"),
        ("Government-ready?", "No accountability", "Auditable evidence chain"),
    ]
    add_table(doc, ["Dimension", "LLM Wrapper", "Our Graph System"], unkillable)

    # ===========================================
    doc.add_heading("KILLER STAT FOR THE PITCH", level=1)
    # ===========================================

    doc.add_paragraph(
        "\"India has 20,000+ published Indian Standards across 400+ technical committees. "
        "A procurement officer preparing a tender for cement must consider IS 269, IS 455, IS 1489, "
        "IS 3535, IS 4031 (14 parts), IS 4032, IS 516, IS 383, IS 10262 — that's 20+ standards "
        "for ONE product. Today, they do this from memory or by asking colleagues. "
        "Our system does it in 3 seconds.\""
    )

    # ===========================================
    doc.add_heading("FEASIBILITY FOR 36-HOUR HACKATHON", level=1)
    # ===========================================

    feasibility = [
        ("Knowledge graph (metadata)", "HIGH", "Scrape BIS catalog, build in Neo4j/NetworkX"),
        ("Dependency resolution", "HIGH", "Standard graph algorithms"),
        ("Tender audit mode", "HIGH", "Regex extraction + graph lookup"),
        ("ICS classification", "MEDIUM", "Start with keyword rules, upgrade to ML"),
        ("Hybrid search", "HIGH", "Elasticsearch + sentence-transformers"),
        ("Amendment tracking", "MEDIUM", "Parse BIS gazette notifications"),
        ("Clause-level matching", "LOW", "Needs full texts — defer to post-hackathon"),
    ]
    add_table(doc, ["Component", "Feasibility", "Notes"], feasibility)

    # ===========================================
    doc.add_heading("SUMMARY: 7 DIFFERENTIATORS", level=1)
    # ===========================================

    summary = [
        "1. Standards Dependency Resolver — like npm/pip for standards (graph algorithms)",
        "2. Tender Audit Mode — upload tender, get compliance report (killer feature)",
        "3. ICS Classification — structured narrowing, not semantic guessing",
        "4. Amendment Chain Compilation — temporal version tracking",
        "5. Specification-to-Clause Matching — sub-document level evidence",
        "6. Closed-Set Grounding — provably zero hallucinations",
        "7. Quantified Evaluation — real metrics with methodology",
    ]
    for item in summary:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_paragraph()
    final = doc.add_paragraph(
        "This is what separates a hackathon project from a production-ready government system. "
        "The graph gives you correctness. The AI gives you convenience. Together, they give you trust."
    )
    final.runs[0].bold = True

    # Save
    doc.save(os.path.join(OUTPUT_DIR, "00_NOVELTY_FINAL.docx"))
    print("Created: 00_NOVELTY_FINAL.docx")


if __name__ == "__main__":
    create_final_novelty()
    print("\nFinal novelty document created!")
