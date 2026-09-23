# Quick Start Guide

Get StandardsAI running on your local machine in 5 minutes.

---

## Prerequisites

- **Python 3.10+** (check with `python --version`)
- **pip** (Python package manager)
- **Git** (optional, for cloning)

---

## Step 1: Get the Code

```bash
# Option A: Clone from repository
git clone <repo-url>
cd SIH

# Option B: Download ZIP and extract
# Then navigate to the SIH folder
```

---

## Step 2: Install Dependencies

### Backend Dependencies

```bash
cd backend
pip install fastapi uvicorn pydantic PyMuPDF
```

### Frontend Dependencies

```bash
cd ../frontend
pip install streamlit requests
```

### All at Once (Copy-Paste)

```bash
pip install fastapi uvicorn pydantic PyMuPDF streamlit requests
```

---

## Step 3: Start the Servers

### Option A: One-Click Launcher

```bash
# From the SIH root directory
python run_demo.py
```

This will:
1. Start the backend on port 8000
2. Start the frontend on port 8501
3. Open your browser automatically

### Option B: Manual Start (Recommended for Development)

**Terminal 1 - Backend:**
```bash
cd backend
python -m uvicorn app.main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
streamlit run app.py --server.port 8501
```

---

## Step 4: Open the Application

| Service | URL |
|---------|-----|
| **Frontend (UI)** | http://localhost:8501 |
| **Backend (API)** | http://localhost:8000 |
| **API Documentation** | http://localhost:8000/docs |

---

## Step 5: Try It Out

### Demo 1: Semantic Search

1. Go to the **Search** tab
2. Type: `cement for road construction`
3. Click **Search**
4. See: IS 269, IS 455, IS 1489 with relevance scores

### Demo 2: Tender Audit

1. Go to the **Tender Audit** tab
2. The sample text is pre-loaded with errors
3. Click **Audit Document**
4. See: Withdrawn standards, missing dependencies, warnings

### Demo 3: Dependency Graph

1. Go to the **Dependency Graph** tab
2. Select: `IS 269:2015 - Ordinary Portland Cement`
3. Click **Show Dependencies**
4. See: Visual tree of normative references

---

## Troubleshooting

### "Module not found" Error

```bash
# Install the missing module
pip install <module-name>
```

### "Port already in use" Error

```bash
# Find and kill the process using the port
# Windows:
netstat -ano | findstr :8000
taskkill /F /PID <PID>

# Linux/Mac:
lsof -i :8000
kill -9 <PID>
```

### "Cannot connect to API"

Make sure the backend is running on port 8000:
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{"status":"healthy","standards_loaded":15,"relationships_loaded":8}
```

### Standards not loading

Check the data path in `backend/app/main.py`:
```python
DATA_PATH = Path(__file__).parent.parent.parent / "data" / "sample_standards.json"
```

Make sure `data/sample_standards.json` exists.

---

## What's Next?

- [FEATURES.md](FEATURES.md) - Learn about all features
- [ARCHITECTURE.md](ARCHITECTURE.md) - Understand the system design
- [API.md](API.md) - Explore the API endpoints
- [DEMO_SCRIPT.md](DEMO_SCRIPT.md) - Prepare for video presentation

---

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure ports 8000 and 8501 are available
