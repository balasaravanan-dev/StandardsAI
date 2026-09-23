# API Reference

Complete API documentation for StandardsAI.

**Base URL:** `http://localhost:8000`

**API Documentation (Swagger):** `http://localhost:8000/docs`

---

## Table of Contents

1. [Health Check](#health-check)
2. [Recommend Standards](#recommend-standards)
3. [Audit Text](#audit-text)
4. [Audit PDF](#audit-pdf)
5. [Get Dependency Graph](#get-dependency-graph)
6. [List Standards](#list-standards)
7. [Get Standard Details](#get-standard-details)

---

## Health Check

Check if the API is running and data is loaded.

### Request

```
GET /health
```

### Response

```json
{
  "status": "healthy",
  "standards_loaded": 15,
  "relationships_loaded": 8
}
```

### Example

```bash
curl http://localhost:8000/health
```

---

## Recommend Standards

Search for relevant standards based on a product description.

### Request

```
POST /api/v1/recommend
Content-Type: application/json
```

### Request Body

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `query` | string | Yes | - | Product description |
| `language` | string | No | "en" | Language code |
| `include_allied` | boolean | No | true | Include allied standards |
| `include_certifications` | boolean | No | true | Include certifications |
| `max_results` | integer | No | 10 | Maximum results |

### Response

```json
{
  "query_understood": "cement for road construction",
  "context_detected": {
    "coastal": false,
    "drinking_water": false,
    "industrial": false,
    "construction": true,
    "food": false
  },
  "primary_standards": [
    {
      "is_number": "IS 269:2015",
      "title": "Ordinary Portland Cement - Specification",
      "scope": "Covers the chemical, physical and mechanical requirements...",
      "relevance_score": 95.5,
      "is_latest": true,
      "mandatory_certification": true,
      "amendments": "Amd 1 (2019)",
      "match_reasons": ["Keyword match (rank 1)", "Semantic match (rank 1)"]
    }
  ],
  "allied_standards": [
    {
      "is_number": "IS 455:2015",
      "title": "Portland Slag Cement - Specification",
      "scope": "Specifies requirements for Portland slag cement...",
      "relevance_score": 75.0,
      "match_reasons": ["Dependency of primary standard"]
    }
  ],
  "certifications": [
    {
      "type": "BIS_PRODUCT_CERTIFICATION",
      "name": "ISI Mark",
      "mandatory": true,
      "applicable_to": "IS 269:2015"
    }
  ],
  "total_found": 5
}
```

### Example

```bash
curl -X POST http://localhost:8000/api/v1/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "query": "cement for coastal road construction",
    "max_results": 5
  }'
```

---

## Audit Text

Audit tender text for standards compliance issues.

### Request

```
POST /api/v1/audit/text
Content-Type: application/json
```

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `text` | string | Yes | Tender document text |

### Response

```json
{
  "total_references": 4,
  "valid_count": 1,
  "error_count": 2,
  "warning_count": 3,
  "errors": [
    {
      "standard": "IS 456:1978",
      "message": "WITHDRAWN in 2000",
      "suggestion": "Use IS 456:2000 instead"
    },
    {
      "standard": "IS 269:2015",
      "message": "Requires IS 4031 series but not found in tender",
      "suggestion": "Add reference to IS 4031 series"
    }
  ],
  "warnings": [
    {
      "standard": "IS 269:2015",
      "message": "Amendment Amd 1 (2019) not referenced",
      "suggestion": "Consider referencing latest amendment"
    },
    {
      "standard": "IS 269:2015",
      "message": "Mandatory certification (BIS ISI Mark) not mentioned",
      "suggestion": "Add certification requirement clause"
    }
  ],
  "valid_standards": [
    {
      "is_number": "IS 269:2015",
      "title": "Ordinary Portland Cement - Specification"
    }
  ],
  "summary": "Found 2 errors and 3 warnings that need attention."
}
```

### Example

```bash
curl -X POST http://localhost:8000/api/v1/audit/text \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The cement shall conform to IS 269:2015. Testing as per IS 456:1978."
  }'
```

---

## Audit PDF

Audit a PDF tender document for standards compliance.

### Request

```
POST /api/v1/audit/pdf
Content-Type: multipart/form-data
```

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `file` | file | Yes | PDF file to audit |

### Response

Same as [Audit Text](#audit-text).

### Example

```bash
curl -X POST http://localhost:8000/api/v1/audit/pdf \
  -F "file=@tender_document.pdf"
```

### Notes

- Only PDF files are supported
- Requires PyMuPDF library installed
- Large PDFs may take longer to process

---

## Get Dependency Graph

Get the dependency tree for a specific standard.

### Request

```
GET /api/v1/graph/{standard_id}?depth={depth}
```

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `standard_id` | string | Yes | Standard number (URL encoded) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `depth` | integer | No | 2 | Traversal depth (1-4) |

### Response

```json
{
  "root": "IS 269:2015",
  "root_details": {
    "is_number": "IS 269:2015",
    "title": "Ordinary Portland Cement - Specification",
    "scope": "Covers the chemical, physical and mechanical requirements...",
    "department": "Civil Engineering",
    "category": "Cement",
    "year": 2015,
    "latest_amendment": "Amd 1 (2019)",
    "status": "current",
    "mandatory_certification": true,
    "normative_references": ["IS 4031 series", "IS 4032", "IS 650"],
    "keywords": ["OPC cement", "Portland cement", "construction"]
  },
  "total_dependencies": 3,
  "flat_list": ["IS 269:2015", "IS 4031 series", "IS 4032", "IS 650"],
  "tree": {
    "id": "IS 269:2015",
    "details": {...},
    "depth": 0,
    "children": [
      {
        "id": "IS 4031 series",
        "details": {...},
        "depth": 1,
        "children": []
      }
    ]
  },
  "missing": [],
  "allied": ["IS 455:2015", "IS 1489-1:2015"]
}
```

### Example

```bash
# Note: URL encode the standard ID
curl "http://localhost:8000/api/v1/graph/IS%20269:2015?depth=2"
```

---

## List Standards

Get a list of all standards in the database.

### Request

```
GET /api/v1/standards
```

### Response

```json
{
  "total": 15,
  "standards": [
    {
      "is_number": "IS 269:2015",
      "title": "Ordinary Portland Cement - Specification",
      "category": "Cement",
      "mandatory_certification": true
    },
    {
      "is_number": "IS 455:2015",
      "title": "Portland Slag Cement - Specification",
      "category": "Cement",
      "mandatory_certification": true
    }
  ]
}
```

### Example

```bash
curl http://localhost:8000/api/v1/standards
```

---

## Get Standard Details

Get full details of a specific standard.

### Request

```
GET /api/v1/standards/{is_number}
```

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `is_number` | string | Yes | Standard number (URL encoded) |

### Response

```json
{
  "is_number": "IS 269:2015",
  "title": "Ordinary Portland Cement - Specification",
  "scope": "Covers the chemical, physical and mechanical requirements of ordinary Portland cement (OPC)",
  "department": "Civil Engineering",
  "category": "Cement",
  "year": 2015,
  "latest_amendment": "Amd 1 (2019)",
  "status": "current",
  "mandatory_certification": true,
  "normative_references": ["IS 4031 series", "IS 4032", "IS 650"],
  "keywords": ["OPC cement", "Portland cement", "construction", "concrete", "road construction"]
}
```

### Example

```bash
curl "http://localhost:8000/api/v1/standards/IS%20269:2015"
```

### Error Response (404)

```json
{
  "detail": "Standard not found"
}
```

---

## Error Responses

All endpoints may return these error responses:

### 400 Bad Request

```json
{
  "detail": "Query cannot be empty"
}
```

### 404 Not Found

```json
{
  "detail": "Standard not found"
}
```

### 500 Internal Server Error

```json
{
  "detail": "Error processing request: <error message>"
}
```

---

## Response Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request - Invalid input |
| 404 | Not Found - Resource doesn't exist |
| 500 | Internal Server Error |

---

## Rate Limiting

Currently no rate limiting is implemented. For production:

- 100 requests/minute for search
- 10 requests/minute for PDF audit
- 1000 requests/minute for read operations

---

## Authentication

Currently no authentication is required. For production:

- API Key authentication
- OAuth 2.0 with government SSO
- Role-based access control

---

## SDK Examples

### Python

```python
import requests

BASE_URL = "http://localhost:8000"

# Search
response = requests.post(
    f"{BASE_URL}/api/v1/recommend",
    json={"query": "cement for construction"}
)
results = response.json()

# Audit
response = requests.post(
    f"{BASE_URL}/api/v1/audit/text",
    json={"text": "Cement as per IS 456:1978"}
)
audit = response.json()

# Graph
response = requests.get(
    f"{BASE_URL}/api/v1/graph/IS%20269:2015"
)
graph = response.json()
```

### JavaScript

```javascript
const BASE_URL = "http://localhost:8000";

// Search
const searchResponse = await fetch(`${BASE_URL}/api/v1/recommend`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ query: "cement for construction" })
});
const results = await searchResponse.json();

// Audit
const auditResponse = await fetch(`${BASE_URL}/api/v1/audit/text`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ text: "Cement as per IS 456:1978" })
});
const audit = await auditResponse.json();
```

---

## Next Steps

- [DEMO_SCRIPT.md](DEMO_SCRIPT.md) - How to demonstrate the API
- [ARCHITECTURE.md](ARCHITECTURE.md) - How the API works internally
