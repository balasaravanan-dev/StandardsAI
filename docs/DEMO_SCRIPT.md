# Video Demo Script

Step-by-step script for recording the StandardsAI demonstration video.

---

## Overview

| Section | Duration | Content |
|---------|----------|---------|
| 1. Introduction | 30 sec | Problem statement |
| 2. Feature 1: Search | 60 sec | Semantic search demo |
| 3. Feature 2: Audit | 90 sec | Tender audit (killer feature) |
| 4. Feature 3: Graph | 60 sec | Dependency visualization |
| 5. Technical | 60 sec | Architecture overview |
| 6. Closing | 30 sec | Impact and summary |
| **Total** | **~5 min** | |

---

## Pre-Recording Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 8501
- [ ] Browser open to http://localhost:8501
- [ ] Screen recording software ready
- [ ] Microphone tested
- [ ] Script printed/visible

---

## Script

### 1. Introduction (30 seconds)

**[Show: Title slide or home page]**

> "Government procurement in India is worth over 20 lakh crore rupees annually. Every tender must reference the correct Indian Standards. But with 22,000 BIS standards and complex interdependencies, procurement officers spend hours researching standards for each tender.
>
> Today, we present StandardsAI - an AI-powered recommendation engine that finds the right standards in seconds, not hours."

---

### 2. Feature 1: Semantic Search (60 seconds)

**[Show: Search tab]**

> "Let's start with semantic search. I'll type a simple product description."

**[Type: "cement for road construction in coastal area"]**

**[Click: Search button]**

> "Within milliseconds, the system finds the relevant standards. Notice:
>
> - IS 269:2015 - Ordinary Portland Cement - with a 95% relevance score
> - The system detected the 'coastal' context automatically
> - It flagged that BIS Mark certification is MANDATORY
> - And it shows the latest amendment from 2019
>
> This isn't keyword matching. The system UNDERSTANDS that 'coastal' means we need corrosion-resistant standards."

**[Scroll to show allied standards]**

> "It also shows allied standards - these are the dependencies that the primary standard requires. You get the complete package, not just one standard."

---

### 3. Feature 2: Tender Audit - THE KILLER FEATURE (90 seconds)

**[Show: Tender Audit tab]**

> "Now the killer feature - Tender Audit. This is what sets us apart from every other solution."

**[Show the pre-loaded sample tender text]**

> "This is a sample tender document. It references several Indian Standards. Let's see if there are any compliance issues."

**[Click: Audit Document button]**

**[Wait for results]**

> "Look at this! The system found:"

**[Point to each section as you mention it]**

> "TWO CRITICAL ERRORS:
> - IS 456:1978 is WITHDRAWN. It was superseded by IS 456:2000 back in the year 2000. But someone is still referencing the old version!
> - IS 4825:1968 is also WITHDRAWN. Superseded by IS 4825:2020.
>
> If this tender was published, it would reference outdated standards - leading to procurement disputes, quality failures, and potentially legal issues."

**[Point to warnings]**

> "It also found WARNINGS:
> - The latest amendment to IS 269 from 2019 isn't referenced
> - BIS Mark certification is mandatory for cement, but it's not mentioned in the tender
>
> This audit would take a human expert 2-4 hours of manual research. Our system does it in under 3 seconds."

**[Pause for emphasis]**

> "This is like a COMPILER for tender documents - it catches errors BEFORE they become expensive procurement disputes."

---

### 4. Feature 3: Dependency Graph (60 seconds)

**[Show: Dependency Graph tab]**

> "Standards don't exist in isolation. They have dependencies - like software packages."

**[Select: IS 269:2015 from dropdown]**

**[Click: Show Dependencies]**

> "Here's the dependency tree for OPC Cement standard. It references:
> - IS 4031 series for testing methods
> - IS 4032 for chemical analysis  
> - IS 650 for standard sand
>
> This is like npm or pip for standards. We RESOLVE the full dependency tree so you know exactly what's needed."

**[Point to certification]**

> "And notice - it automatically flags that BIS Mark certification is mandatory. No manual lookup required."

---

### 5. Technical Architecture (60 seconds)

**[Show: About tab or architecture diagram]**

> "How does this work? The key insight: This is a GRAPH problem, not a text problem.
>
> Most AI solutions use an LLM for everything. We use a KNOWLEDGE GRAPH as the core engine:
> - Dependency resolution is GRAPH TRAVERSAL - no AI needed
> - Version checking is DATABASE LOOKUP - no AI needed
> - Certification checking is a RULE ENGINE - no AI needed
>
> AI is only used where it adds value: understanding messy input and generating explanations.
>
> This means:
> - ZERO hallucinations - every output is validated against the database
> - Traceable paths - you can see WHY each standard was recommended
> - 100% data sovereignty - everything runs on-premise, zero data leaves India"

---

### 6. Closing (30 seconds)

**[Show: Title slide or summary]**

> "StandardsAI transforms a 2-4 hour manual research process into a 3-second automated check.
>
> We're not building a chatbot that guesses standards. We built a Standards Dependency Resolver - a knowledge graph of 22,000+ Indian Standards that resolves dependencies, detects outdated versions, and audits tender documents.
>
> The AI understands your input. The graph gives you the correct answer. That's why this solution wins.
>
> Thank you."

---

## Demo Scenarios Summary

### Scenario 1: Search
- **Input:** "cement for road construction in coastal area"
- **Highlight:** Context detection, certification flagging

### Scenario 2: Audit
- **Input:** Pre-loaded tender with IS 456:1978, IS 4825:1968
- **Highlight:** WITHDRAWN detection, missing dependencies

### Scenario 3: Graph
- **Input:** IS 269:2015
- **Highlight:** Dependency tree, certification requirements

---

## Troubleshooting During Demo

### API Not Responding
- Check if backend is running: `curl http://localhost:8000/health`
- Restart: `python -m uvicorn app.main:app --reload --port 8000`

### No Results
- Verify data is loaded (health endpoint should show 15 standards)
- Check DATA_PATH in main.py

### Frontend Not Loading
- Check if Streamlit is running on port 8501
- Restart: `streamlit run app.py --server.port 8501`

---

## Key Phrases to Remember

| Topic | Key Phrase |
|-------|-----------|
| Problem | "22,000 standards, 2-4 hours per tender" |
| Solution | "3 seconds, not hours" |
| Audit | "Like a compiler for tender documents" |
| Graph | "Like npm/pip for standards" |
| AI | "AI understands input, graph gives answer" |
| Data | "Zero data leaves India" |

---

## Backup Plan

If live demo fails, show:
1. API documentation at `/docs`
2. Pre-recorded GIF/video
3. Screenshots in presentation
4. Explain architecture without live demo

---

## Post-Recording Checklist

- [ ] Review recording for audio quality
- [ ] Trim unnecessary pauses
- [ ] Add captions if required
- [ ] Export in required format
- [ ] Test playback on presentation device
