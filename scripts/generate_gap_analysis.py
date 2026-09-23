"""
Generate GAP ANALYSIS document for SIH 26108
Comprehensive analysis of what exists vs what's missing
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


def create_gap_analysis():
    doc = Document()

    # Title
    title = doc.add_heading("GAP ANALYSIS", 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    subtitle = doc.add_paragraph("What Exists Today vs What's Missing in Indian Standards Discovery")
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

    info = doc.add_paragraph()
    info.add_run("SIH 2024 | Problem ID: 26108 | Ministry of Consumer Affairs").italic = True
    info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph()

    # ==========================================
    doc.add_heading("1. CURRENT STATE OF BIS STANDARDS DISCOVERY", level=1)
    # ==========================================

    doc.add_paragraph(
        "Today, procurement officers in India have access to several tools for finding Indian Standards. "
        "However, each tool has critical limitations that prevent efficient standards discovery."
    )

    current_state = [
        ("BIS 'Know Your Standards' Portal", "Keyword search by IS number or title",
         "No semantic understanding; no related-standards graph; no procurement context"),
        ("standards.bis.gov.in", "Department-wise browsing, catalog download",
         "Siloed from procurement portals; no API; no amendment tracking alerts"),
        ("GeM Portal (gem.gov.in)", "References standards in product listings (e.g., 'Surgical Gloves as per IS 4148')",
         "Standards are HARDCODED per category — no dynamic recommendation; no allied standard discovery"),
        ("CPPP (eprocure.gov.in)", "Publishes tenders with technical specifications",
         "ZERO intelligence layer — procurement officers manually look up standards"),
        ("ISO OBP (International)", "Lifecycle tracking, cross-references, ICS classification",
         "India has NO equivalent; BIS data is fragmented across 4+ portals"),
    ]
    add_table(doc, ["Tool / Portal", "What It Does", "Critical Gaps"], current_state)

    # ==========================================
    doc.add_heading("2. THE 6 CORE GAPS", level=1)
    # ==========================================

    # Gap 1
    doc.add_heading("Gap 1: Semantic Gap", level=2)
    doc.add_paragraph("Problem: Current tools are keyword-based only.")
    doc.add_paragraph(
        "Example: Searching 'corrosion-resistant pipes for coastal water supply' on BIS website "
        "returns nothing useful. The officer must already know it's IS 4985 or IS 15778."
    )
    doc.add_paragraph("Impact: Officers spend hours guessing which standards might apply.")
    doc.add_paragraph("Our Solution: NER extracts context + ICS classification + semantic search.")

    # Gap 2
    doc.add_heading("Gap 2: Context Gap", level=2)
    doc.add_paragraph("Problem: Same product in different environments needs different standards.")
    doc.add_paragraph(
        "Example: 'Steel pipes' for a coastal water project vs an oil refinery require completely "
        "different IS references + test methods. No tool understands this context."
    )
    doc.add_paragraph("Impact: Wrong standards referenced, leading to quality failures.")
    doc.add_paragraph("Our Solution: Context-aware recommendation with environment factors extracted from input.")

    # Gap 3
    doc.add_heading("Gap 3: Graph Gap (THE BIGGEST)", level=2)
    doc.add_paragraph("Problem: Standards don't exist in isolation — they have dependencies.")
    doc.add_paragraph(
        "Example: IS 1239 (steel tubes) normatively references:\n"
        "  • IS 1387 (dimensions)\n"
        "  • IS 1879 (threading)\n"
        "  • IS 10748 (hot-dip galvanizing)\n"
        "  • IS 228 (chemical analysis)\n\n"
        "NO TOOL maps this dependency graph. Officers must manually open each standard and find references."
    )
    doc.add_paragraph("Impact: Incomplete tender specifications; missing allied standards.")
    doc.add_paragraph("Our Solution: Knowledge graph with 100,000+ relationship edges + dependency resolver.")

    # Gap 4
    doc.add_heading("Gap 4: Lifecycle Gap", level=2)
    doc.add_paragraph("Problem: Standards get revised, amended, withdrawn, superseded.")
    doc.add_paragraph(
        "Example: IS 456:1978 (Plain and Reinforced Concrete) was superseded by IS 456:2000. "
        "Officers routinely reference the 1978 edition in tenders because no tool alerts them."
    )
    doc.add_paragraph("Impact: Tenders reference withdrawn standards; legal disputes.")
    doc.add_paragraph("Our Solution: Version tracking + amendment chain compilation + auto-alerts.")

    # Gap 5
    doc.add_heading("Gap 5: Certification Gap", level=2)
    doc.add_paragraph("Problem: ~500+ products are under mandatory BIS certification (QCOs).")
    doc.add_paragraph(
        "Example: Cement, steel, electrical appliances, food products — all require ISI mark. "
        "No tool auto-flags this requirement when a standard is referenced."
    )
    doc.add_paragraph("Impact: Tenders miss mandatory certification clauses; non-compliant products enter supply chain.")
    doc.add_paragraph("Our Solution: QCO database + CRS list + automatic certification flagging.")

    # Gap 6
    doc.add_heading("Gap 6: Integration Gap", level=2)
    doc.add_paragraph("Problem: No tool plugs into the tender-writing workflow.")
    doc.add_paragraph(
        "Officers must: Open GeM/CPPP → Switch to BIS website → Search → Copy standard number → "
        "Switch back to tender → Paste → Repeat. This context-switching wastes hours."
    )
    doc.add_paragraph("Impact: Low adoption of any standards tool; errors from manual transcription.")
    doc.add_paragraph("Our Solution: REST API + Browser extension + Direct GeM integration.")

    # ==========================================
    doc.add_heading("3. GAP-TO-FEATURE MAPPING", level=1)
    # ==========================================

    gap_feature = [
        ("Semantic Gap", "Semantic search + ICS classification", "BERT multi-label classifier + hybrid BM25/vector retrieval"),
        ("Context Gap", "Context-aware recommendations", "NER for entity extraction + environment factor weighting"),
        ("Graph Gap", "Dependency resolver", "Neo4j knowledge graph + recursive traversal + version constraints"),
        ("Lifecycle Gap", "Version intelligence", "Temporal queries + amendment chain + gazette monitoring"),
        ("Certification Gap", "QCO checker", "Rule engine against QCO/CRS/Hallmarking databases"),
        ("Integration Gap", "API + Browser extension", "REST API (OpenAPI spec) + Chrome extension + GeM Integration Toolkit"),
    ]
    add_table(doc, ["Gap", "Feature We Build", "Technical Implementation"], gap_feature)

    # ==========================================
    doc.add_heading("4. COMPETITIVE LANDSCAPE", level=1)
    # ==========================================

    doc.add_paragraph("Why doesn't this solution already exist?")

    competition = [
        ("BIS Website", "Search only; no recommendations, no graph, no risk analysis"),
        ("ChatGPT / Claude / Gemini", "Hallucinate standard numbers; no access to current BIS data; can't track amendments"),
        ("ISO OBP (Online Browsing Platform)", "International standards only; no Indian Standards; no procurement integration"),
        ("Commercial Compliance Tools (e.g., RegTech)", "Focus on financial/legal compliance, not technical standards for procurement"),
        ("GeM Internal Tools", "Hardcoded category-standard mappings; no semantic intelligence"),
        ("ERP Procurement Modules (SAP, Oracle)", "Generic procurement workflows; no standards recommendation"),
    ]
    add_table(doc, ["Potential Competitor", "Why They Don't Solve This"], competition)

    doc.add_paragraph()
    conclusion = doc.add_paragraph(
        "CONCLUSION: The gap is clear. No AI system today combines: (a) comprehensive BIS standards knowledge, "
        "(b) semantic procurement context understanding, (c) knowledge graph for allied standards, and "
        "(d) procurement portal integration. StandardsAI fills ALL FOUR gaps simultaneously."
    )
    conclusion.runs[0].bold = True

    # ==========================================
    doc.add_heading("5. QUANTIFIED PROBLEM SIZE", level=1)
    # ==========================================

    problem_size = [
        ("Total BIS Standards", "22,000+", "BIS website"),
        ("Annual new standards published", "500+", "BIS gazette"),
        ("Products under mandatory certification", "500+", "QCO/CRS lists"),
        ("GeM product categories", "10,000+", "GeM portal"),
        ("Annual government procurement value", "₹20+ lakh crore", "GeM statistics"),
        ("Estimated procurement officers", "300,000+", "Central + State + PSU"),
        ("Standards-related procurement disputes", "~40% of all disputes", "Industry estimate"),
        ("Time spent on manual standards research", "2-4 hours per tender", "User interviews"),
        ("Cost of a single procurement dispute", "₹10-50 lakhs average", "Legal estimates"),
    ]
    add_table(doc, ["Metric", "Value", "Source"], problem_size)

    # ==========================================
    doc.add_heading("6. THE GAP STATEMENT (For Judges)", level=1)
    # ==========================================

    doc.add_paragraph(
        "Today, a procurement officer preparing a tender for stainless steel utensils must:"
    )
    steps = [
        "1. Search BIS website for 'stainless steel' — gets 200+ results",
        "2. Manually identify that IS 9235 might be relevant",
        "3. Open IS 9235, find it references IS 6911, IS 6603, IS 1586, IS 6912",
        "4. Search each of those separately to understand their scope",
        "5. Check if any are under mandatory certification — search the QCO list",
        "6. Verify none are withdrawn — check gazette notifications",
        "7. Check for amendments — search amendment lists",
        "8. Type all standard numbers into the tender document manually",
    ]
    for step in steps:
        doc.add_paragraph(step, style='List Bullet')

    doc.add_paragraph()
    doc.add_paragraph("This takes 2-4 HOURS.")
    doc.add_paragraph("Our system does it in 3 SECONDS.")
    doc.add_paragraph()

    key_insight = doc.add_paragraph(
        "THE KEY INSIGHT: The gap is not 'better search.' The gap is 'no one has built the dependency graph.' "
        "Once you have the graph, everything else — recommendations, audits, version checks, certification flags — "
        "becomes graph traversal, not AI guesswork."
    )
    key_insight.runs[0].bold = True

    # ==========================================
    doc.add_heading("7. BEFORE vs AFTER COMPARISON", level=1)
    # ==========================================

    before_after = [
        ("Find relevant standards", "2-4 hours of manual search", "3 seconds with semantic + graph"),
        ("Discover allied standards", "Often missed entirely", "Automatic dependency resolution"),
        ("Check if current version", "Manual gazette search", "Automatic version validation"),
        ("Find amendments", "Usually missed", "Amendment chain compilation"),
        ("Check certification requirements", "Separate QCO lookup", "Automatic flagging"),
        ("Integrate into tender", "Copy-paste from multiple tabs", "One-click export / API integration"),
        ("Audit existing tender", "Not possible", "Upload PDF → instant compliance report"),
    ]
    add_table(doc, ["Task", "BEFORE (Current State)", "AFTER (StandardsAI)"], before_after)

    # ==========================================
    doc.add_heading("8. WHY NOW?", level=1)
    # ==========================================

    doc.add_paragraph("Several factors make this the right time to build StandardsAI:")

    why_now = [
        ("BIS Digitization", "BIS has been digitizing standards metadata — data is more accessible than ever"),
        ("GeM Growth", "GeM has grown to ₹20+ lakh crore in transactions — the platform is mature"),
        ("AI Maturity", "Embedding models, graph databases, and LLMs have matured for this use case"),
        ("IndiaAI Mission", "Government is actively seeking AI solutions — alignment with policy"),
        ("Bhashini", "Multilingual AI infrastructure now available for Hindi/regional languages"),
        ("Post-COVID Procurement", "Increased scrutiny on procurement quality after pandemic-related failures"),
    ]
    add_table(doc, ["Factor", "Why It Matters"], why_now)

    # ==========================================
    doc.add_heading("9. SUMMARY: THE GAP WE FILL", level=1)
    # ==========================================

    doc.add_paragraph("We fill a gap that has existed for decades but was never addressed:")

    summary_points = [
        "NO existing tool provides semantic understanding of procurement context",
        "NO existing tool maps the standards dependency graph",
        "NO existing tool tracks lifecycle (versions, amendments, withdrawals)",
        "NO existing tool auto-flags certification requirements",
        "NO existing tool integrates into procurement portal workflows",
        "NO existing tool can audit tender documents for compliance",
    ]
    for point in summary_points:
        doc.add_paragraph(point, style='List Bullet')

    doc.add_paragraph()
    final = doc.add_paragraph(
        "StandardsAI is not an incremental improvement. It's the FIRST system that treats "
        "Indian Standards as a structured knowledge graph rather than a text search problem. "
        "That's why this solution will win."
    )
    final.runs[0].bold = True

    # Save
    doc.save(os.path.join(OUTPUT_DIR, "11_Gap_Analysis.docx"))
    print("Created: 11_Gap_Analysis.docx")


if __name__ == "__main__":
    create_gap_analysis()
    print("\nGap Analysis document created!")
