"""
StandardsAI - Streamlit Frontend
Demo UI for Video Presentation
SIH 2026 | Problem ID: 26108
"""

import streamlit as st
import streamlit.components.v1 as components
import requests
import json
from typing import Dict, List

# Configuration
API_URL = st.secrets.get("API_URL", "http://localhost:8000") if hasattr(st, 'secrets') else "http://localhost:8000"
DEMO_MODE = True  # Enable demo mode when backend is unavailable

# Demo data for when backend is not available
DEMO_STANDARDS = [
    {"is_number": "IS 269:2015", "title": "Ordinary Portland Cement - Specification", "category": "Cement", "mandatory_certification": True,
     "scope": "This standard covers the requirements for ordinary portland cement used for general concrete construction. It specifies physical and chemical requirements, packaging, marking, and sampling."},
    {"is_number": "IS 455:2015", "title": "Portland Slag Cement - Specification", "category": "Cement", "mandatory_certification": True,
     "scope": "This standard covers portland slag cement made by grinding together portland cement clinker, granulated blast furnace slag and gypsum. Ideal for marine and coastal environments."},
    {"is_number": "IS 1489-1:2015", "title": "Portland Pozzolana Cement (Fly Ash Based) - Specification", "category": "Cement", "mandatory_certification": True,
     "scope": "This standard covers fly ash based portland pozzolana cement manufactured by blending OPC clinker with fly ash. Good durability against sulfate attack."},
    {"is_number": "IS 456:2000", "title": "Plain and Reinforced Concrete - Code of Practice", "category": "Concrete", "mandatory_certification": False,
     "scope": "This code covers the general structural use of plain and reinforced concrete. It covers materials, design, and construction practices."},
    {"is_number": "IS 383:2016", "title": "Coarse and Fine Aggregate for Concrete - Specification", "category": "Aggregates", "mandatory_certification": False,
     "scope": "This standard covers the requirements for aggregates, crushed or uncrushed, derived from natural sources for use in concrete."},
    {"is_number": "IS 1786:2008", "title": "High Strength Deformed Steel Bars for Concrete Reinforcement", "category": "Steel", "mandatory_certification": True,
     "scope": "This standard covers the requirements for high strength deformed steel bars for use as reinforcement in concrete."},
    {"is_number": "IS 3025 (Part 17):1984", "title": "Methods of Sampling and Test for Water", "category": "Water", "mandatory_certification": False,
     "scope": "This standard covers methods for testing water used in concrete mixing and curing."},
    {"is_number": "IS 10500:2012", "title": "Drinking Water - Specification", "category": "Water", "mandatory_certification": False,
     "scope": "This standard prescribes the requirements and methods of sampling and test for drinking water."},
    {"is_number": "IS 16660:2017", "title": "LED Luminaires for General Lighting", "category": "Electrical", "mandatory_certification": True,
     "scope": "This standard covers the safety and performance requirements for LED luminaires for general lighting purposes."},
    {"is_number": "IS 15885:2018", "title": "Self-Ballasted LED Lamps for General Lighting", "category": "Electrical", "mandatory_certification": True,
     "scope": "This standard covers self-ballasted LED lamps for general lighting service with rated voltage up to 250V."},
    {"is_number": "IS 2190:2010", "title": "Selection, Installation and Maintenance of Portable Fire Extinguishers", "category": "Fire Safety", "mandatory_certification": True,
     "scope": "This standard covers requirements for selection, installation and maintenance of portable fire extinguishers."},
    {"is_number": "IS 15683:2018", "title": "Fire Extinguisher - ABC Dry Powder Type", "category": "Fire Safety", "mandatory_certification": True,
     "scope": "This standard covers the requirements for ABC dry powder type fire extinguishers."},
    {"is_number": "IS 1239-1:2004", "title": "Steel Tubes, Tubulars and Other Wrought Steel Fittings - Part 1: Steel Tubes", "category": "Steel Pipes", "mandatory_certification": False,
     "scope": "This standard covers requirements for seamless and welded steel tubes for water, gas, steam and air lines."},
    {"is_number": "IS 4736:1986", "title": "Hot Dipped Zinc Coated Mild Steel Tube", "category": "Steel Pipes", "mandatory_certification": False,
     "scope": "This standard covers hot dipped zinc coated mild steel tubes suitable for potable water supply and general engineering."},
]

