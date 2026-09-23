"""
Tender Audit Service - The Killer Feature
Extracts and validates all standard references in tender documents
"""

import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path
import json


@dataclass
class AuditError:
    """Represents an error found during audit."""
    severity: str  # "error" or "warning"
    standard: str
    message: str
    suggestion: Optional[str] = None


@dataclass
class AuditResult:
    """Complete audit result for a tender document."""
    total_references: int
    valid_count: int
    error_count: int
    warning_count: int
    errors: List[AuditError]
    warnings: List[AuditError]
    valid_standards: List[Dict]
    missing_certifications: List[str]
    missing_dependencies: Dict[str, List[str]]


class TenderAuditor:
    """Audits tender documents for standards compliance."""

    # Regex patterns for Indian Standards
    IS_PATTERNS = [
        r'IS\s*(\d+(?:-\d+)?)\s*:\s*(\d{4})',  # IS 269:2015
        r'IS\s*(\d+(?:-\d+)?)\s*\(\d{4}\)',     # IS 269 (2015)
        r'IS\s*(\d+(?:-\d+)?)',                  # IS 269 (year not specified)
        r'BIS\s*(\d+(?:-\d+)?)\s*:\s*(\d{4})',  # BIS 269:2015
    ]

    def __init__(self, standards_db: Dict, withdrawn_db: Optional[Dict] = None):
        """
        Initialize auditor with standards database.

        Args:
            standards_db: Full standards database
            withdrawn_db: Database of withdrawn/superseded standards
        """
        self.standards = {s["is_number"]: s for s in standards_db.get("standards", [])}
        self.certifications = standards_db.get("certifications", [])
        self.relationships = standards_db.get("relationships", [])

        # Load or create withdrawn standards mapping
        self.withdrawn = withdrawn_db or self._default_withdrawn()

    def _default_withdrawn(self) -> Dict:
        """Default withdrawn standards for demo."""
        return {
            "IS 456:1978": {
                "status": "withdrawn",
                "superseded_by": "IS 456:2000",
                "year_withdrawn": 2000
            },
            "IS 269:1989": {
                "status": "withdrawn",
                "superseded_by": "IS 269:2015",
                "year_withdrawn": 2015
            },
            "IS 4825:1968": {
                "status": "withdrawn",
                "superseded_by": "IS 4825:2020",
                "year_withdrawn": 2020
            },
            "IS 1239:1990": {
                "status": "withdrawn",
                "superseded_by": "IS 1239-1:2004",
                "year_withdrawn": 2004
            },
            "IS 10500:1991": {
                "status": "withdrawn",
                "superseded_by": "IS 10500:2012",
                "year_withdrawn": 2012
            }
        }

    def extract_standards(self, text: str) -> List[Tuple[str, Optional[str]]]:
        """
        Extract all standard references from text.

        Returns:
            List of (standard_number, year) tuples
        """
        found = []

        for pattern in self.IS_PATTERNS:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    std_num = f"IS {match[0]}"
                    year = match[1] if len(match) > 1 else None
                else:
                    std_num = f"IS {match}"
                    year = None
                found.append((std_num, year))

        # Deduplicate while preserving order
        seen = set()
        unique = []
        for item in found:
            key = f"{item[0]}:{item[1]}" if item[1] else item[0]
            if key not in seen:
                seen.add(key)
                unique.append(item)

        return unique

    def audit(self, text: str) -> AuditResult:
        """
        Full audit of tender document text.

        Algorithm:
        1. Extract all IS references
        2. For each reference:
           - Check if exists in database
           - Check if withdrawn/superseded
           - Check for latest amendments
        3. Check dependency completeness
        4. Check certification requirements
        """
        extracted = self.extract_standards(text)

        errors = []
        warnings = []
        valid_standards = []

        # Track referenced standards for completeness check
        referenced_ids = []

        for std_num, year in extracted:
            full_id = f"{std_num}:{year}" if year else std_num

            # Check if withdrawn
            if full_id in self.withdrawn:
                withdrawn_info = self.withdrawn[full_id]
                errors.append(AuditError(
                    severity="error",
                    standard=full_id,
                    message=f"WITHDRAWN in {withdrawn_info['year_withdrawn']}",
                    suggestion=f"Use {withdrawn_info['superseded_by']} instead"
                ))
                continue

            # Find in current database
            matched = self._find_standard(std_num, year)

            if not matched:
                # Not in database - might be valid but we can't verify
                warnings.append(AuditError(
                    severity="warning",
                    standard=full_id,
                    message="Not found in database - cannot verify",
                    suggestion="Verify manually on BIS website"
                ))
                continue

            # Check for amendments
            if matched.get("latest_amendment"):
                if not self._amendment_referenced(text, matched):
                    warnings.append(AuditError(
                        severity="warning",
                        standard=matched["is_number"],
                        message=f"Amendment {matched['latest_amendment']} not referenced",
                        suggestion="Consider referencing latest amendment"
                    ))

            # Valid standard found
            valid_standards.append(matched)
            referenced_ids.append(matched["is_number"])

        # Check dependency completeness
        missing_deps = self._check_dependencies(referenced_ids)
        for parent, missing in missing_deps.items():
            for dep in missing:
                errors.append(AuditError(
                    severity="error",
                    standard=parent,
                    message=f"Requires {dep} but not found in tender",
                    suggestion=f"Add reference to {dep}"
                ))

        # Check certifications
        missing_certs = self._check_certifications(referenced_ids, text)
        for cert in missing_certs:
            warnings.append(AuditError(
                severity="warning",
                standard=cert["standard"],
                message=f"Mandatory certification ({cert['type']}) not mentioned",
                suggestion="Add certification requirement clause"
            ))

        return AuditResult(
            total_references=len(extracted),
            valid_count=len(valid_standards),
            error_count=len([e for e in errors if e.severity == "error"]),
            warning_count=len(warnings),
            errors=[e for e in errors if e.severity == "error"],
            warnings=warnings,
            valid_standards=valid_standards,
            missing_certifications=[c["type"] for c in missing_certs],
            missing_dependencies=missing_deps
        )

    def _find_standard(self, std_num: str, year: Optional[str]) -> Optional[Dict]:
        """Find a standard in the database."""
        # Try exact match first
        if year:
            full_id = f"{std_num}:{year}"
            if full_id in self.standards:
                return self.standards[full_id]

        # Try matching by number only
        for is_num, std in self.standards.items():
            base_num = is_num.split(":")[0]
            if base_num == std_num:
                return std

        return None

    def _amendment_referenced(self, text: str, standard: Dict) -> bool:
        """Check if the latest amendment is referenced in text."""
        amendment = standard.get("latest_amendment", "")
        if not amendment:
            return True

        # Check for patterns like "Amd 1", "Amendment 1", etc.
        patterns = [
            rf'{standard["is_number"]}.*{amendment}',
            rf'{amendment}.*{standard["is_number"]}',
            rf'Amendment.*{amendment.split()[-1]}' if amendment else '',
        ]

        for pattern in patterns:
            if pattern and re.search(pattern, text, re.IGNORECASE):
                return True

        return False

    def _check_dependencies(self, referenced_ids: List[str]) -> Dict[str, List[str]]:
        """Check if all required dependencies are referenced."""
        referenced_set = set(referenced_ids)
        missing = {}

        for std_id in referenced_ids:
            if std_id not in self.standards:
                continue

            std = self.standards[std_id]
            required = std.get("normative_references", [])

            for req in required:
                # Check if any version of the required standard is referenced
                req_base = req.split(":")[0] if ":" in req else req
                found = any(
                    ref_id.startswith(req_base) or req_base in ref_id
                    for ref_id in referenced_set
                )

                if not found:
                    if std_id not in missing:
                        missing[std_id] = []
                    missing[std_id].append(req)

        return missing

    def _check_certifications(
        self,
        referenced_ids: List[str],
        text: str
    ) -> List[Dict]:
        """Check if mandatory certifications are mentioned."""
        missing = []
        cert_patterns = [
            r'BIS\s*mark',
            r'ISI\s*mark',
            r'certification',
            r'certified',
            r'CRS',
            r'compulsory\s*registration'
        ]

        has_cert_mention = any(
            re.search(p, text, re.IGNORECASE) for p in cert_patterns
        )

        for std_id in referenced_ids:
            if std_id not in self.standards:
                continue

            std = self.standards[std_id]
            if std.get("mandatory_certification") and not has_cert_mention:
                missing.append({
                    "standard": std_id,
                    "type": "BIS ISI Mark"
                })

        return missing


def audit_text(text: str, standards_db: Dict) -> AuditResult:
    """Convenience function to audit text."""
    auditor = TenderAuditor(standards_db)
    return auditor.audit(text)


def audit_pdf(pdf_path: str, standards_db: Dict) -> AuditResult:
    """Audit a PDF file."""
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return audit_text(text, standards_db)
    except ImportError:
        raise ImportError("PyMuPDF not installed. Run: pip install PyMuPDF")
    except Exception as e:
        raise Exception(f"Error reading PDF: {e}")
