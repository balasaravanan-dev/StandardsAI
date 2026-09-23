"""
Generate DOCX documents for SIH 26108 - StandardsAI
Each document covers a specific aspect of the solution
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
import os

OUTPUT_DIR = r"C:\Users\balak\Downloads\SIH\docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_styled_doc(title, subtitle=""):
    doc = Document()

    # Title
    title_para = doc.add_heading(title, 0)
    title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    if subtitle:
        sub = doc.add_paragraph(subtitle)
        sub.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Add project info
    info = doc.add_paragraph()
    info.add_run("SIH 2024 | Problem ID: 26108 | Ministry of Consumer Affairs").italic = True
    info.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph()  # Spacing
    return doc


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Table Grid'

    # Header row
    hdr_cells = table.rows[0].cells
    for i, header in enumerate(headers):
        hdr_cells[i].text = header
        hdr_cells[i].paragraphs[0].runs[0].bold = True

    # Data rows
    for row_data in rows:
        row_cells = table.add_row().cells
        for i, cell_data in enumerate(row_data):
            row_cells[i].text = str(cell_data)

    doc.add_paragraph()  # Spacing


# ============================================================
# DOCUMENT 1: PROBLEM STATEMENT ANALYSIS
# ============================================================
def create_problem_statement():
    doc = create_styled_doc(
        "Problem Statement Analysis",
        "AI-Powered Recommendation Engine for Indian Standards"
    )

    doc.add_heading("1. Problem Overview", level=1)
    doc.add_paragraph(
        "Government departments, Public Sector Enterprises (PSEs), procurement agencies, and "
        "private organizations procure a wide range of products and services through e-procurement "
        "portals. Procurement officials are required to prepare technical specifications that "
        "reference the appropriate Indian Standards (IS)."
    )

    doc.add_heading("2. Core Challenges", level=1)

    challenges = [
        ("Volume", "22,000+ published BIS standards across 30+ technical departments"),
        ("Complexity", "Standards have complex interdependencies via normative references"),
        ("Currency", "Frequent revisions, amendments, and withdrawals"),
        ("Discovery", "No intelligent search - only keyword matching available"),
        ("Expertise", "Requires domain knowledge most procurement officers lack"),
    ]
    add_table(doc, ["Challenge", "Description"], challenges)

    doc.add_heading("3. Impact of the Problem", level=1)
    impacts = [
        "Tenders reference outdated or withdrawn standards",
        "Missing critical allied standards (safety, test methods, terminology)",
        "Incomplete technical specifications",
        "Procurement disputes and litigation",
        "Reduced product quality in government purchases",
        "₹20+ lakh crore annual procurement at risk",
    ]
    for impact in impacts:
        doc.add_paragraph(impact, style='List Bullet')

    doc.add_heading("4. Current State Analysis", level=1)

    doc.add_heading("4.1 BIS Website (bis.gov.in)", level=2)
    doc.add_paragraph(
        "Offers keyword-based search only. Searching 'steel pipes' returns 500+ results "
        "with no context understanding. Cannot differentiate between pipes for drinking water "
        "vs industrial chemicals. No allied standards linking."
    )

    doc.add_heading("4.2 GeM Portal (gem.gov.in)", level=2)
    doc.add_paragraph(
        "References IS numbers in product listings but has no recommendation system. "
        "Standards are manually embedded by category managers. No automated suggestion."
    )

    doc.add_heading("4.3 Manual Process", level=2)
    doc.add_paragraph(
        "Officers rely on personal knowledge, colleague consultation, or hours of manual "
        "research. Error-prone, time-consuming, and inconsistent across departments."
    )

    doc.add_heading("5. Market Gap Validation", level=1)
    doc.add_paragraph(
        "Research confirms NO existing AI solution for standards recommendation - validated "
        "across ISO, ASTM, IEEE, and BIS. This represents a first-of-its-kind opportunity "
        "aligned with IndiaAI Mission objectives."
    )

    doc.add_heading("6. Domain Research Findings", level=1)
    findings = [
        ("Total BIS Standards", "22,000+"),
        ("Annual Growth", "500+ new standards/year"),
        ("Technical Departments", "30+"),
        ("Mandatory Certifications", "400+ products under compulsory scheme"),
        ("Annual Procurement Value", "₹20+ lakh crore (GeM alone)"),
        ("Certification Types", "ISI Mark, CRS, Hallmarking"),
    ]
    add_table(doc, ["Metric", "Value"], findings)

    doc.add_heading("7. Problem Statement Requirements", level=1)
    requirements = [
        "Accept product descriptions, technical specifications, or tender documents as input",
        "Recommend relevant Indian Standard(s) based on semantic understanding",
        "Identify allied standards including normative references, test methods, terminology",
        "Highlight latest published version and amendments",
        "Suggest mandatory certification requirements (BIS, CRS, Hallmarking)",
        "Support multilingual input and natural language queries",
    ]
    for i, req in enumerate(requirements, 1):
        doc.add_paragraph(f"{i}. {req}")

    doc.save(os.path.join(OUTPUT_DIR, "01_Problem_Statement_Analysis.docx"))
    print("Created: 01_Problem_Statement_Analysis.docx")


# ============================================================
# DOCUMENT 2: PRODUCT THINKING
# ============================================================
def create_product_thinking():
    doc = create_styled_doc(
        "Product Thinking",
        "User-Centered Design for StandardsAI"
    )

    doc.add_heading("1. User Personas", level=1)

    doc.add_heading("1.1 Primary: Procurement Officer", level=2)
    doc.add_paragraph("Profile:")
    persona1 = [
        "Government/PSE employee preparing tender specifications",
        "Age: 30-55, typically with administrative background",
        "May not have deep technical knowledge of product categories",
        "Works under time pressure with strict compliance requirements",
        "Uses GeM portal and government email daily",
    ]
    for item in persona1:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_paragraph("Pain Points:")
    pains1 = [
        "Overwhelmed by 22,000+ standards to search through",
        "Fear of missing critical safety or compliance standards",
        "Time pressure to complete tender specifications",
        "Lack of domain expertise for technical products",
        "No reliable way to verify if standard is current",
    ]
    for item in pains1:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("1.2 Secondary: Tender Evaluator", level=2)
    doc.add_paragraph("Profile:")
    persona2 = [
        "Reviews submitted bids for compliance with tender requirements",
        "Needs to verify if bidders meet all referenced standards",
        "Values completeness and accuracy in specifications",
        "Often works with domain experts for technical evaluation",
    ]
    for item in persona2:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("1.3 Tertiary: Vendor/Supplier", level=2)
    doc.add_paragraph("Profile:")
    persona3 = [
        "Needs to understand applicable standards for their products",
        "Values clarity on certification requirements before bidding",
        "May use system to ensure product compliance",
        "Interested in standards for new product development",
    ]
    for item in persona3:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("2. User Journey Map", level=1)
    journey = [
        ("Trigger", "Officer receives requirement to create tender for specific product"),
        ("Current Pain", "Spends 2-4 hours searching BIS website, asking colleagues"),
        ("Discovery", "Opens StandardsAI, enters product description"),
        ("Processing", "AI analyzes context, searches semantic database"),
        ("Results", "Receives ranked standards with allied standards tree"),
        ("Validation", "Reviews recommendations, checks certifications"),
        ("Action", "Exports specification text to tender document"),
        ("Outcome", "Complete, accurate tender in minutes instead of hours"),
    ]
    add_table(doc, ["Stage", "Description"], journey)

    doc.add_heading("3. Key Differentiators", level=1)

    doc.add_heading("3.1 Semantic Understanding", level=2)
    doc.add_paragraph(
        "Unlike keyword search, our AI understands context. 'Steel pipes for water supply' "
        "is understood to include drinking water safety, corrosion resistance, and pressure "
        "ratings - not just 'pipe' and 'water'."
    )

    doc.add_heading("3.2 Complete Standard Packages", level=2)
    doc.add_paragraph(
        "We don't just return one standard - we return the full dependency tree: main "
        "standard + test methods + terminology + safety + installation standards. A complete "
        "package for comprehensive tender specifications."
    )

    doc.add_heading("3.3 Always Current", level=2)
    doc.add_paragraph(
        "System flags outdated references, shows latest amendments, warns about withdrawn "
        "standards. Daily updates from BIS bulletins ensure currency."
    )

    doc.add_heading("3.4 Compliance Aware", level=2)
    doc.add_paragraph(
        "Automatically identifies mandatory certifications - BIS Product Certification (ISI mark), "
        "Compulsory Registration Scheme (CRS), Hallmarking - preventing compliance gaps."
    )

    doc.add_heading("4. Value Proposition", level=1)
    doc.add_paragraph(
        "\"Describe your product in plain language. Get the complete standards package in seconds. "
        "It's like having a standards expert on call 24/7.\""
    )

    doc.add_heading("5. Success Metrics", level=1)
    metrics = [
        ("Time to Complete Specification", "2-4 hours → 5 minutes", "95% reduction"),
        ("Standards Coverage", "1-2 standards → 5-8 standards", "3x improvement"),
        ("Version Accuracy", "60% current → 99% current", "Near perfect"),
        ("User Satisfaction", "Frustrated → Confident", "Qualitative"),
        ("Adoption Rate", "0 → 10,000 officers", "Year 1 target"),
    ]
    add_table(doc, ["Metric", "Before → After", "Improvement"], metrics)

    doc.save(os.path.join(OUTPUT_DIR, "02_Product_Thinking.docx"))
    print("Created: 02_Product_Thinking.docx")


# ============================================================
# DOCUMENT 3: SYSTEM DESIGN
# ============================================================
def create_system_design():
    doc = create_styled_doc(
        "System Design",
        "Architecture and Components"
    )

    doc.add_heading("1. High-Level Architecture", level=1)
    doc.add_paragraph(
        "StandardsAI follows a layered architecture with clear separation of concerns:"
    )

    layers = [
        ("User Interface Layer", "Web Portal, API Gateway, GeM Integration, Mobile App"),
        ("Application Layer", "Document Parser, Query Processor, Recommendation Engine, Translation Service"),
        ("AI/ML Layer", "Embedding Model, RAG Pipeline, LLM Reasoning, Re-ranking Model"),
        ("Data Layer", "Vector DB (Qdrant), Graph DB (Neo4j), PostgreSQL, BIS Knowledge Base"),
    ]
    add_table(doc, ["Layer", "Components"], layers)

    doc.add_heading("2. Core Components", level=1)

    doc.add_heading("2.1 Document Parser", level=2)
    parser_features = [
        "Extracts text from PDFs, DOCX, and plain text inputs",
        "Identifies product names, specifications, technical parameters",
        "Uses OCR (Tesseract) for scanned documents",
        "Handles tables and structured data extraction",
        "Supports multilingual document processing",
    ]
    for feature in parser_features:
        doc.add_paragraph(feature, style='List Bullet')

    doc.add_heading("2.2 Query Processor", level=2)
    processor_features = [
        "Cleans and normalizes input text",
        "Translates non-English to English while preserving original",
        "Extracts key entities and attributes using NER",
        "Classifies product category for focused search",
        "Handles abbreviations and domain terminology",
    ]
    for feature in processor_features:
        doc.add_paragraph(feature, style='List Bullet')

    doc.add_heading("2.3 Recommendation Engine", level=2)
    doc.add_paragraph("Multi-stage recommendation process:")
    stages = [
        ("Stage 1", "Vector similarity search in standards corpus using embeddings"),
        ("Stage 2", "Knowledge graph traversal for allied standards discovery"),
        ("Stage 3", "LLM re-ranking with context understanding"),
        ("Stage 4", "Certification requirement mapping and flagging"),
    ]
    add_table(doc, ["Stage", "Function"], stages)

    doc.add_heading("2.4 Standards Knowledge Graph", level=2)
    doc.add_paragraph("Graph structure for standards relationships:")
    graph_elements = [
        ("Nodes", "Standards, Products, Organizations, Certifications, Categories"),
        ("Edges", "REFERENCES, SUPERSEDES, ALLIED_TO, TESTED_BY, CERTIFIED_BY"),
        ("Properties", "Version, Status, Amendment Date, Scope, Keywords"),
    ]
    add_table(doc, ["Element", "Details"], graph_elements)

    doc.add_heading("3. Data Flow", level=1)
    flow_steps = [
        "User submits product description or uploads document",
        "Document Parser extracts and structures text content",
        "Query Processor normalizes and translates input",
        "Embedding Model converts query to semantic vector",
        "Vector DB returns top-K similar standards",
        "Graph DB expands results with allied standards",
        "LLM re-ranks and explains recommendations",
        "Certification Mapper adds compliance requirements",
        "Results returned with confidence scores and citations",
    ]
    for i, step in enumerate(flow_steps, 1):
        doc.add_paragraph(f"{i}. {step}")

    doc.add_heading("4. Integration Points", level=1)
    integrations = [
        ("GeM Portal", "REST API for inline recommendations during tender creation"),
        ("BIS Database", "Daily sync of new standards and amendments"),
        ("Bhashini", "API integration for multilingual translation"),
        ("DigiLocker", "OAuth SSO for government user authentication"),
        ("NIC Cloud", "Production hosting with data residency compliance"),
    ]
    add_table(doc, ["System", "Integration Method"], integrations)

    doc.add_heading("5. Architecture Diagram (Text Representation)", level=1)
    doc.add_paragraph(
        "[See separate architecture diagram image]\n\n"
        "USER INTERFACE LAYER\n"
        "    ↓\n"
        "APPLICATION LAYER (FastAPI)\n"
        "    ↓\n"
        "AI/ML LAYER (Embeddings + RAG + LLM)\n"
        "    ↓\n"
        "DATA LAYER (Qdrant + Neo4j + PostgreSQL)"
    )

    doc.save(os.path.join(OUTPUT_DIR, "03_System_Design.docx"))
    print("Created: 03_System_Design.docx")


# ============================================================
# DOCUMENT 4: TECHNICAL ARCHITECTURE
# ============================================================
def create_technical_architecture():
    doc = create_styled_doc(
        "Technical Architecture",
        "Technology Stack and Implementation Details"
    )

    doc.add_heading("1. Technology Stack", level=1)

    stack = [
        ("Frontend", "Next.js 14 + TypeScript + Tailwind CSS", "Modern, accessible, SSR for SEO"),
        ("Backend", "FastAPI (Python 3.11+)", "Best ML ecosystem, async, auto docs"),
        ("Vector DB", "ChromaDB (MVP) → Qdrant (prod)", "Fast prototyping, scalable production"),
        ("Graph DB", "Neo4j Community Edition", "Native graph queries, free tier"),
        ("Primary DB", "PostgreSQL 15", "Battle-tested, government approved"),
        ("Embeddings", "BAAI/bge-base-en-v1.5", "Free, fast, accurate"),
        ("Multilingual", "paraphrase-multilingual-MiniLM-L12-v2", "Hindi + 100 languages"),
        ("LLM", "Claude API / Groq + Llama 3.1", "Accuracy with free fallback"),
        ("Translation", "Bhashini API / IndicTrans2", "Government initiative alignment"),
        ("Document Processing", "LangChain + PyMuPDF + Unstructured", "Handles all formats"),
        ("Visualization", "React Flow + Recharts", "Interactive graphs and charts"),
        ("Deployment", "Docker + Railway/Render → NIC Cloud", "Fast demo, gov production"),
    ]
    add_table(doc, ["Layer", "Technology", "Rationale"], stack)

    doc.add_heading("2. Data Sources", level=1)
    sources = [
        ("BIS Standards Catalog", "services.bis.gov.in", "IS numbers, titles, scopes, categories"),
        ("Standards Download", "standardsbis.bsbedge.com", "Full standard PDFs"),
        ("Know Your Standards", "bis.gov.in/know-your-standards", "Standard lookup tool"),
        ("GeM Portal", "gem.gov.in", "Product categories with IS references"),
        ("BIS Bulletin", "bis.gov.in", "Weekly new/revised standards"),
    ]
    add_table(doc, ["Source", "URL", "Data Available"], sources)

    doc.add_heading("3. API Design", level=1)

    doc.add_heading("3.1 Recommendation Endpoint", level=2)
    doc.add_paragraph("POST /api/v1/recommend")
    doc.add_paragraph("Request Body:")
    doc.add_paragraph(
        '{\n'
        '  "query": "Steel pipes for drinking water supply",\n'
        '  "input_type": "text",\n'
        '  "language": "en",\n'
        '  "include_allied": true,\n'
        '  "include_certifications": true,\n'
        '  "max_results": 10\n'
        '}'
    )

    doc.add_paragraph("Response:")
    doc.add_paragraph(
        '{\n'
        '  "primary_standards": [...],\n'
        '  "allied_standards": [...],\n'
        '  "certifications": [...],\n'
        '  "query_understood": "...",\n'
        '  "standard_graph": {...}\n'
        '}'
    )

    doc.add_heading("3.2 Additional Endpoints", level=2)
    endpoints = [
        ("GET /api/v1/standards", "List all standards with pagination"),
        ("GET /api/v1/standards/{is_number}", "Get specific standard details"),
        ("POST /api/v1/upload", "Upload document for analysis"),
        ("GET /api/v1/graph/{is_number}", "Get standards relationship graph"),
        ("GET /health", "Health check endpoint"),
    ]
    add_table(doc, ["Endpoint", "Description"], endpoints)

    doc.add_heading("4. Data Pipeline", level=1)
    pipeline = [
        ("Ingestion", "Scrape BIS catalog, download PDFs, fetch GeM data"),
        ("Extraction", "Parse PDFs, extract metadata, identify relationships"),
        ("Processing", "Clean text, normalize terminology, generate embeddings"),
        ("Storage", "PostgreSQL (metadata), Qdrant (vectors), Neo4j (graph)"),
        ("Updates", "Daily sync with BIS bulletin for new/amended standards"),
    ]
    add_table(doc, ["Stage", "Operations"], pipeline)

    doc.add_heading("5. Government AI Infrastructure", level=1)
    doc.add_paragraph("Leveraging existing government AI initiatives:")
    gov_infra = [
        ("Bhashini", "bhashini.gov.in", "Multilingual NLP for Indian languages"),
        ("IndiaAI/AIRAWAT", "indiaai.gov.in", "GPU compute for ML training"),
        ("DigiLocker", "digilocker.gov.in", "Government SSO authentication"),
        ("NIC Cloud", "cloud.gov.in", "Secure government hosting"),
    ]
    add_table(doc, ["Initiative", "URL", "Usage"], gov_infra)

    doc.add_heading("6. Embedding Strategy", level=1)
    doc.add_paragraph("Chunking strategy for standards documents:")
    chunks = [
        "Metadata Chunk: title, number, scope, committee",
        "Scope & Definition Chunk: defines applicability",
        "Technical Requirements Chunks: by section (512 tokens, 50 overlap)",
        "Test Methods Chunk: verification procedures",
        "Marking & Packaging Chunk: labeling requirements",
        "Annexures Chunks: additional technical details",
    ]
    for chunk in chunks:
        doc.add_paragraph(chunk, style='List Bullet')

    doc.save(os.path.join(OUTPUT_DIR, "04_Technical_Architecture.docx"))
    print("Created: 04_Technical_Architecture.docx")


# ============================================================
# DOCUMENT 5: SECURITY
# ============================================================
def create_security():
    doc = create_styled_doc(
        "Security",
        "Threat Model, Measures, and Compliance"
    )

    doc.add_heading("1. Threat Model", level=1)
    threats = [
        ("Data Leakage", "High", "Tender information exposed", "E2E encryption, no query logging"),
        ("API Abuse/DDoS", "Medium", "Service unavailability", "Rate limiting, API keys, WAF"),
        ("LLM Prompt Injection", "Medium", "Malicious output generation", "Input sanitization, output validation"),
        ("Unauthorized Access", "High", "Data breach", "OAuth 2.0, RBAC, MFA"),
        ("Data Poisoning", "Low", "Corrupted recommendations", "Verified sources only, audit trail"),
        ("Man-in-the-Middle", "Medium", "Data interception", "TLS 1.3, certificate pinning"),
    ]
    add_table(doc, ["Threat", "Risk Level", "Impact", "Mitigation"], threats)

    doc.add_heading("2. Authentication & Authorization", level=1)
    auth_measures = [
        "OAuth 2.0 with government SSO (DigiLocker/eSign)",
        "Role-Based Access Control (RBAC) with defined permission levels",
        "API key management for third-party integrations",
        "Session timeout and secure token handling",
        "Multi-factor authentication for admin access",
    ]
    for measure in auth_measures:
        doc.add_paragraph(measure, style='List Bullet')

    doc.add_heading("3. Data Protection", level=1)

    doc.add_heading("3.1 Encryption", level=2)
    encryption = [
        ("In Transit", "TLS 1.3 for all API communications"),
        ("At Rest", "AES-256 encryption for stored data"),
        ("Database", "Encrypted connections, field-level encryption for sensitive data"),
    ]
    add_table(doc, ["Type", "Implementation"], encryption)

    doc.add_heading("3.2 Data Handling", level=2)
    handling = [
        "No PII stored beyond session requirements",
        "Tender documents processed in memory only - never persisted",
        "Query logs anonymized and aggregated for analytics",
        "Automatic data retention policy enforcement",
        "Secure deletion procedures for all temporary data",
    ]
    for item in handling:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("4. Government Compliance", level=1)
    compliance = [
        ("GIGW", "Guidelines for Indian Government Websites - UI/UX standards"),
        ("IT Act 2000", "Information Technology Act compliance"),
        ("Data Residency", "All data stored within India (mandatory)"),
        ("MeitY Guidelines", "Ministry guidelines for government software"),
        ("CERT-In", "Incident reporting requirements"),
    ]
    add_table(doc, ["Standard", "Description"], compliance)

    doc.add_heading("5. LLM Security", level=1)
    llm_security = [
        "Input sanitization before all LLM API calls",
        "Output validation and filtering for unexpected responses",
        "Self-hosted LLM option (Llama) for sensitive deployments",
        "No training on user queries or tender data",
        "Prompt injection detection and blocking",
        "Rate limiting on LLM calls to prevent abuse",
    ]
    for item in llm_security:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("6. Security Operations", level=1)
    secops = [
        ("VAPT", "Regular Vulnerability Assessment and Penetration Testing"),
        ("Audit Logging", "Complete trail of all sensitive operations"),
        ("Monitoring", "24/7 security monitoring and alerting"),
        ("Incident Response", "Defined playbooks for security incidents"),
        ("Access Reviews", "Quarterly review of access permissions"),
    ]
    add_table(doc, ["Practice", "Description"], secops)

    doc.add_heading("7. Deployment Security", level=1)
    deploy_security = [
        "Container security scanning before deployment",
        "Network segmentation and firewall rules",
        "Secrets management via HashiCorp Vault or AWS Secrets Manager",
        "Immutable infrastructure with automated patching",
        "Disaster recovery with encrypted backups",
    ]
    for item in deploy_security:
        doc.add_paragraph(item, style='List Bullet')

    doc.save(os.path.join(OUTPUT_DIR, "05_Security.docx"))
    print("Created: 05_Security.docx")


# ============================================================
# DOCUMENT 6: SCALABILITY
# ============================================================
def create_scalability():
    doc = create_styled_doc(
        "Scalability",
        "Load Projections and Scaling Strategy"
    )

    doc.add_heading("1. Load Projections", level=1)
    projections = [
        ("Daily Queries", "1,000", "50,000", "500,000"),
        ("Concurrent Users", "50", "500", "5,000"),
        ("Standards in DB", "20,000", "25,000", "35,000"),
        ("Response Time (p95)", "<3s", "<2s", "<1s"),
        ("Uptime SLA", "99%", "99.5%", "99.9%"),
    ]
    add_table(doc, ["Metric", "Initial", "Year 1", "Year 3"], projections)

    doc.add_heading("2. Horizontal Scaling Strategy", level=1)
    h_scaling = [
        "Stateless application servers behind load balancer",
        "Kubernetes for container orchestration and auto-scaling",
        "Auto-scaling based on CPU/memory thresholds",
        "Pod Disruption Budgets for zero-downtime deployments",
        "Horizontal Pod Autoscaler (HPA) for dynamic scaling",
    ]
    for item in h_scaling:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("3. Database Scaling", level=1)

    doc.add_heading("3.1 PostgreSQL", level=2)
    pg_scaling = [
        "Read replicas for query distribution",
        "Connection pooling with PgBouncer",
        "Partitioning for large tables",
        "Regular vacuuming and index optimization",
    ]
    for item in pg_scaling:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("3.2 Qdrant (Vector DB)", level=2)
    qdrant_scaling = [
        "Cluster mode with automatic sharding",
        "Replication for high availability",
        "HNSW index optimization for fast search",
        "Separate collections for different embedding types",
    ]
    for item in qdrant_scaling:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("3.3 Neo4j (Graph DB)", level=2)
    neo4j_scaling = [
        "Causal clustering for read scaling",
        "Core servers for write operations",
        "Read replicas for query distribution",
        "Index optimization for traversal queries",
    ]
    for item in neo4j_scaling:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("4. Caching Strategy", level=1)
    caching = [
        ("Redis Cluster", "Frequently queried standards and recommendations"),
        ("CDN", "Static assets, documentation, UI components"),
        ("Query Cache", "Recent query results (TTL: 1 hour)"),
        ("Embedding Cache", "Pre-computed embeddings for common terms"),
        ("Graph Cache", "Frequently accessed relationship paths"),
    ]
    add_table(doc, ["Cache Type", "Usage"], caching)

    doc.add_heading("5. Async Processing", level=1)
    async_proc = [
        "Celery + RabbitMQ for background job processing",
        "Document upload processing in worker pods",
        "Batch embedding generation for new standards",
        "Webhook callbacks for async results",
        "Priority queues for different request types",
    ]
    for item in async_proc:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("6. Infrastructure Architecture", level=1)
    infra = [
        ("Cloud Provider", "NIC Cloud (production) / AWS GovCloud (backup)"),
        ("Primary Region", "Delhi NCR"),
        ("DR Region", "Mumbai"),
        ("Edge Locations", "Hyderabad, Chennai, Kolkata"),
        ("CDN", "CloudFront / Akamai"),
    ]
    add_table(doc, ["Component", "Configuration"], infra)

    doc.add_heading("7. Performance Optimization", level=1)
    perf_opts = [
        "Query optimization with EXPLAIN ANALYZE",
        "Connection pooling for all database connections",
        "Gzip compression for API responses",
        "Lazy loading for UI components",
        "Pre-computed recommendations for popular categories",
        "Edge caching for static API responses",
    ]
    for item in perf_opts:
        doc.add_paragraph(item, style='List Bullet')

    doc.save(os.path.join(OUTPUT_DIR, "06_Scalability.docx"))
    print("Created: 06_Scalability.docx")


# ============================================================
# DOCUMENT 7: ENGINEERING DECISIONS
# ============================================================
def create_engineering_decisions():
    doc = create_styled_doc(
        "Engineering Decisions",
        "Key Trade-offs and Technical Choices"
    )

    doc.add_heading("1. Key Trade-offs", level=1)
    tradeoffs = [
        ("Embedding Model", "OpenAI vs Self-hosted", "Self-hosted (BGE)", "Data sovereignty, no API dependency"),
        ("LLM", "Claude API vs Llama", "Hybrid approach", "Accuracy with cost fallback"),
        ("Vector DB", "Pinecone vs Qdrant", "Qdrant", "Self-hosted option, no vendor lock-in"),
        ("Graph DB", "Neo4j vs ArangoDB", "Neo4j", "Mature ecosystem, Cypher queries"),
        ("Search", "Pure vector vs Hybrid", "Hybrid", "Keywords matter for IS numbers"),
        ("Frontend", "React vs Next.js", "Next.js", "SSR for SEO, API routes"),
    ]
    add_table(doc, ["Decision", "Options", "Choice", "Rationale"], tradeoffs)

    doc.add_heading("2. Why Semantic Search Over Keyword?", level=1)
    doc.add_paragraph(
        "Example Query: 'Corrosion resistant pipes for coastal area water supply'"
    )

    doc.add_heading("2.1 Keyword Search Results", level=2)
    keyword_results = [
        "Matches 'pipe', 'water' literally",
        "Returns generic pipe standards",
        "Misses context of 'coastal' (marine environment)",
        "Ignores 'corrosion resistant' requirement",
        "User must manually filter 500+ results",
    ]
    for item in keyword_results:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("2.2 Semantic Search Results", level=2)
    semantic_results = [
        "IS 4736 - Hot dip zinc coating (coastal corrosion protection)",
        "IS 15778 - CPVC pipes (corrosion resistant material)",
        "IS 10500 - Drinking water specification (potable water context)",
        "IS 4984 - HDPE pipes (alternative corrosion-resistant option)",
    ]
    for item in semantic_results:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("3. RAG vs Fine-tuning", level=1)
    doc.add_paragraph("We chose RAG (Retrieval Augmented Generation) over fine-tuning:")
    rag_reasons = [
        "Standards change frequently - RAG allows real-time updates",
        "No need to retrain model when standards are added/revised",
        "Citations are natural - every recommendation traceable to source",
        "Lower compute requirements for deployment",
        "Reduces hallucination by grounding in actual documents",
    ]
    for reason in rag_reasons:
        doc.add_paragraph(reason, style='List Bullet')

    doc.add_heading("4. Chunking Strategy", level=1)
    doc.add_paragraph("Standards documents chunked for optimal retrieval:")
    chunks = [
        ("Chunk Size", "512 tokens", "Balances context and specificity"),
        ("Overlap", "50 tokens", "Ensures context continuity"),
        ("Boundary Preservation", "Section-based", "Maintains semantic coherence"),
        ("Metadata", "IS number in each chunk", "Enables source attribution"),
    ]
    add_table(doc, ["Aspect", "Value", "Rationale"], chunks)

    doc.add_heading("5. Graph vs Relational for Relationships", level=1)
    doc.add_paragraph("Neo4j chosen over PostgreSQL foreign keys:")
    graph_reasons = [
        "Standards relationships are naturally graph-shaped",
        "Multi-hop traversals (standard → reference → reference) are native",
        "Cypher queries are intuitive for relationship exploration",
        "Visualization of standards network is built-in",
        "Path-finding algorithms for related standards",
    ]
    for reason in graph_reasons:
        doc.add_paragraph(reason, style='List Bullet')

    doc.add_heading("6. Multilingual Approach", level=1)
    doc.add_paragraph("Translation-first vs multilingual embeddings:")
    multilingual = [
        ("Approach", "Translate to English, then embed + search"),
        ("Translation", "Bhashini API for government alignment"),
        ("Fallback", "IndicTrans2 for self-hosted option"),
        ("Rationale", "Standards corpus is in English; translation ensures accuracy"),
        ("Output", "Results displayed in original language with English details"),
    ]
    add_table(doc, ["Aspect", "Choice/Details"], multilingual)

    doc.add_heading("7. API-First Design", level=1)
    doc.add_paragraph("Benefits of API-first architecture:")
    api_benefits = [
        "GeM integration without UI dependency",
        "Mobile app can use same backend",
        "Third-party ERP integrations enabled",
        "Clear contract between frontend and backend",
        "Easier testing and documentation",
    ]
    for benefit in api_benefits:
        doc.add_paragraph(benefit, style='List Bullet')

    doc.save(os.path.join(OUTPUT_DIR, "07_Engineering_Decisions.docx"))
    print("Created: 07_Engineering_Decisions.docx")


# ============================================================
# DOCUMENT 8: COMMUNICATION
# ============================================================
def create_communication():
    doc = create_styled_doc(
        "Communication",
        "Stakeholder Management and Change Strategy"
    )

    doc.add_heading("1. Stakeholder Mapping", level=1)
    stakeholders = [
        ("BIS", "Data partner, standards authority", "MoU for data access, co-branding"),
        ("GeM Portal", "Integration partner", "API integration, joint pilot program"),
        ("DoCA", "Problem owner, ministry sponsor", "Monthly reviews, compliance reports"),
        ("NIC", "Hosting and security partner", "Technical integration, security audit"),
        ("Procurement Officers", "End users", "Training sessions, feedback collection"),
        ("Vendors/Suppliers", "Secondary users", "User guides, support channel"),
    ]
    add_table(doc, ["Stakeholder", "Interest", "Engagement Strategy"], stakeholders)

    doc.add_heading("2. Communication Channels", level=1)
    channels = [
        ("Ministry Updates", "Monthly progress reports, quarterly reviews"),
        ("Technical Partners", "Weekly sync calls, shared documentation"),
        ("End Users", "In-app notifications, email newsletters"),
        ("Public", "Press releases, social media updates"),
    ]
    add_table(doc, ["Audience", "Channel/Frequency"], channels)

    doc.add_heading("3. Training Program", level=1)

    doc.add_heading("3.1 Training Materials", level=2)
    materials = [
        "Video tutorials in Hindi and English (5-10 minute modules)",
        "Quick reference cards (printable A4 format)",
        "Interactive demo environment for practice",
        "FAQ document with common scenarios",
        "Troubleshooting guide for common issues",
    ]
    for material in materials:
        doc.add_paragraph(material, style='List Bullet')

    doc.add_heading("3.2 Training Delivery", level=2)
    delivery = [
        ("Virtual Webinars", "Weekly sessions for new users"),
        ("In-person Workshops", "Major procurement hubs (Delhi, Mumbai, Chennai)"),
        ("Train-the-Trainer", "Departmental champions program"),
        ("Self-paced Learning", "Online modules with certification"),
    ]
    add_table(doc, ["Format", "Details"], delivery)

    doc.add_heading("4. Change Management", level=1)

    doc.add_heading("4.1 Adoption Strategy", level=2)
    adoption = [
        ("Phase 1", "Optional tool alongside existing process - build familiarity"),
        ("Phase 2", "Recommended use - flag if system not consulted"),
        ("Phase 3", "Integrated into tender creation workflow - default tool"),
    ]
    add_table(doc, ["Phase", "Approach"], adoption)

    doc.add_heading("4.2 Resistance Management", level=2)
    resistance = [
        "Address 'AI replacing humans' concern - position as assistant, not replacement",
        "Show time savings with real examples from pilot users",
        "Provide escape hatch - manual process always available",
        "Celebrate early adopters and success stories",
        "Executive sponsorship for organizational buy-in",
    ]
    for item in resistance:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("5. Feedback Loop", level=1)
    feedback = [
        ("In-app Feedback", "Thumbs up/down on recommendations, comment box"),
        ("Monthly Surveys", "NPS score, feature requests, pain points"),
        ("User Interviews", "Quarterly deep-dive sessions with power users"),
        ("Usage Analytics", "Track adoption, popular queries, drop-off points"),
        ("Bug Reporting", "In-app issue reporting with screenshot capture"),
    ]
    add_table(doc, ["Mechanism", "Description"], feedback)

    doc.add_heading("6. Success Metrics for Adoption", level=1)
    success = [
        ("Awareness", "80% of target users know about the tool"),
        ("Trial", "50% have tried at least one query"),
        ("Adoption", "30% use regularly (weekly)"),
        ("Advocacy", "10% actively recommend to colleagues"),
        ("Dependency", "Tool becomes default for specifications"),
    ]
    add_table(doc, ["Stage", "Target"], success)

    doc.save(os.path.join(OUTPUT_DIR, "08_Communication.docx"))
    print("Created: 08_Communication.docx")


# ============================================================
# DOCUMENT 9: PITCHING
# ============================================================
def create_pitching():
    doc = create_styled_doc(
        "Pitching",
        "Presentation Strategy and Demo Script"
    )

    doc.add_heading("1. Elevator Pitch (30 seconds)", level=1)
    doc.add_paragraph(
        "\"Every year, Indian government spends Rs. 15 lakh crore on procurement. Incorrect or "
        "missing standards in tenders lead to quality failures and legal disputes. Our AI engine "
        "analyzes tender specifications and instantly recommends the complete set of applicable "
        "Indian Standards - not just keywords, but understanding context. It's like having a "
        "standards expert on call 24/7, integrated directly into GeM.\""
    )

    doc.add_heading("2. Problem Statement (for judges)", level=1)
    problems = [
        "22,000+ BIS standards, growing 500+/year",
        "Average procurement officer knows <100 standards",
        "40% of procurement disputes involve standards issues (estimated)",
        "Current solution: manual search, colleague consultation",
        "Result: Outdated references, missing safety standards, litigation",
    ]
    for problem in problems:
        doc.add_paragraph(problem, style='List Bullet')

    doc.add_heading("3. Solution Summary", level=1)
    doc.add_paragraph("Input: Product description in any Indian language")
    doc.add_paragraph("Output:")
    outputs = [
        "Primary applicable standards (ranked by relevance)",
        "Allied standards tree (test methods, safety, terminology)",
        "Latest versions with amendment history",
        "Mandatory certification flags (BIS, CRS, Hallmarking)",
        "Export-ready specification text",
    ]
    for output in outputs:
        doc.add_paragraph(output, style='List Bullet')

    doc.add_heading("4. Demo Flow", level=1)

    doc.add_heading("4.1 Demo Scenario 1: Simple Query", level=2)
    doc.add_paragraph("Query: \"LED bulbs for government office lighting\"")
    doc.add_paragraph("Expected Results:")
    demo1 = [
        "IS 16102 - LED lamps safety requirements",
        "IS 10322 - Luminaires requirements",
        "BIS Product Certification flag (mandatory)",
    ]
    for item in demo1:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("4.2 Demo Scenario 2: Complex Context", level=2)
    doc.add_paragraph("Query: \"Corrosion resistant pipes for coastal drinking water supply\"")
    doc.add_paragraph("Expected Results:")
    demo2 = [
        "IS 1239 - Steel tubes (primary)",
        "IS 4736 - Zinc coating (coastal protection)",
        "IS 10500 - Drinking water specification",
        "IS 4984 - HDPE pipes (alternative)",
    ]
    for item in demo2:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("4.3 Demo Scenario 3: Multilingual", level=2)
    doc.add_paragraph("Query (Hindi): \"सड़क निर्माण के लिए सीमेंट\"")
    doc.add_paragraph("Expected Results:")
    demo3 = [
        "IS 269 - OPC cement",
        "IS 455 - PSC cement",
        "IS 1489 - PPC cement",
        "Usage guidance based on application",
    ]
    for item in demo3:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("5. Competitive Advantage", level=1)
    comparison = [
        ("Semantic search", "Yes", "No (keyword only)", "N/A"),
        ("Allied standards", "Auto-linked", "Manual lookup", "Expert knowledge"),
        ("Latest version", "Automatic", "Manual check", "Often missed"),
        ("Multilingual", "22 languages", "English/Hindi", "Depends"),
        ("Integration", "API/GeM ready", "Standalone", "None"),
        ("Response time", "<3 seconds", "Minutes", "Hours/Days"),
    ]
    add_table(doc, ["Feature", "StandardsAI", "BIS Website", "Manual"], comparison)

    doc.add_heading("6. Impact Metrics", level=1)
    metrics = [
        ("Time Saved", "80% reduction in standards research time"),
        ("Accuracy", "95% relevant standard identification"),
        ("Completeness", "3x more allied standards referenced per tender"),
        ("Disputes", "50% reduction in standards-related procurement disputes"),
        ("Adoption", "Target 10,000 procurement officers in Year 1"),
    ]
    add_table(doc, ["Metric", "Projected Impact"], metrics)

    doc.add_heading("7. Anticipated Questions & Answers", level=1)

    qas = [
        ("How do you get BIS data?",
         "BIS publishes a public catalog at services.bis.gov.in. We scrape for MVP, "
         "propose formal partnership for production."),
        ("What about accuracy?",
         "RAG grounds AI in actual data with citations. Human review recommended "
         "for critical decisions."),
        ("How is this different from ChatGPT?",
         "ChatGPT has outdated knowledge, can't traverse standards graph, can't track "
         "amendments. We're domain-specific and always current."),
        ("Security for tender information?",
         "Documents processed in memory only, never stored. All data in India. "
         "Self-hosted LLM option available."),
        ("Multilingual support?",
         "Bhashini integration for all 22 scheduled languages. Government initiative alignment."),
    ]
    for q, a in qas:
        doc.add_paragraph(f"Q: {q}", style='List Bullet')
        doc.add_paragraph(f"A: {a}")

    doc.add_heading("8. Closing Statement", level=1)
    doc.add_paragraph(
        "\"Every correctly referenced standard prevents a procurement dispute. "
        "Every dispute prevented saves lakhs in litigation and months in delays. "
        "StandardsAI makes this automatic.\""
    )

    doc.save(os.path.join(OUTPUT_DIR, "09_Pitching.docx"))
    print("Created: 09_Pitching.docx")


# ============================================================
# DOCUMENT 10: IMPLEMENTATION ROADMAP
# ============================================================
def create_implementation_roadmap():
    doc = create_styled_doc(
        "Implementation Roadmap",
        "MVP Timeline, Phases, and Team Roles"
    )

    doc.add_heading("1. Phase 1: MVP (Hackathon - 36 hours)", level=1)

    doc.add_heading("1.1 Critical Path Timeline", level=2)
    mvp_timeline = [
        ("Hours 0-4", "Data Prep", "Scrape 500 BIS standards metadata from bis.gov.in"),
        ("Hours 4-12", "Backend Core", "FastAPI server, embeddings, ChromaDB, recommendation API"),
        ("Hours 8-16", "Knowledge Graph", "Neo4j setup, standard relationships, graph traversal"),
        ("Hours 12-20", "Frontend", "Next.js UI, search form, results display, graph visualization"),
        ("Hours 20-24", "Integration", "End-to-end testing, error handling, polish"),
        ("Hours 24-36", "Demo Polish", "Demo scenarios, Hindi demo, pitch deck, video backup"),
    ]
    add_table(doc, ["Time", "Task", "Deliverable"], mvp_timeline)

    doc.add_heading("1.2 Must Have Features", level=2)
    must_have = [
        "Web interface with text input",
        "Semantic search on 500 standards dataset",
        "Top 5 recommendations with relevance scores",
        "Basic allied standards linking",
        "Demo-ready presentation",
    ]
    for feature in must_have:
        doc.add_paragraph(feature, style='List Bullet')

    doc.add_heading("1.3 Nice to Have Features", level=2)
    nice_to_have = [
        "Document upload (PDF)",
        "Hindi language support",
        "Interactive standards graph visualization",
        "Certification requirement flags",
    ]
    for feature in nice_to_have:
        doc.add_paragraph(feature, style='List Bullet')

    doc.add_heading("2. Phase 2: Pilot (3 months post-hackathon)", level=1)
    pilot = [
        "Full BIS standards ingestion (22,000+)",
        "Knowledge graph completion with all relationships",
        "GeM API integration prototype",
        "User authentication and search history",
        "Feedback collection system",
        "Security audit and VAPT",
    ]
    for item in pilot:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("3. Phase 3: Production (6-12 months)", level=1)
    production = [
        "Full multilingual support (22 languages)",
        "Production security hardening",
        "Scalability to 100K daily queries",
        "Mobile app (Android/iOS)",
        "Certification mapping automation",
        "Analytics dashboard for ministry",
        "GeM production integration",
    ]
    for item in production:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading("4. Team Roles", level=1)
    team = [
        ("ML Engineer", "Embeddings, RAG pipeline, LLM integration, model optimization"),
        ("Backend Developer", "FastAPI, database design, API development, caching"),
        ("Frontend Developer", "Next.js UI, UX design, responsive design, accessibility"),
        ("Data Engineer", "Standards data processing, ETL pipeline, data quality"),
        ("Domain Expert", "Standards knowledge, demo scenarios, user validation"),
        ("Presenter/Designer", "Pitch deck, demo script, visuals, documentation"),
    ]
    add_table(doc, ["Role", "Responsibilities"], team)

    doc.add_heading("5. Risk Mitigation", level=1)
    risks = [
        ("BIS data access denied", "Medium", "Critical", "Early engagement, show public benefit, explore scraping"),
        ("LLM hallucinations", "Medium", "High", "RAG with citations, human-in-loop"),
        ("Low user adoption", "Medium", "High", "Strong training, make genuinely useful"),
        ("Scale issues", "Low", "Medium", "Proper architecture, load testing"),
        ("Security breach", "Low", "Critical", "Gov security guidelines, audits"),
    ]
    add_table(doc, ["Risk", "Probability", "Impact", "Mitigation"], risks)

    doc.add_heading("6. Success Criteria", level=1)

    doc.add_heading("6.1 MVP Success (Hackathon)", level=2)
    mvp_success = [
        "Working demo with 3+ query scenarios",
        "Response time under 5 seconds",
        "Accurate recommendations for demo queries",
        "Clean, functional UI",
        "Compelling pitch presentation",
    ]
    for criteria in mvp_success:
        doc.add_paragraph(criteria, style='List Bullet')

    doc.add_heading("6.2 Pilot Success (3 months)", level=2)
    pilot_success = [
        "100+ procurement officers using the system",
        "Positive feedback score (NPS > 30)",
        "95% accuracy on test queries",
        "GeM integration prototype working",
        "Security audit passed",
    ]
    for criteria in pilot_success:
        doc.add_paragraph(criteria, style='List Bullet')

    doc.add_heading("6.3 Production Success (12 months)", level=2)
    prod_success = [
        "10,000+ active users",
        "99.5% uptime achieved",
        "Full GeM integration live",
        "Measurable reduction in disputes",
        "Ministry endorsement for national rollout",
    ]
    for criteria in prod_success:
        doc.add_paragraph(criteria, style='List Bullet')

    doc.add_heading("7. Budget Estimate", level=1)
    budget = [
        ("Cloud Infrastructure", "Rs. 50,000/month", "Scaling with usage"),
        ("LLM API Costs", "Rs. 20,000/month", "Claude/Groq usage"),
        ("Domain & SSL", "Rs. 5,000/year", "One-time setup"),
        ("Development Tools", "Rs. 10,000/month", "IDEs, CI/CD, monitoring"),
        ("Total Year 1", "Rs. 10-12 lakhs", "Before government funding"),
    ]
    add_table(doc, ["Item", "Cost", "Notes"], budget)

    doc.save(os.path.join(OUTPUT_DIR, "10_Implementation_Roadmap.docx"))
    print("Created: 10_Implementation_Roadmap.docx")


# ============================================================
# MAIN EXECUTION
# ============================================================
if __name__ == "__main__":
    print("Generating DOCX documents for SIH 26108 - StandardsAI\n")
    print(f"Output directory: {OUTPUT_DIR}\n")

    create_problem_statement()
    create_product_thinking()
    create_system_design()
    create_technical_architecture()
    create_security()
    create_scalability()
    create_engineering_decisions()
    create_communication()
    create_pitching()
    create_implementation_roadmap()

    print("\n" + "="*50)
    print("All documents created successfully!")
    print("="*50)