DEMO_SEARCH_RESULTS = {
    "cement": {
        "query_understood": "Cement for road construction in coastal area",
        "context_detected": {"coastal_environment": True, "road_construction": True, "government_procurement": True},
        "primary_standards": [
            {"is_number": "IS 269:2015", "title": "Ordinary Portland Cement - Specification", "scope": "This standard covers ordinary portland cement for general construction. Specifies physical, chemical requirements and testing methods.", "relevance_score": 95, "mandatory_certification": True, "match_reasons": ["Exact match: cement", "Context: construction"], "amendments": "Amendment 1 (2019)"},
            {"is_number": "IS 455:2015", "title": "Portland Slag Cement - Specification", "scope": "Portland slag cement made with blast furnace slag. Excellent for marine and coastal environments due to sulfate resistance.", "relevance_score": 92, "mandatory_certification": True, "match_reasons": ["Match: cement", "Context: coastal - slag cement recommended"], "amendments": None},
            {"is_number": "IS 1489-1:2015", "title": "Portland Pozzolana Cement (Fly Ash Based)", "scope": "Fly ash based PPC. Good durability, lower heat of hydration. Suitable for mass concreting.", "relevance_score": 88, "mandatory_certification": True, "match_reasons": ["Match: cement", "Alternative for durability"], "amendments": None},
        ],
        "allied_standards": [
            {"is_number": "IS 456:2000", "title": "Code of Practice for Plain and Reinforced Concrete", "scope": "General structural design code for concrete", "relevance_score": 80, "match_reasons": ["Dependency: referenced by cement standards"]},
            {"is_number": "IS 383:2016", "title": "Aggregates for Concrete - Specification", "scope": "Requirements for coarse and fine aggregates", "relevance_score": 75, "match_reasons": ["Dependency: required for concrete work"]},
        ],
        "certifications": [
            {"type": "BIS", "name": "BIS Certification Mark (ISI Mark)", "mandatory": True, "applicable_to": "IS 269:2015"},
            {"type": "BIS", "name": "BIS Certification Mark (ISI Mark)", "mandatory": True, "applicable_to": "IS 455:2015"},
        ],
        "total_found": 5
    },
    "led": {
        "query_understood": "LED bulbs for government office",
        "context_detected": {"electrical": True, "government_procurement": True, "energy_efficiency": True},
        "primary_standards": [
            {"is_number": "IS 16660:2017", "title": "LED Luminaires for General Lighting", "scope": "Safety and performance requirements for LED luminaires for general lighting in offices and buildings.", "relevance_score": 96, "mandatory_certification": True, "match_reasons": ["Exact match: LED", "Context: office lighting"], "amendments": None},
            {"is_number": "IS 15885:2018", "title": "Self-Ballasted LED Lamps for General Lighting", "scope": "Requirements for self-ballasted LED lamps including safety, performance, and energy efficiency.", "relevance_score": 94, "mandatory_certification": True, "match_reasons": ["Match: LED bulbs", "Context: general lighting"], "amendments": "Amendment 1 (2020)"},
        ],
        "allied_standards": [
            {"is_number": "IS 10322-5-1:1994", "title": "Luminaires Part 5 Particular Requirements Section 1", "scope": "Safety requirements for luminaires", "relevance_score": 70, "match_reasons": ["Dependency: general luminaire safety"]},
        ],
        "certifications": [
            {"type": "BIS", "name": "BIS Certification Mark (ISI Mark)", "mandatory": True, "applicable_to": "IS 16660:2017"},
            {"type": "BEE", "name": "BEE Star Rating", "mandatory": True, "applicable_to": "IS 15885:2018"},
        ],
        "total_found": 3
    },
    "steel": {
        "query_understood": "Steel pipes for water supply",
        "context_detected": {"water_supply": True, "piping": True},
        "primary_standards": [
            {"is_number": "IS 1239-1:2004", "title": "Steel Tubes for Water, Gas and Steam", "scope": "Requirements for mild steel tubes suitable for screwing to BS 21 pipe threads. For water, gas, steam lines.", "relevance_score": 94, "mandatory_certification": False, "match_reasons": ["Exact match: steel pipes", "Context: water supply"], "amendments": None},
            {"is_number": "IS 4736:1986", "title": "Hot Dipped Zinc Coated Mild Steel Tube", "scope": "Zinc coated steel tubes for potable water supply. Corrosion resistant coating for longer life.", "relevance_score": 91, "mandatory_certification": False, "match_reasons": ["Match: steel pipes", "Context: water - galvanized recommended"], "amendments": "Reaffirmed 2017"},
        ],
        "allied_standards": [
            {"is_number": "IS 1387:1993", "title": "General Requirements for Supply of Metallic Materials", "scope": "General requirements for inspection, packaging and marking", "relevance_score": 65, "match_reasons": ["Dependency: metallic material supply"]},
        ],
        "certifications": [],
        "total_found": 3
    },
    "fire": {
        "query_understood": "Fire extinguisher for school",
        "context_detected": {"fire_safety": True, "public_building": True, "mandatory_compliance": True},
        "primary_standards": [
            {"is_number": "IS 15683:2018", "title": "ABC Dry Powder Type Fire Extinguisher", "scope": "Requirements for ABC type portable fire extinguishers using monoammonium phosphate as extinguishing agent.", "relevance_score": 97, "mandatory_certification": True, "match_reasons": ["Exact match: fire extinguisher", "Context: school - ABC type recommended"], "amendments": None},
            {"is_number": "IS 2190:2010", "title": "Selection, Installation and Maintenance of Fire Extinguishers", "scope": "Code of practice for selection, installation, inspection and maintenance of portable fire extinguishers.", "relevance_score": 92, "mandatory_certification": True, "match_reasons": ["Match: fire extinguisher", "Context: installation guidance"], "amendments": None},
        ],
        "allied_standards": [
            {"is_number": "IS 2189:2008", "title": "Selection, Installation and Maintenance of Automatic Fire Detection and Alarm System", "scope": "Requirements for fire detection systems", "relevance_score": 70, "match_reasons": ["Related: fire safety systems"]},
        ],
        "certifications": [
            {"type": "BIS", "name": "BIS Certification Mark (ISI Mark)", "mandatory": True, "applicable_to": "IS 15683:2018"},
        ],
        "total_found": 3
    }
}

