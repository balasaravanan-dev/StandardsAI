# StandardsAI

**AI-Powered Recommendation Engine for Identifying Applicable Indian Standards**

```
   _____ _                  _               _        _    ___ 
  / ____| |                | |             | |      / \  |_ _|
 | (___ | |_ __ _ _ __   __| | __ _ _ __ __| |___  / _ \  | | 
  \___ \| __/ _` | '_ \ / _` |/ _` | '__/ _` / __|/ ___ \ | | 
  ____) | || (_| | | | | (_| | (_| | | | (_| \__ \ /   \ \| |_
 |_____/ \__\__,_|_| |_|\__,_|\__,_|_|  \__,_|___/_/   \_\___|
```

**SIH 2026 | Problem ID: 26108 | Ministry of Consumer Affairs (DoCA)**

---

## The Problem

Government procurement officials must reference correct Indian Standards (IS) in tender specifications. With **22,000+ BIS standards** and complex interdependencies:

- Officers spend **2-4 hours** researching standards for each tender
- Wrong or outdated standards lead to **procurement disputes**
- Missing allied standards cause **quality failures**
- No existing tool provides intelligent recommendations

## Our Solution

StandardsAI is a **knowledge graph-powered recommendation engine** that:

| Feature | Description |
|---------|-------------|
| **Semantic Search** | Understands context, not just keywords |
| **Dependency Resolution** | Like npm/pip - resolves full standards package |
| **Tender Audit** | Upload document, get compliance report |
| **Certification Flagging** | Auto-detects mandatory BIS mark requirements |

### The Core Insight

> "This is a GRAPH problem, not a text problem. The knowledge graph is the engine; AI is just garnish for understanding input and generating explanations."

---

## Quick Start

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd SIH

# Install backend dependencies
cd backend
pip install fastapi uvicorn pydantic PyMuPDF

# Install frontend dependencies
cd ../frontend
pip install streamlit requests
```

### Run the Demo

**Option 1: One-Click Launcher**
```bash
python run_demo.py
```

**Option 2: Manual Start**

Terminal 1 - Backend:
```bash
cd backend
python -m uvicorn app.main:app --reload --port 8000
```

Terminal 2 - Frontend:
```bash
cd frontend
streamlit run app.py --server.port 8501
```

Then open: **http://localhost:8501**

---

## Features

### 1. Semantic Search

Find standards by describing your product:

```
Input: "Cement for road construction in coastal area"

Output:
- IS 269:2015 (OPC Cement) - 95% match
- IS 455:2015 (PSC Cement) - Good for coastal/marine
- IS 1489-1:2015 (PPC Cement) - Eco-friendly alternative
- BIS Mark certification MANDATORY
```

### 2. Tender Audit (The Killer Feature)

Upload a tender document and get instant compliance report:

```
AUDIT RESULTS
---------------------------------------------
ERRORS:
  IS 456:1978 - WITHDRAWN (Use IS 456:2000)
  IS 4825:1968 - WITHDRAWN (Use IS 4825:2020)
  Missing: IS 4031 (required by IS 269)

WARNINGS:
  Amendment Amd 1 (2019) not referenced
  BIS Mark certification not mentioned

VALID:
  IS 269:2015 - Current, valid
---------------------------------------------
3 Errors, 2 Warnings found
```

### 3. Dependency Graph

Visualize how standards are interconnected:

```
IS 269:2015 (OPC Cement)
├── IS 4031 series (Testing methods)
├── IS 4032 (Chemical analysis)
├── IS 650 (Sand for testing)
└── [Certification: BIS Mark MANDATORY]
```

### 4. Certification Flagging

Automatic detection of mandatory certifications:

- ISI Mark (BIS Product Certification)
- CRS (Compulsory Registration Scheme)
- Hallmarking

---

## Project Structure

```
SIH/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI server
│   │   └── services/
│   │       ├── search.py        # Hybrid BM25 + semantic search
│   │       ├── graph.py         # Dependency resolution algorithm
│   │       └── audit.py         # Tender audit logic
│   └── requirements.txt
├── frontend/
│   └── app.py                   # Streamlit UI
├── data/
│   └── sample_standards.json    # Standards database
├── docs/
│   ├── QUICKSTART.md           # Getting started guide
│   ├── FEATURES.md             # Feature documentation
│   ├── ARCHITECTURE.md         # System architecture
│   ├── API.md                  # API reference
│   └── DEMO_SCRIPT.md          # Video demo script
├── presentation/
│   ├── PPT_CONTENT.md          # Presentation slides
│   └── PITCH_SCRIPT.md         # Pitch script
├── run_demo.py                  # One-click launcher
└── README.md
```

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/recommend` | POST | Search for standards |
| `/api/v1/audit/text` | POST | Audit tender text |
| `/api/v1/audit/pdf` | POST | Audit PDF document |
| `/api/v1/graph/{id}` | GET | Get dependency graph |
| `/api/v1/standards` | GET | List all standards |
| `/api/v1/standards/{id}` | GET | Get standard details |

### Example: Search

```bash
curl -X POST http://localhost:8000/api/v1/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "cement for construction"}'
```

### Example: Audit

```bash
curl -X POST http://localhost:8000/api/v1/audit/text \
  -H "Content-Type: application/json" \
  -d '{"text": "The cement shall conform to IS 456:1978"}'
```

---

## Technology Stack

| Layer | Demo | Production |
|-------|------|------------|
| Frontend | Streamlit | Next.js |
| Backend | FastAPI | FastAPI |
| Database | JSON + In-memory | PostgreSQL + pgvector |
| Search | BM25 + Keyword | Hybrid BM25 + Vector |
| Graph | NetworkX | Apache AGE (PostgreSQL) |
| LLM | Groq API | Self-hosted Llama 3.1 |

### Why This Stack?

- **100% Data Sovereignty** - Zero data leaves India
- **Government Approved** - PostgreSQL is NIC-approved
- **Single Database** - One audit, one backup, one approval

---

## Documentation

| Document | Description |
|----------|-------------|
| [QUICKSTART.md](docs/QUICKSTART.md) | Step-by-step setup guide |
| [FEATURES.md](docs/FEATURES.md) | Complete feature documentation |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | System design and algorithms |
| [API.md](docs/API.md) | API reference |
| [DEMO_SCRIPT.md](docs/DEMO_SCRIPT.md) | Video presentation script |

---

## Why This Wins

| Dimension | Others | StandardsAI |
|-----------|--------|-------------|
| Architecture | LLM wrapper | Knowledge Graph engine |
| Accuracy | Hallucinations | Zero - closed-set grounding |
| Audit | None | Upload PDF, get report |
| Data | External APIs | 100% on-premise |
| Integration | "We'll integrate" | Browser extension ready |

---

## Team

[Your Team Name] - [Your Institution]

---

## License

MIT License

---

**SIH 2026 | Problem ID: 26108 | Ministry of Consumer Affairs**
