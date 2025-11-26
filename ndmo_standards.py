#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NDMO Quality Standards and Requirements
National Data Management Office Quality Standards

Developer: AI Assistant
Purpose: Define comprehensive NDMO quality standards for data governance
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
import json

class QualityLevel(Enum):
    """Quality levels for NDMO standards"""
    EXCELLENT = "excellent"
    GOOD = "good"
    ACCEPTABLE = "acceptable"
    POOR = "poor"
    CRITICAL = "critical"

class ComplianceStatus(Enum):
    """Compliance status"""
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NOT_APPLICABLE = "not_applicable"

@dataclass
class NDMOStandard:
    """Individual NDMO standard definition"""
    id: str
    name: str
    description: str
    category: str
    requirement: str
    threshold: float
    weight: float
    critical: bool = False

class NDMOStandardsManager:
    """Manager for NDMO quality standards"""
    
    def __init__(self):
        """Initialize NDMO standards manager"""
        self.standards = self._load_ndmo_standards()
        self.categories = self._get_categories()
    
    def _load_ndmo_standards(self) -> Dict[str, NDMOStandard]:
        """Load NDMO quality standards"""
        standards = {}
        
        # Data Governance Standards
        standards["DG001"] = NDMOStandard(
            id="DG001",
            name="Unique Identifiers",
            description="All data records must have unique identifiers",
            category="Data Governance",
            requirement="Primary key must exist and be unique",
            threshold=1.0,
            weight=0.2,
            critical=True
        )
        
        standards["DG002"] = NDMOStandard(
            id="DG002",
            name="Data Lineage",
            description="Data lineage must be documented and traceable",
            category="Data Governance",
            requirement="Source and transformation history must be documented",
            threshold=0.8,
            weight=0.15
        )
        
        standards["DG003"] = NDMOStandard(
            id="DG003",
            name="Data Ownership",
            description="Data ownership must be clearly defined",
            category="Data Governance",
            requirement="Data steward and owner must be identified",
            threshold=0.9,
            weight=0.1
        )
        
        # Data Quality Standards
        standards["DQ001"] = NDMOStandard(
            id="DQ001",
            name="Data Completeness",
            description="Data completeness must meet minimum thresholds",
            category="Data Quality",
            requirement="No more than 5% missing values in critical fields",
            threshold=0.95,
            weight=0.25,
            critical=True
        )
        
        standards["DQ002"] = NDMOStandard(
            id="DQ002",
            name="Data Accuracy",
            description="Data accuracy must be validated and verified",
            category="Data Quality",
            requirement="Data must pass accuracy validation rules",
            threshold=0.98,
            weight=0.2,
            critical=True
        )
        
        standards["DQ003"] = NDMOStandard(
            id="DQ003",
            name="Data Consistency",
            description="Data must be consistent across systems",
            category="Data Quality",
            requirement="Data values must be consistent with business rules",
            threshold=0.95,
            weight=0.15
        )
        
        standards["DQ004"] = NDMOStandard(
            id="DQ004",
            name="Data Uniqueness",
            description="Duplicate records must be minimized",
            category="Data Quality",
            requirement="No more than 2% duplicate records",
            threshold=0.98,
            weight=0.15
        )
        
        standards["DQ005"] = NDMOStandard(
            id="DQ005",
            name="Data Validity",
            description="Data must conform to defined formats and ranges",
            category="Data Quality",
            requirement="Data must pass format and range validation",
            threshold=0.95,
            weight=0.15
        )
        
        standards["DQ006"] = NDMOStandard(
            id="DQ006",
            name="Data Timeliness",
            description="Data must be current and up-to-date",
            category="Data Quality",
            requirement="Data must be updated within defined timeframes",
            threshold=0.9,
            weight=0.1
        )
        
        # Data Security Standards
        standards["DS001"] = NDMOStandard(
            id="DS001",
            name="Data Encryption",
            description="Sensitive data must be encrypted",
            category="Data Security",
            requirement="PII and sensitive data must be encrypted at rest and in transit",
            threshold=1.0,
            weight=0.3,
            critical=True
        )
        
        standards["DS002"] = NDMOStandard(
            id="DS002",
            name="Access Control",
            description="Data access must be controlled and monitored",
            category="Data Security",
            requirement="Role-based access control must be implemented",
            threshold=0.95,
            weight=0.25
        )
        
        standards["DS003"] = NDMOStandard(
            id="DS003",
            name="Data Masking",
            description="Sensitive data must be masked in non-production environments",
            category="Data Security",
            requirement="PII must be masked in test and development environments",
            threshold=1.0,
            weight=0.2
        )
        
        standards["DS004"] = NDMOStandard(
            id="DS004",
            name="Audit Trail",
            description="Data access and modifications must be logged",
            category="Data Security",
            requirement="Complete audit trail must be maintained",
            threshold=0.95,
            weight=0.25
        )
        
        # Data Architecture Standards
        standards["DA001"] = NDMOStandard(
            id="DA001",
            name="Data Modeling",
            description="Data models must follow standard conventions",
            category="Data Architecture",
            requirement="Data models must follow naming conventions and best practices",
            threshold=0.9,
            weight=0.2
        )
        
        standards["DA002"] = NDMOStandard(
            id="DA002",
            name="Data Integration",
            description="Data integration must be standardized",
            category="Data Architecture",
            requirement="ETL processes must follow standard patterns",
            threshold=0.85,
            weight=0.15
        )
        
        standards["DA003"] = NDMOStandard(
            id="DA003",
            name="Data Storage",
            description="Data storage must follow retention policies",
            category="Data Architecture",
            requirement="Data must be stored according to retention policies",
            threshold=0.9,
            weight=0.15
        )
        
        # Business Rules Standards
        standards["BR001"] = NDMOStandard(
            id="BR001",
            name="Business Rule Validation",
            description="Business rules must be implemented and validated",
            category="Business Rules",
            requirement="All business rules must be documented and implemented",
            threshold=0.95,
            weight=0.3
        )
        
        standards["BR002"] = NDMOStandard(
            id="BR002",
            name="Data Relationships",
            description="Data relationships must be properly defined",
            category="Business Rules",
            requirement="Foreign key relationships must be enforced",
            threshold=0.9,
            weight=0.2
        )
        
        standards["BR003"] = NDMOStandard(
            id="BR003",
            name="Calculated Fields",
            description="Calculated fields must be accurate and consistent",
            category="Business Rules",
            requirement="Calculated fields must follow business logic",
            threshold=0.98,
            weight=0.25
        )
        
        return standards
    
    def _get_categories(self) -> List[str]:
        """Get all categories"""
        return ["Data Governance", "Data Quality", "Data Security", "Data Architecture", "Business Rules"]
    
    def get_standard(self, standard_id: str) -> Optional[NDMOStandard]:
        """Get a specific standard by ID"""
        return self.standards.get(standard_id)
    
    def get_standards_by_category(self, category: str) -> List[NDMOStandard]:
        """Get all standards in a category"""
        return [std for std in self.standards.values() if std.category == category]
    
    def get_critical_standards(self) -> List[NDMOStandard]:
        """Get all critical standards"""
        return [std for std in self.standards.values() if std.critical]
    
    def calculate_compliance_score(self, results: Dict[str, float]) -> Dict[str, Any]:
        """Calculate overall compliance score"""
        total_weight = 0
        weighted_score = 0
        critical_failures = []
        
        for standard_id, score in results.items():
            if standard_id in self.standards:
                standard = self.standards[standard_id]
                total_weight += standard.weight
                weighted_score += score * standard.weight
                
                if standard.critical and score < standard.threshold:
                    critical_failures.append(standard_id)
        
        overall_score = weighted_score / total_weight if total_weight > 0 else 0
        
        # Determine compliance status
        if critical_failures:
            status = ComplianceStatus.NON_COMPLIANT
        elif overall_score >= 0.95:
            status = ComplianceStatus.COMPLIANT
        elif overall_score >= 0.8:
            status = ComplianceStatus.PARTIALLY_COMPLIANT
        else:
            status = ComplianceStatus.NON_COMPLIANT
        
        return {
            "overall_score": overall_score,
            "status": status.value,
            "critical_failures": critical_failures,
            "category_scores": self._calculate_category_scores(results),
            "recommendations": self._generate_recommendations(results)
        }
    
    def _calculate_category_scores(self, results: Dict[str, float]) -> Dict[str, float]:
        """Calculate scores by category"""
        category_scores = {}
        
        for category in self.categories:
            category_standards = self.get_standards_by_category(category)
            category_weight = sum(std.weight for std in category_standards)
            category_score = 0
            
            for standard in category_standards:
                if standard.id in results:
                    category_score += results[standard.id] * standard.weight
            
            category_scores[category] = category_score / category_weight if category_weight > 0 else 0
        
        return category_scores
    
    def _generate_recommendations(self, results: Dict[str, float]) -> List[str]:
        """Generate recommendations based on results"""
        recommendations = []
        
        for standard_id, score in results.items():
            if standard_id in self.standards:
                standard = self.standards[standard_id]
                if score < standard.threshold:
                    recommendations.append(
                        f"Improve {standard.name}: Current score {score:.1%}, "
                        f"required {standard.threshold:.1%}. {standard.requirement}"
                    )
        
        return recommendations
    
    def validate_schema_compliance(self, schema_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate schema against NDMO standards"""
        results = {}
        
        # Check for unique identifiers
        has_primary_key = self._check_primary_key(schema_data)
        results["DG001"] = 1.0 if has_primary_key else 0.0
        
        # Check data completeness requirements
        completeness_score = self._check_completeness_requirements(schema_data)
        results["DQ001"] = completeness_score
        
        # Check data types and formats
        validity_score = self._check_data_validity(schema_data)
        results["DQ005"] = validity_score
        
        # Check business rules
        business_rules_score = self._check_business_rules(schema_data)
        results["BR001"] = business_rules_score
        
        return self.calculate_compliance_score(results)
    
    def _check_primary_key(self, schema_data: Dict[str, Any]) -> bool:
        """Check if schema has primary key"""
        columns = schema_data.get("columns", [])
        for column in columns:
            if column.get("primary_key", False) or column.get("unique", False):
                return True
        return False
    
    def _check_completeness_requirements(self, schema_data: Dict[str, Any]) -> float:
        """Check completeness requirements"""
        columns = schema_data.get("columns", [])
        if not columns:
            return 0.0
        
        required_fields = 0
        for column in columns:
            if column.get("required", False):
                required_fields += 1
        
        return min(1.0, required_fields / max(len(columns) * 0.3, 1))
    
    def _check_data_validity(self, schema_data: Dict[str, Any]) -> float:
        """Check data validity requirements"""
        columns = schema_data.get("columns", [])
        if not columns:
            return 0.0
        
        valid_columns = 0
        for column in columns:
            if column.get("data_type") and column.get("constraints"):
                valid_columns += 1
        
        return valid_columns / len(columns)
    
    def _check_business_rules(self, schema_data: Dict[str, Any]) -> float:
        """Check business rules implementation"""
        business_rules = schema_data.get("business_rules", [])
        if not business_rules:
            return 0.5  # Partial score if no business rules defined
        
        implemented_rules = sum(1 for rule in business_rules if rule.get("implemented", False))
        return implemented_rules / len(business_rules)
    
    def export_standards(self, filepath: str = "ndmo_standards.json"):
        """Export standards to JSON file"""
        standards_data = {}
        for std_id, standard in self.standards.items():
            standards_data[std_id] = {
                "id": standard.id,
                "name": standard.name,
                "description": standard.description,
                "category": standard.category,
                "requirement": standard.requirement,
                "threshold": standard.threshold,
                "weight": standard.weight,
                "critical": standard.critical
            }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(standards_data, f, indent=2, ensure_ascii=False)
        
        return filepath

def main():
    """Test the NDMO standards manager"""
    manager = NDMOStandardsManager()
    
    print("NDMO Quality Standards Manager")
    print("=" * 50)
    
    # Display all standards
    for category in manager.categories:
        print(f"\n{category}:")
        standards = manager.get_standards_by_category(category)
        for standard in standards:
            critical_mark = " [CRITICAL]" if standard.critical else ""
            print(f"  {standard.id}: {standard.name}{critical_mark}")
            print(f"    Threshold: {standard.threshold:.1%}")
            print(f"    Weight: {standard.weight:.1%}")
    
    # Test compliance calculation
    test_results = {
        "DG001": 1.0,
        "DQ001": 0.95,
        "DQ002": 0.98,
        "DQ005": 0.90,
        "BR001": 0.85
    }
    
    compliance = manager.calculate_compliance_score(test_results)
    print(f"\nTest Compliance Score: {compliance['overall_score']:.1%}")
    print(f"Status: {compliance['status']}")
    
    # Export standards
    export_file = manager.export_standards()
    print(f"\nStandards exported to: {export_file}")

if __name__ == "__main__":
    main()