DEMO_AUDIT_RESULT = {
    "total_references": 5,
    "valid_count": 2,
    "error_count": 2,
    "warning_count": 1,
    "errors": [
        {"standard": "IS 456:1978", "message": "WITHDRAWN - This standard has been superseded", "suggestion": "Replace with IS 456:2000 (Plain and Reinforced Concrete - Code of Practice)"},
        {"standard": "IS 4825:1968", "message": "WITHDRAWN - This standard has been superseded", "suggestion": "Replace with IS 4825:2020 (Masonry Cement - Specification)"},
    ],
    "warnings": [
        {"standard": "IS 269:2015", "message": "Amendment 1 (2019) not referenced", "suggestion": "Update reference to include latest amendment: IS 269:2015/Amd 1:2019"},
    ],
    "valid_standards": [
        {"is_number": "IS 383:2016", "title": "Coarse and Fine Aggregate for Concrete - Specification"},
        {"is_number": "IS 10500:2012", "title": "Drinking Water - Specification"},
    ],
    "summary": "Found 2 errors and 1 warning that need attention."
}

DEMO_GRAPH_RESULT = {
    "root": "IS 269:2015",
    "root_details": {"title": "Ordinary Portland Cement - Specification", "category": "Cement"},
    "total_dependencies": 5,
    "flat_list": ["IS 269:2015", "IS 4031-1:1996", "IS 4031-2:1999", "IS 4031-4:1988", "IS 4032:1985", "IS 650:1991"],
    "tree": {
        "id": "IS 269:2015",
        "details": {"title": "Ordinary Portland Cement - Specification"},
        "children": [
            {"id": "IS 4031-1:1996", "details": {"title": "Methods of Physical Tests for Hydraulic Cement - Part 1: Fineness"}, "children": []},
            {"id": "IS 4031-2:1999", "details": {"title": "Methods of Physical Tests - Part 2: Determination of Fineness by Blaine"}, "children": []},
            {"id": "IS 4031-4:1988", "details": {"title": "Methods of Physical Tests - Part 4: Consistency of Standard Cement Paste"}, "children": []},
            {"id": "IS 4032:1985", "details": {"title": "Method of Chemical Analysis of Hydraulic Cement"}, "children": []},
            {"id": "IS 650:1991", "details": {"title": "Standard Sand for Testing Cement - Specification"}, "children": []},
        ]
    },
    "certifications": [{"description": "BIS Certification Mark (ISI Mark) is MANDATORY for cement sold in India"}]
}

