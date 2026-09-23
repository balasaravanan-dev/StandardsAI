# Features Documentation

Complete guide to all StandardsAI features.

---

## Table of Contents

1. [Semantic Search](#1-semantic-search)
2. [Tender Audit](#2-tender-audit)
3. [Dependency Resolution](#3-dependency-resolution)
4. [Certification Flagging](#4-certification-flagging)
5. [Context Detection](#5-context-detection)

---

## 1. Semantic Search

### What It Does

Finds relevant Indian Standards based on natural language product descriptions. Unlike keyword search, it understands context and meaning.

### How to Use

**Via UI:**
1. Go to the **Search** tab
2. Enter a product description (e.g., "steel pipes for water supply")
3. Click **Search**

**Via API:**
```bash
curl -X POST http://localhost:8000/api/v1/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "cement for coastal road construction"}'
```

### What It Returns

| Field | Description |
|-------|-------------|
| `primary_standards` | Top matching standards with scores |
| `allied_standards` | Related standards (dependencies) |
| `certifications` | Mandatory certification requirements |
| `context_detected` | Detected context factors |

### Example

**Input:**
```
"Stainless steel kitchen utensils for government canteen"
```

**Output:**
```
Primary Standards:
- IS 9235:2020 - Stainless Steel Utensils (95%)
  - BIS Mark MANDATORY
  - Amendment: Amd 1 (2022)

Allied Standards:
- IS 6911:2017 - SS Plate/Sheet
- IS 6603:2001 - Chemical Composition
- IS 6912:2003 - Terminology

Context Detected:
- food: true
- construction: false
```

### Algorithm

The search uses **Hybrid BM25 + Semantic** approach:

1. **BM25 Search** - Keyword matching on title, scope, keywords
2. **Semantic Search** - Jaccard similarity + keyword boost
3. **RRF Fusion** - Reciprocal Rank Fusion combines results
4. **Context Boost** - Boost standards matching detected context

---

## 2. Tender Audit

### What It Does

Analyzes tender documents and identifies compliance issues:

- **Withdrawn Standards** - Standards that have been superseded
- **Missing Dependencies** - Required standards not referenced
- **Missing Amendments** - Latest amendments not mentioned
- **Certification Gaps** - Mandatory certifications not specified

### How to Use

**Via UI:**
1. Go to the **Tender Audit** tab
2. Paste tender text or upload PDF
3. Click **Audit Document**

**Via API (Text):**
```bash
curl -X POST http://localhost:8000/api/v1/audit/text \
  -H "Content-Type: application/json" \
  -d '{"text": "The cement shall conform to IS 456:1978"}'
```

**Via API (PDF):**
```bash
curl -X POST http://localhost:8000/api/v1/audit/pdf \
  -F "file=@tender.pdf"
```

### What It Returns

| Field | Description |
|-------|-------------|
| `total_references` | Total IS references found |
| `valid_count` | Valid standards |
| `error_count` | Critical issues |
| `warning_count` | Non-critical issues |
| `errors` | List of errors with suggestions |
| `warnings` | List of warnings with suggestions |
| `valid_standards` | Standards that passed validation |

### Example

**Input (Tender Text):**
```
TENDER DOCUMENT
1. Cement shall conform to IS 269:2015
2. Testing as per IS 456:1978
3. Quality per IS 4825:1968
```

**Output:**
```
ERRORS (3):
- IS 456:1978 - WITHDRAWN in 2000
  Suggestion: Use IS 456:2000 instead

- IS 4825:1968 - WITHDRAWN in 2020
  Suggestion: Use IS 4825:2020 instead

- IS 269:2015 requires IS 4031 - NOT FOUND in tender
  Suggestion: Add reference to IS 4031 series

WARNINGS (2):
- IS 269:2015 Amendment Amd 1 (2019) not referenced
- BIS Mark certification not mentioned (mandatory for cement)

VALID (1):
- IS 269:2015 - Ordinary Portland Cement
```

### Withdrawn Standards Database

The system knows about these withdrawn standards:

| Withdrawn | Superseded By | Year |
|-----------|---------------|------|
| IS 456:1978 | IS 456:2000 | 2000 |
| IS 269:1989 | IS 269:2015 | 2015 |
| IS 4825:1968 | IS 4825:2020 | 2020 |
| IS 1239:1990 | IS 1239-1:2004 | 2004 |
| IS 10500:1991 | IS 10500:2012 | 2012 |

---

## 3. Dependency Resolution

### What It Does

Resolves the full dependency tree of a standard, similar to how npm or pip resolves package dependencies.

### How to Use

**Via UI:**
1. Go to the **Dependency Graph** tab
2. Select a standard from dropdown
3. Set depth (1-4)
4. Click **Show Dependencies**

**Via API:**
```bash
curl http://localhost:8000/api/v1/graph/IS%20269:2015?depth=2
```

### What It Returns

| Field | Description |
|-------|-------------|
| `root` | The starting standard |
| `root_details` | Full details of root standard |
| `tree` | Nested tree structure |
| `flat_list` | All dependencies (flat) |
| `total_dependencies` | Count of dependencies |
| `certifications` | Certification requirements |

### Example

**Input:** `IS 269:2015` (OPC Cement)

**Output:**
```
Root: IS 269:2015
Total Dependencies: 3

Dependency Tree:
IS 269:2015 (Ordinary Portland Cement)
├── IS 4031 series (Testing methods)
├── IS 4032 (Chemical analysis)
└── IS 650 (Standard sand for testing)

Flat List:
["IS 269:2015", "IS 4031 series", "IS 4032", "IS 650"]

Certifications:
- BIS ISI Mark (Mandatory)
```

### Algorithm

Uses **Breadth-First Search (BFS)** traversal:

1. Start with the requested standard
2. Add to queue with depth 0
3. For each standard in queue:
   - Get its normative references
   - Add unvisited references to queue
   - Track depth for each standard
4. Build tree structure for visualization
5. Return flat list + tree

---

## 4. Certification Flagging

### What It Does

Automatically identifies mandatory certification requirements for standards:

- **ISI Mark** (BIS Product Certification)
- **CRS** (Compulsory Registration Scheme)
- **Hallmarking**

### How It Works

When you search for or view a standard, the system:

1. Checks if the standard is in the certification database
2. Returns applicable certifications with details
3. Flags mandatory vs optional certifications

### Certification Database

| Type | Name | Products |
|------|------|----------|
| BIS_PRODUCT_CERTIFICATION | ISI Mark | Cement, Steel, Electrical, Fire Safety |
| CRS | Compulsory Registration | Electronics, IT Equipment |
| HALLMARKING | BIS Hallmarking | Gold Jewelry |

### Example

**Standard:** IS 269:2015 (OPC Cement)

**Certification Output:**
```json
{
  "type": "BIS_PRODUCT_CERTIFICATION",
  "name": "ISI Mark",
  "mandatory": true,
  "description": "Product requires BIS ISI Mark certification"
}
```

---

## 5. Context Detection

### What It Does

Automatically detects context factors from the query and boosts relevant standards.

### Detected Contexts

| Context | Trigger Words | Effect |
|---------|---------------|--------|
| `coastal` | coastal, marine, sea, beach | Boosts corrosion-resistant standards |
| `drinking_water` | drinking, potable, water supply | Boosts water quality standards |
| `industrial` | industrial, factory, plant | Boosts industrial standards |
| `construction` | construction, building, road | Boosts construction standards |
| `food` | food, kitchen, canteen, eating | Boosts food-grade standards |

### Example

**Query:** "Steel pipes for coastal drinking water supply"

**Context Detected:**
```json
{
  "coastal": true,
  "drinking_water": true,
  "industrial": false,
  "construction": false,
  "food": false
}
```

**Effect:**
- Standards mentioning "marine" or "corrosion" get +10% boost
- Standards mentioning "potable" get +10% boost

---

## Feature Comparison

| Feature | Basic RAG | StandardsAI |
|---------|-----------|-------------|
| Search | Vector only | Hybrid BM25 + Vector |
| Dependencies | None | Full tree resolution |
| Audit | None | Comprehensive validation |
| Certifications | None | Automatic flagging |
| Withdrawn | None | Database + detection |
| Context | None | Auto-detection + boost |

---

## Next Steps

- [ARCHITECTURE.md](ARCHITECTURE.md) - How these features are implemented
- [API.md](API.md) - API reference for all endpoints
- [DEMO_SCRIPT.md](DEMO_SCRIPT.md) - How to demonstrate these features