st.set_page_config(
    page_title="StandardsAI - Indian Standards Recommendation",
    page_icon="S",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Light Mode with Be Vietnam Pro font
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700&display=swap');

    * {
        font-family: 'Be Vietnam Pro', sans-serif !important;
    }

    .stApp {
        background-color: #FFFFFF;
    }

    .main-header {
        font-family: 'Be Vietnam Pro', sans-serif !important;
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a1a2e;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .sub-header {
        font-family: 'Be Vietnam Pro', sans-serif !important;
        font-size: 1.2rem;
        color: #4a4a68;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 400;
    }

    .error-box {
        background-color: #fff5f5;
        border-left: 4px solid #e53e3e;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0.25rem;
        color: #1a1a2e;
    }

    .warning-box {
        background-color: #fffbeb;
        border-left: 4px solid #d97706;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0.25rem;
        color: #1a1a2e;
    }

    .success-box {
        background-color: #f0fdf4;
        border-left: 4px solid #22c55e;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0.25rem;
        color: #1a1a2e;
    }

    .standard-card {
        background-color: #f8fafc;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        border: 1px solid #e2e8f0;
    }

    .cert-badge {
        background-color: #dc2626;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.8rem;
        font-weight: 600;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Be Vietnam Pro', sans-serif !important;
        color: #1a1a2e !important;
    }

    p, span, div, label {
        font-family: 'Be Vietnam Pro', sans-serif !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        font-family: 'Be Vietnam Pro', sans-serif !important;
        font-weight: 500;
    }

    .stButton > button {
        font-family: 'Be Vietnam Pro', sans-serif !important;
        font-weight: 500;
    }

    .stTextInput > div > div > input {
        font-family: 'Be Vietnam Pro', sans-serif !important;
    }

    .stTextArea > div > div > textarea {
        font-family: 'Be Vietnam Pro', sans-serif !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #f8fafc;
    }

    section[data-testid="stSidebar"] * {
        color: #1a1a2e !important;
    }

    /* Prevent scroll jump on search results */
    .search-results-anchor {
        scroll-margin-top: 0;
    }

    .stApp > header {
        position: sticky;
        top: 0;
    }
</style>
""", unsafe_allow_html=True)


def check_api_health() -> bool:
    """Check if the API is running."""
    try:
        response = requests.get(f"{API_URL}/health", timeout=2)
        return response.status_code == 200
    except:
        return False


def get_demo_search_result(query: str) -> Dict:
    """Get demo search result based on query keywords."""
    query_lower = query.lower()
    if "cement" in query_lower or "concrete" in query_lower or "road" in query_lower or "coastal" in query_lower:
        result = DEMO_SEARCH_RESULTS["cement"].copy()
        result["query_understood"] = query
        return result
    elif "led" in query_lower or "bulb" in query_lower or "light" in query_lower or "lamp" in query_lower:
        result = DEMO_SEARCH_RESULTS["led"].copy()
        result["query_understood"] = query
        return result
    elif "steel" in query_lower or "pipe" in query_lower or "tube" in query_lower or "water supply" in query_lower:
        result = DEMO_SEARCH_RESULTS["steel"].copy()
        result["query_understood"] = query
        return result
    elif "fire" in query_lower or "extinguisher" in query_lower or "safety" in query_lower:
        result = DEMO_SEARCH_RESULTS["fire"].copy()
        result["query_understood"] = query
        return result
    else:
        result = DEMO_SEARCH_RESULTS["cement"].copy()
        result["query_understood"] = query
        return result


def search_standards(query: str, use_demo: bool = False) -> Dict:
    """Search for standards."""
    if use_demo and DEMO_MODE:
        return get_demo_search_result(query)
    try:
        response = requests.post(
            f"{API_URL}/api/v1/recommend",
            json={"query": query, "max_results": 10},
            timeout=5
        )
        return response.json()
    except Exception as e:
        if DEMO_MODE:
            return get_demo_search_result(query)
        return {"error": str(e)}


def audit_text(text: str, use_demo: bool = False) -> Dict:
    """Audit tender text."""
    if use_demo and DEMO_MODE:
        return DEMO_AUDIT_RESULT
    try:
        response = requests.post(
            f"{API_URL}/api/v1/audit/text",
            json={"text": text},
            timeout=10
        )
        return response.json()
    except Exception as e:
        if DEMO_MODE:
            return DEMO_AUDIT_RESULT
        return {"error": str(e)}


def get_graph(standard_id: str, depth: int = 2, use_demo: bool = False) -> Dict:
    """Get dependency graph."""
    if use_demo and DEMO_MODE:
        return DEMO_GRAPH_RESULT
    try:
        response = requests.get(
            f"{API_URL}/api/v1/graph/{standard_id}",
            params={"depth": depth},
            timeout=5
        )
        return response.json()
    except Exception as e:
        if DEMO_MODE:
            return DEMO_GRAPH_RESULT
        return {"error": str(e)}


def get_all_standards(use_demo: bool = False) -> List:
    """Get list of all standards."""
    if use_demo and DEMO_MODE:
        return DEMO_STANDARDS
    try:
        response = requests.get(f"{API_URL}/api/v1/standards", timeout=5)
        data = response.json()
        return data.get("standards", [])
    except:
        if DEMO_MODE:
            return DEMO_STANDARDS
        return []


# ============ SIDEBAR ============
with st.sidebar:
    st.markdown("### StandardsAI")
    st.markdown("AI-Powered Recommendation Engine for Indian Standards")

    st.markdown("---")

    # API Status
    api_healthy = check_api_health()
    if api_healthy:
        st.success("API Connected")
        use_demo = False
    else:
        if DEMO_MODE:
            st.info("Demo Mode Active")
            st.caption("Using sample data for demonstration")
            use_demo = True
        else:
            st.error("API Not Connected")
            st.info("Start the backend:\n```\ncd backend\nuvicorn app.main:app --reload\n```")
            use_demo = False

    # Store in session state for use in other tabs
    st.session_state['use_demo'] = use_demo if 'use_demo' not in st.session_state or not api_healthy else st.session_state.get('use_demo', use_demo)

    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.85rem; color: #4a4a68; line-height: 2;">
    <div>&#9654; Search</div>
    <div>&#9679; Dependencies</div>
    <div>&#9733; Audit</div>
    <div>&#10003; Certification</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**SIH 2026** | Problem ID: 26108")
    st.markdown("Ministry of Consumer Affairs")


# ============ MAIN CONTENT ============
st.markdown('<p class="main-header">StandardsAI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Recommendation Engine for Indian Standards</p>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Search", "Tender Audit", "Dependency Graph", "About"])


# ============ TAB 1: SEARCH ============
with tab1:
    st.markdown("### Find Applicable Standards")
    st.markdown("Enter a product description to find relevant Indian Standards")

    col1, col2 = st.columns([4, 1])
    with col1:
        query = st.text_input(
            "Product Description",
            placeholder="e.g., Cement for road construction in coastal area",
            label_visibility="collapsed"
        )
    with col2:
        search_btn = st.button("Search", type="primary", use_container_width=True)

    # Quick examples
    st.markdown("**Quick Examples:**")
    example_cols = st.columns(4)
    examples = [
        "Steel pipes for water supply",
        "LED bulbs for government office",
        "Cement for coastal road construction",
        "Fire extinguisher for school"
    ]

    for i, example in enumerate(examples):
        if example_cols[i].button(example, key=f"ex_{i}"):
            query = example
            search_btn = True

    if search_btn and query:
        use_demo = st.session_state.get('use_demo', not check_api_health())
        with st.spinner("Searching..." if not use_demo else "Loading demo results..."):
            results = search_standards(query, use_demo=use_demo)

        if "error" in results:
            st.error(f"Error: {results['error']}")
        else:
            # Context detected
            context = results.get("context_detected", {})
            active_context = [k for k, v in context.items() if v]
            if active_context:
                st.info(f"**Context Detected:** {', '.join(active_context)}")

            # Primary Standards
            st.markdown("### Primary Standards")
            for std in results.get("primary_standards", []):
                with st.container():
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        st.markdown(f"**{std['is_number']}** - {std['title']}")
                        st.caption(std['scope'][:200] + "..." if len(std['scope']) > 200 else std['scope'])

                        if std.get('match_reasons'):
                            st.caption(f"Match: {', '.join(std['match_reasons'])}")

                    with col2:
                        st.metric("Score", f"{std['relevance_score']:.0f}%")
                        if std.get('mandatory_certification'):
                            st.markdown('<span class="cert-badge">BIS MARK REQUIRED</span>', unsafe_allow_html=True)

                    if std.get('amendments'):
                        st.warning(f"Latest Amendment: {std['amendments']}")

                    st.markdown("---")

            # Allied Standards
            if results.get("allied_standards"):
                st.markdown("### Allied Standards (Dependencies)")
                for std in results["allied_standards"]:
                    st.markdown(f"- **{std['is_number']}** - {std['title']}")

            # Certifications
            if results.get("certifications"):
                st.markdown("### Certification Requirements")
                for cert in results["certifications"]:
                    st.error(f"**{cert['name']}** required for {cert['applicable_to']}")

            # Keep view near top (prevent auto-scroll to bottom)
            components.html("""
                <script>
                    window.parent.document.querySelector('section.main').scrollTo({top: 0, behavior: 'instant'});
                </script>
            """, height=0)


# ============ TAB 2: TENDER AUDIT ============
with tab2:
    st.markdown("### Tender Document Audit")
    st.markdown("Paste tender text or upload a PDF to check for compliance issues")

    audit_method = st.radio(
        "Input Method",
        ["Paste Text", "Upload PDF"],
        horizontal=True
    )

    if audit_method == "Paste Text":
        # Sample tender with errors for demo
        sample_tender = """TENDER DOCUMENT
Government of India
Ministry of Road Transport & Highways

TECHNICAL SPECIFICATIONS FOR CEMENT SUPPLY

1. The cement shall conform to IS 269:2015 (Ordinary Portland Cement)
2. Testing shall be done as per IS 456:1978 (Code of Practice for Plain and Reinforced Concrete)
3. Aggregates shall conform to IS 383:2016
4. The contractor shall ensure quality as per IS 4825:1968
5. Water used for mixing shall be tested as per IS 10500:2012

Note: All materials must meet the specified Indian Standards.
"""

        tender_text = st.text_area(
            "Tender Text",
            value=sample_tender,
            height=300,
            help="Paste your tender document text here"
        )

        if st.button("Audit Document", type="primary"):
            use_demo = st.session_state.get('use_demo', not check_api_health())
            with st.spinner("Auditing..." if not use_demo else "Loading demo audit results..."):
                result = audit_text(tender_text, use_demo=use_demo)

            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                # Summary
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total References", result['total_references'])
                col2.metric("Valid", result['valid_count'], delta_color="normal")
                col3.metric("Errors", result['error_count'], delta=f"-{result['error_count']}" if result['error_count'] > 0 else None, delta_color="inverse")
                col4.metric("Warnings", result['warning_count'])

                st.markdown(f"**Summary:** {result['summary']}")

                # Errors
                if result['errors']:
                    st.markdown("### Errors (Must Fix)")
                    for err in result['errors']:
                        st.markdown(f"""
                        <div class="error-box">
                            <strong>{err['standard']}</strong> - {err['message']}<br>
                            <em>Suggestion: {err.get('suggestion', 'N/A')}</em>
                        </div>
                        """, unsafe_allow_html=True)

                # Warnings
                if result['warnings']:
                    st.markdown("### Warnings (Should Review)")
                    for warn in result['warnings']:
                        st.markdown(f"""
                        <div class="warning-box">
                            <strong>{warn['standard']}</strong> - {warn['message']}<br>
                            <em>Suggestion: {warn.get('suggestion', 'N/A')}</em>
                        </div>
                        """, unsafe_allow_html=True)

                # Valid
                if result['valid_standards']:
                    st.markdown("### Valid Standards")
                    for std in result['valid_standards']:
                        st.markdown(f"""
                        <div class="success-box">
                            <strong>{std['is_number']}</strong> - {std['title']}
                        </div>
                        """, unsafe_allow_html=True)

    else:  # Upload PDF
        st.markdown("""
        <div style="border: 2px dashed #cbd5e1; border-radius: 8px; padding: 2rem; text-align: center; background: #f8fafc; margin: 1rem 0;">
            <div style="font-size: 2rem; color: #94a3b8; margin-bottom: 0.5rem;">[PDF]</div>
            <div style="color: #64748b; font-size: 0.9rem;">Upload your tender document</div>
        </div>
        """, unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Choose PDF file", type=['pdf'], label_visibility="collapsed")
        if uploaded_file:
            st.markdown(f"""
            <div style="background: #f0fdf4; border: 1px solid #22c55e; border-radius: 6px; padding: 0.75rem; margin-top: 0.5rem;">
                <strong>File:</strong> {uploaded_file.name}
            </div>
            """, unsafe_allow_html=True)
            st.info("PDF processing requires PyMuPDF. For demo, please use 'Paste Text' option.")


# ============ TAB 3: DEPENDENCY GRAPH ============
with tab3:
    st.markdown("### Standards Dependency Graph")
    st.markdown("Visualize how standards are interconnected through normative references")

    # Get all standards for dropdown
    use_demo = st.session_state.get('use_demo', not check_api_health())
    all_standards = get_all_standards(use_demo=use_demo)

    if all_standards:
        standard_options = {f"{s['is_number']} - {s['title'][:50]}": s['is_number'] for s in all_standards}

        col1, col2 = st.columns([3, 1])
        with col1:
            selected = st.selectbox(
                "Select a Standard",
                options=list(standard_options.keys())
            )
        with col2:
            depth = st.slider("Depth", 1, 4, 2)

        if st.button("Show Dependencies", type="primary"):
            standard_id = standard_options[selected]

            with st.spinner("Loading graph..." if not use_demo else "Loading demo graph..."):
                result = get_graph(standard_id, depth, use_demo=use_demo)

            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                # Stats
                col1, col2, col3 = st.columns(3)
                col1.metric("Root Standard", result['root'])
                col2.metric("Total Dependencies", result['total_dependencies'])
                col3.metric("Depth Explored", depth)

                # Tree view
                st.markdown("### Dependency Tree")

                def render_tree(node, level=0):
                    """Render tree recursively."""
                    indent = "  " * level
                    prefix = "[ROOT]" if level == 0 else "|--" if level == 1 else "|  " * (level-1) + "|--"

                    details = node.get("details", {})
                    title = details.get("title", "Unknown")[:60]

                    st.markdown(f"`{prefix}` **{node['id']}** - {title}")

                    for child in node.get("children", []):
                        render_tree(child, level + 1)

                render_tree(result['tree'])

                # Flat list
                st.markdown("### All Dependencies (Flat List)")
                st.code(", ".join(result['flat_list']))

                # Certifications
                if result.get('certifications'):
                    st.markdown("### Certification Requirements")
                    for cert in result['certifications']:
                        st.warning(f"{cert['description']}")
    else:
        st.warning("No standards loaded. Make sure the API is running.")


# ============ TAB 4: ABOUT ============
with tab4:
    st.markdown("### About StandardsAI")

    st.markdown("""
    **StandardsAI** is an AI-powered recommendation engine that helps procurement officers
    identify the correct Indian Standards for tender specifications.

    #### The Problem
    - **22,000+** BIS standards exist across 400+ technical committees
    - Procurement officers spend **2-4 hours** researching standards for each tender
    - Wrong or outdated standards lead to **procurement disputes and litigation**
    - No existing tool provides intelligent recommendations

    #### Our Solution

    | Feature | Description |
    |---------|-------------|
    | **Semantic Search** | Understands context, not just keywords |
    | **Dependency Resolution** | Like npm/pip - resolves full standards package |
    | **Tender Audit** | Upload document, get compliance report |
    | **Certification Flagging** | Auto-detects mandatory BIS mark requirements |

    #### The Core Insight

    > "This is a GRAPH problem, not a text problem. The knowledge graph is the engine;
    > AI is just garnish for understanding input and generating explanations."

    #### Technology Stack

    - **Backend:** FastAPI (Python)
    - **Search:** Hybrid BM25 + Semantic
    - **Graph:** Dependency resolution algorithm
    - **Database:** PostgreSQL with pgvector (production)
    - **LLM:** Self-hosted Llama 3.1 (production)

    #### Data Sovereignty

    100% on-premise deployment. Zero data leaves India.

    ---

    **SIH 2026** | Problem ID: 26108 | Ministry of Consumer Affairs (DoCA)
    """)

    # Demo scenarios
    st.markdown("### Demo Scenarios")

    with st.expander("Scenario 1: Semantic Search"):
        st.markdown("""
        **Input:** "Cement for road construction in coastal area"

        **Expected Output:**
        - IS 269:2015 (OPC Cement) - Primary
        - IS 455:2015 (PSC Cement) - Good for coastal/marine
        - IS 1489-1:2015 (PPC Cement) - Alternative
        - BIS Mark certification MANDATORY
        """)

    with st.expander("Scenario 2: Tender Audit (Killer Feature)"):
        st.markdown("""
        **Input:** Sample tender document with errors

        **Expected Errors:**
        - IS 456:1978 - WITHDRAWN (superseded by IS 456:2000)
        - IS 4825:1968 - WITHDRAWN (superseded by IS 4825:2020)
        - BIS Mark certification not mentioned
        """)

    with st.expander("Scenario 3: Dependency Graph"):
        st.markdown("""
        **Input:** Select IS 269:2015 (OPC Cement)

        **Expected Output:**
        - Dependencies: IS 4031 series, IS 4032, IS 650
        - Visual tree showing relationships
        - Certification requirements
        """)


# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #4a4a68; font-family: Be Vietnam Pro, sans-serif;'>"
    "StandardsAI | SIH 2026 | Problem ID: 26108 | Ministry of Consumer Affairs"
    "</p>",
    unsafe_allow_html=True
)
