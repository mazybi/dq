#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Schema Problem Analyzer and Corrector
Detailed analysis of schema problems with specific correction recommendations

Developer: AI Assistant
Purpose: Analyze schema problems and provide specific correction guidance
"""

import pandas as pd
import numpy as np
from datetime import datetime
import json
from typing import Dict, List, Any, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

from ndmo_standards import NDMOStandardsManager, ComplianceStatus
from smart_schema_analyzer import SmartSchemaAnalyzer

class SchemaProblemAnalyzer:
    """Analyzes schema problems and provides correction guidance"""
    
    def __init__(self):
        """Initialize the problem analyzer"""
        self.ndmo_manager = NDMOStandardsManager()
        self.schema_analyzer = SmartSchemaAnalyzer()
        self.problem_analysis = {}
        self.correction_plan = {}
    
    def analyze_schema_problems(self, schema_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze specific problems in the schema"""
        print("🔍 Analyzing schema problems...")
        
        problems = {
            "critical_problems": [],
            "major_problems": [],
            "minor_problems": [],
            "missing_requirements": [],
            "correction_plan": {},
            "priority_actions": []
        }
        
        schema_info = schema_analysis.get("schema_analysis", {})
        ndmo_compliance = schema_analysis.get("ndmo_compliance", {})
        
        # Analyze each category
        self._analyze_data_governance_problems(schema_info, problems)
        self._analyze_data_quality_problems(schema_info, problems)
        self._analyze_data_security_problems(schema_info, problems)
        self._analyze_data_architecture_problems(schema_info, problems)
        self._analyze_business_rules_problems(schema_info, problems)
        
        # Generate correction plan
        problems["correction_plan"] = self._generate_correction_plan(problems)
        problems["priority_actions"] = self._prioritize_actions(problems)
        
        self.problem_analysis = problems
        return problems
    
    def _analyze_data_governance_problems(self, schema_info: Dict[str, Any], problems: Dict[str, Any]):
        """Analyze data governance problems"""
        columns = schema_info.get("columns", [])
        
        # Check for unique identifiers (DG001)
        has_primary_key = any(col.get("primary_key", False) for col in columns)
        if not has_primary_key:
            problems["critical_problems"].append({
                "id": "DG001",
                "name": "Missing Primary Key",
                "description": "No primary key found in schema",
                "impact": "Critical - Data integrity compromised",
                "solution": "Add a primary key column (e.g., 'id', 'serial_number')",
                "example": "Add column: 'id' (integer, auto-increment, primary key)"
            })
        
        # Check for data lineage (DG002)
        has_documentation = any("documentation" in col.get("name", "").lower() for col in columns)
        if not has_documentation:
            problems["major_problems"].append({
                "id": "DG002",
                "name": "Missing Data Lineage",
                "description": "No data lineage documentation found",
                "impact": "Major - Data traceability compromised",
                "solution": "Add columns for data source and transformation history",
                "example": "Add columns: 'data_source', 'created_date', 'last_modified'"
            })
        
        # Check for data ownership (DG003)
        has_ownership = any("owner" in col.get("name", "").lower() or "steward" in col.get("name", "").lower() for col in columns)
        if not has_ownership:
            problems["major_problems"].append({
                "id": "DG003",
                "name": "Missing Data Ownership",
                "description": "No data ownership information found",
                "impact": "Major - Data accountability unclear",
                "solution": "Add columns for data owner and steward",
                "example": "Add columns: 'data_owner', 'data_steward', 'department'"
            })
    
    def _analyze_data_quality_problems(self, schema_info: Dict[str, Any], problems: Dict[str, Any]):
        """Analyze data quality problems"""
        columns = schema_info.get("columns", [])
        
        # Check for completeness requirements (DQ001)
        required_fields = sum(1 for col in columns if col.get("constraints", {}).get("required", False))
        if required_fields < len(columns) * 0.3:  # Less than 30% required fields
            problems["major_problems"].append({
                "id": "DQ001",
                "name": "Insufficient Required Fields",
                "description": f"Only {required_fields} out of {len(columns)} fields are marked as required",
                "impact": "Major - Data completeness compromised",
                "solution": "Mark critical fields as required",
                "example": "Set required=True for: customer_id, invoice_number, amount, date"
            })
        
        # Check for data validation (DQ002)
        fields_with_validation = sum(1 for col in columns if col.get("constraints", {}))
        if fields_with_validation < len(columns) * 0.5:  # Less than 50% with validation
            problems["major_problems"].append({
                "id": "DQ002",
                "name": "Insufficient Data Validation",
                "description": f"Only {fields_with_validation} out of {len(columns)} fields have validation rules",
                "impact": "Major - Data accuracy compromised",
                "solution": "Add validation rules for all fields",
                "example": "Add constraints: min_length, max_length, allowed_values, pattern"
            })
        
        # Check for uniqueness constraints (DQ004)
        unique_fields = sum(1 for col in columns if col.get("unique", False))
        if unique_fields < 2:  # Less than 2 unique fields
            problems["major_problems"].append({
                "id": "DQ004",
                "name": "Insufficient Uniqueness Constraints",
                "description": f"Only {unique_fields} fields have uniqueness constraints",
                "impact": "Major - Data uniqueness compromised",
                "solution": "Add uniqueness constraints to key fields",
                "example": "Set unique=True for: customer_id, invoice_number, email"
            })
        
        # Check for data types (DQ005)
        unknown_types = sum(1 for col in columns if col.get("data_type") == "unknown")
        if unknown_types > 0:
            problems["minor_problems"].append({
                "id": "DQ005",
                "name": "Unknown Data Types",
                "description": f"{unknown_types} fields have unknown data types",
                "impact": "Minor - Data type validation compromised",
                "solution": "Define specific data types for all fields",
                "example": "Set data_type: 'numeric', 'datetime', 'text', 'email', 'phone'"
            })
    
    def _analyze_data_security_problems(self, schema_info: Dict[str, Any], problems: Dict[str, Any]):
        """Analyze data security problems"""
        columns = schema_info.get("columns", [])
        
        # Check for sensitive data protection (DS001)
        sensitive_fields = [col for col in columns if any(keyword in col.get("name", "").lower() 
                          for keyword in ["password", "ssn", "credit", "card", "secret", "private"])]
        if sensitive_fields:
            problems["critical_problems"].append({
                "id": "DS001",
                "name": "Sensitive Data Exposure",
                "description": f"Found {len(sensitive_fields)} fields with sensitive data",
                "impact": "Critical - Data security compromised",
                "solution": "Encrypt or mask sensitive data fields",
                "example": "Add encryption for: password, ssn, credit_card_number"
            })
        
        # Check for access control (DS002)
        has_access_control = any("access" in col.get("name", "").lower() or "permission" in col.get("name", "").lower() for col in columns)
        if not has_access_control:
            problems["major_problems"].append({
                "id": "DS002",
                "name": "Missing Access Control",
                "description": "No access control information found",
                "impact": "Major - Data access control compromised",
                "solution": "Add access control fields",
                "example": "Add columns: 'access_level', 'permissions', 'user_role'"
            })
        
        # Check for audit trail (DS004)
        has_audit_trail = any(keyword in col.get("name", "").lower() 
                             for keyword in ["created", "modified", "updated", "audit", "log"] for col in columns)
        if not has_audit_trail:
            problems["major_problems"].append({
                "id": "DS004",
                "name": "Missing Audit Trail",
                "description": "No audit trail information found",
                "impact": "Major - Data tracking compromised",
                "solution": "Add audit trail fields",
                "example": "Add columns: 'created_date', 'modified_date', 'created_by', 'modified_by'"
            })
    
    def _analyze_data_architecture_problems(self, schema_info: Dict[str, Any], problems: Dict[str, Any]):
        """Analyze data architecture problems"""
        columns = schema_info.get("columns", [])
        
        # Check for naming conventions (DA001)
        inconsistent_naming = sum(1 for col in columns if not self._is_consistent_naming(col.get("name", "")))
        if inconsistent_naming > 0:
            problems["minor_problems"].append({
                "id": "DA001",
                "name": "Inconsistent Naming",
                "description": f"{inconsistent_naming} fields have inconsistent naming",
                "impact": "Minor - Data architecture compromised",
                "solution": "Standardize field naming conventions",
                "example": "Use snake_case: customer_id, invoice_number, created_date"
            })
        
        # Check for data integration (DA002)
        has_integration_fields = any(keyword in col.get("name", "").lower() 
                                   for keyword in ["source", "system", "import", "sync"] for col in columns)
        if not has_integration_fields:
            problems["minor_problems"].append({
                "id": "DA002",
                "name": "Missing Integration Fields",
                "description": "No data integration information found",
                "impact": "Minor - Data integration compromised",
                "solution": "Add integration tracking fields",
                "example": "Add columns: 'source_system', 'import_date', 'sync_status'"
            })
    
    def _analyze_business_rules_problems(self, schema_info: Dict[str, Any], problems: Dict[str, Any]):
        """Analyze business rules problems"""
        business_rules = schema_info.get("business_rules", [])
        
        # Check for business rule implementation (BR001)
        implemented_rules = sum(1 for rule in business_rules if rule.get("implemented", False))
        if implemented_rules < len(business_rules) * 0.5:  # Less than 50% implemented
            problems["major_problems"].append({
                "id": "BR001",
                "name": "Insufficient Business Rules",
                "description": f"Only {implemented_rules} out of {len(business_rules)} business rules are implemented",
                "impact": "Major - Business logic compromised",
                "solution": "Implement all business rules",
                "example": "Add validation: amount > 0, date <= today, status in ['active', 'inactive']"
            })
        
        # Check for data relationships (BR002)
        relationships = schema_info.get("relationships", [])
        if len(relationships) == 0:
            problems["major_problems"].append({
                "id": "BR002",
                "name": "Missing Data Relationships",
                "description": "No data relationships defined",
                "impact": "Major - Data integrity compromised",
                "solution": "Define foreign key relationships",
                "example": "Add relationships: customer_id -> customers.id, invoice_id -> invoices.id"
            })
    
    def _is_consistent_naming(self, field_name: str) -> bool:
        """Check if field naming is consistent"""
        import re
        # Check for snake_case naming
        return bool(re.match(r'^[a-z][a-z0-9_]*$', field_name.lower()))
    
    def _generate_correction_plan(self, problems: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a detailed correction plan"""
        correction_plan = {
            "immediate_actions": [],
            "short_term_actions": [],
            "long_term_actions": [],
            "estimated_effort": {},
            "resources_needed": []
        }
        
        # Immediate actions (Critical problems)
        for problem in problems["critical_problems"]:
            correction_plan["immediate_actions"].append({
                "problem_id": problem["id"],
                "action": problem["solution"],
                "example": problem["example"],
                "effort": "High",
                "priority": "Critical"
            })
        
        # Short-term actions (Major problems)
        for problem in problems["major_problems"]:
            correction_plan["short_term_actions"].append({
                "problem_id": problem["id"],
                "action": problem["solution"],
                "example": problem["example"],
                "effort": "Medium",
                "priority": "High"
            })
        
        # Long-term actions (Minor problems)
        for problem in problems["minor_problems"]:
            correction_plan["long_term_actions"].append({
                "problem_id": problem["id"],
                "action": problem["solution"],
                "example": problem["example"],
                "effort": "Low",
                "priority": "Medium"
            })
        
        # Estimate effort
        correction_plan["estimated_effort"] = {
            "immediate": len(correction_plan["immediate_actions"]) * 2,  # hours
            "short_term": len(correction_plan["short_term_actions"]) * 1,  # hours
            "long_term": len(correction_plan["long_term_actions"]) * 0.5,  # hours
            "total": (len(correction_plan["immediate_actions"]) * 2 + 
                     len(correction_plan["short_term_actions"]) * 1 + 
                     len(correction_plan["long_term_actions"]) * 0.5)
        }
        
        # Resources needed
        correction_plan["resources_needed"] = [
            "Database Administrator",
            "Data Analyst",
            "Business Analyst",
            "Security Specialist"
        ]
        
        return correction_plan
    
    def _prioritize_actions(self, problems: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Prioritize actions based on impact and effort"""
        all_actions = []
        
        # Add critical problems
        for problem in problems["critical_problems"]:
            all_actions.append({
                "problem_id": problem["id"],
                "name": problem["name"],
                "priority": 1,  # Highest priority
                "impact": "Critical",
                "effort": "High",
                "action": problem["solution"]
            })
        
        # Add major problems
        for problem in problems["major_problems"]:
            all_actions.append({
                "problem_id": problem["id"],
                "name": problem["name"],
                "priority": 2,  # High priority
                "impact": "Major",
                "effort": "Medium",
                "action": problem["solution"]
            })
        
        # Add minor problems
        for problem in problems["minor_problems"]:
            all_actions.append({
                "problem_id": problem["id"],
                "name": problem["name"],
                "priority": 3,  # Medium priority
                "impact": "Minor",
                "effort": "Low",
                "action": problem["solution"]
            })
        
        # Sort by priority
        all_actions.sort(key=lambda x: x["priority"])
        
        return all_actions
    
    def generate_corrected_schema(self, schema_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a corrected schema based on problems found"""
        print("🔧 Generating corrected schema...")
        
        corrected_schema = schema_analysis.copy()
        schema_info = corrected_schema.get("schema_analysis", {})
        columns = schema_info.get("columns", [])
        
        # Add missing critical fields
        self._add_missing_critical_fields(columns)
        
        # Fix data types
        self._fix_data_types(columns)
        
        # Add constraints
        self._add_missing_constraints(columns)
        
        # Add business rules
        self._add_business_rules(schema_info)
        
        # Add relationships
        self._add_relationships(schema_info)
        
        return corrected_schema
    
    def make_schema_ndmo_compliant(self, schema_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Make schema fully NDMO compliant"""
        print("🛡️ Making schema NDMO compliant...")
        
        compliant_schema = schema_analysis.copy()
        schema_info = compliant_schema.get("schema_analysis", {})
        columns = schema_info.get("columns", [])
        
        # 1. Add Primary Key (DG001 - Unique Identifiers)
        self._ensure_primary_key(columns)
        
        # 2. Add Audit Trail Fields (DS004 - Audit Trail)
        self._add_audit_trail_fields(columns)
        
        # 3. Improve Data Types (DQ005 - Data Validity)
        self._improve_data_types_for_ndmo(columns)
        
        # 4. Add Data Quality Constraints (DQ001-DQ006)
        self._add_data_quality_constraints(columns)
        
        # 5. Add Security Fields (DS001-DS003)
        self._add_security_fields(columns)
        
        # 6. Add Business Rules (BR001-BR003)
        self._add_comprehensive_business_rules(schema_info)
        
        # 7. Add Data Lineage Fields (DG002 - Data Lineage)
        self._add_data_lineage_fields(columns)
        
        # 8. Add Data Ownership Fields (DG003 - Data Ownership)
        self._add_data_ownership_fields(columns)
        
        # Update schema info
        schema_info["total_columns"] = len(columns)
        schema_info["ndmo_compliant"] = True
        schema_info["compliance_improvements"] = self._get_compliance_improvements()
        
        return compliant_schema
    
    def _add_missing_critical_fields(self, columns: List[Dict[str, Any]]):
        """Add missing critical fields"""
        existing_names = [col.get("name", "").lower() for col in columns]
        
        # Add primary key if missing
        if not any("id" in name for name in existing_names):
            columns.append({
                "name": "id",
                "data_type": "numeric",
                "primary_key": True,
                "unique": True,
                "nullable": False,
                "constraints": {
                    "required": True,
                    "min_value": 1,
                    "max_value": 999999999
                },
                "sample_values": [1, 2, 3, 4, 5],
                "statistics": {
                    "total_values": 0,
                    "non_null_values": 0,
                    "null_values": 0,
                    "unique_values": 0,
                    "duplicate_values": 0
                },
                "quality_issues": []
            })
        
        # Add audit trail fields
        audit_fields = [
            {"name": "created_date", "data_type": "datetime"},
            {"name": "modified_date", "data_type": "datetime"},
            {"name": "created_by", "data_type": "text"},
            {"name": "modified_by", "data_type": "text"}
        ]
        
        for field in audit_fields:
            if field["name"] not in existing_names:
                columns.append({
                    "name": field["name"],
                    "data_type": field["data_type"],
                    "primary_key": False,
                    "unique": False,
                    "nullable": True,
                    "constraints": {
                        "required": field["name"] in ["created_date", "created_by"]
                    },
                    "sample_values": [],
                    "statistics": {
                        "total_values": 0,
                        "non_null_values": 0,
                        "null_values": 0,
                        "unique_values": 0,
                        "duplicate_values": 0
                    },
                    "quality_issues": []
                })
    
    def _fix_data_types(self, columns: List[Dict[str, Any]]):
        """Fix unknown data types"""
        for column in columns:
            if column.get("data_type") == "unknown":
                # Try to infer from name
                name = column.get("name", "").lower()
                if any(keyword in name for keyword in ["date", "time"]):
                    column["data_type"] = "datetime"
                elif any(keyword in name for keyword in ["amount", "price", "cost", "number", "count"]):
                    column["data_type"] = "numeric"
                elif any(keyword in name for keyword in ["email", "mail"]):
                    column["data_type"] = "email"
                elif any(keyword in name for keyword in ["phone", "mobile", "tel"]):
                    column["data_type"] = "phone"
                else:
                    column["data_type"] = "text"
    
    def _add_missing_constraints(self, columns: List[Dict[str, Any]]):
        """Add missing constraints"""
        for column in columns:
            if not column.get("constraints"):
                column["constraints"] = {}
            
            # Add basic constraints based on data type
            data_type = column.get("data_type", "text")
            constraints = column["constraints"]
            
            if data_type == "text":
                constraints.update({
                    "min_length": 1,
                    "max_length": 255
                })
            elif data_type == "numeric":
                constraints.update({
                    "min_value": 0,
                    "max_value": 999999999
                })
            elif data_type == "email":
                constraints.update({
                    "pattern": r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                    "format": "email"
                })
            elif data_type == "phone":
                constraints.update({
                    "pattern": r'^[\+]?[1-9][\d]{0,15}$',
                    "format": "phone"
                })
    
    def _add_business_rules(self, schema_info: Dict[str, Any]):
        """Add business rules"""
        if "business_rules" not in schema_info:
            schema_info["business_rules"] = []
        
        business_rules = schema_info["business_rules"]
        
        # Add common business rules
        common_rules = [
            {
                "name": "Positive Amounts",
                "type": "validation",
                "description": "All amount fields must be positive",
                "implemented": True,
                "rule": "amount > 0"
            },
            {
                "name": "Valid Dates",
                "type": "validation",
                "description": "All dates must be valid and not in the future",
                "implemented": True,
                "rule": "date <= today()"
            },
            {
                "name": "Required Fields",
                "type": "constraint",
                "description": "Critical fields must not be null",
                "implemented": True,
                "rule": "required_fields IS NOT NULL"
            }
        ]
        
        for rule in common_rules:
            if not any(existing_rule.get("name", "") == rule["name"] for existing_rule in business_rules):
                business_rules.append(rule)
    
    def _add_relationships(self, schema_info: Dict[str, Any]):
        """Add relationships"""
        if "relationships" not in schema_info:
            schema_info["relationships"] = []
        
        relationships = schema_info["relationships"]
        columns = schema_info.get("columns", [])
        
        # Add foreign key relationships
        for column in columns:
            name = column.get("name", "").lower()
            if name.endswith("_id") and name != "id":
                parent_table = name.replace("_id", "")
                relationships.append({
                    "type": "foreign_key",
                    "child_column": name,
                    "parent_table": parent_table,
                    "relationship_type": "many_to_one"
                })
    
    def export_problem_analysis(self, filepath: str = None) -> str:
        """Export problem analysis to JSON file"""
        if not filepath:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = f"schema_problem_analysis_{timestamp}.json"
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.problem_analysis, f, indent=2, ensure_ascii=False, default=str)
            
            print(f"✅ Problem analysis exported to: {filepath}")
            return filepath
        except Exception as e:
            print(f"❌ Error exporting analysis: {str(e)}")
            return None

def main():
    """Test the schema problem analyzer"""
    analyzer = SchemaProblemAnalyzer()
    
    # Example usage
    print("Schema Problem Analyzer")
    print("=" * 50)
    
    # This would typically be called with actual schema analysis results
    # For testing, we'll create a mock schema analysis
    mock_schema_analysis = {
        "schema_analysis": {
            "columns": [
                {
                    "name": "customer_name",
                    "data_type": "text",
                    "primary_key": False,
                    "unique": False,
                    "nullable": True,
                    "constraints": {},
                    "quality_issues": []
                }
            ],
            "business_rules": [],
            "relationships": []
        },
        "ndmo_compliance": {
            "overall_score": 0.389,
            "status": "non_compliant"
        }
    }
    
    # Analyze problems
    problems = analyzer.analyze_schema_problems(mock_schema_analysis)
    
    print(f"Critical Problems: {len(problems['critical_problems'])}")
    print(f"Major Problems: {len(problems['major_problems'])}")
    print(f"Minor Problems: {len(problems['minor_problems'])}")
    
    # Export analysis
    export_file = analyzer.export_problem_analysis()
    if export_file:
        print(f"Analysis saved to: {export_file}")

class SchemaNDMOComplianceProcessor:
    """Process schema to make it NDMO compliant"""
    
    def __init__(self):
        self.ndmo_standards_manager = NDMOStandardsManager()
    
    def make_schema_ndmo_compliant(self, schema_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Make schema fully NDMO compliant"""
        print("🛡️ Making schema NDMO compliant...")
        
        compliant_schema = schema_analysis.copy()
        schema_info = compliant_schema.get("schema_analysis", {})
        columns = schema_info.get("columns", [])
        
        # 1. Add Primary Key (DG001 - Unique Identifiers)
        self._ensure_primary_key(columns)
        
        # 2. Add Audit Trail Fields (DS004 - Audit Trail)
        self._add_audit_trail_fields(columns)
        
        # 3. Improve Data Types (DQ005 - Data Validity)
        self._improve_data_types_for_ndmo(columns)
        
        # 4. Add Data Quality Constraints (DQ001-DQ006)
        self._add_data_quality_constraints(columns)
        
        # 5. Add Security Fields (DS001-DS003)
        self._add_security_fields(columns)
        
        # 6. Add Business Rules (BR001-BR003)
        self._add_comprehensive_business_rules(schema_info)
        
        # 7. Add Data Lineage Fields (DG002 - Data Lineage)
        self._add_data_lineage_fields(columns)
        
        # 8. Add Data Ownership Fields (DG003 - Data Ownership)
        self._add_data_ownership_fields(columns)
        
        # Update schema info
        schema_info["total_columns"] = len(columns)
        schema_info["ndmo_compliant"] = True
        schema_info["compliance_improvements"] = self._get_compliance_improvements()
        
        return compliant_schema
    
    def _ensure_primary_key(self, columns: List[Dict[str, Any]]):
        """Ensure primary key exists (DG001 - Unique Identifiers)"""
        existing_names = [col.get("name", "").lower() for col in columns]
        
        # Check if primary key exists
        has_primary_key = any(col.get("primary_key", False) for col in columns)
        
        if not has_primary_key:
            # Add primary key
            columns.insert(0, {
                "name": "id",
                "data_type": "numeric",
                "primary_key": True,
                "unique": True,
                "nullable": False,
                "constraints": {
                    "required": True,
                    "min_value": 1,
                    "max_value": 999999999,
                    "auto_increment": True
                },
                "sample_values": [1, 2, 3, 4, 5],
                "statistics": {
                    "total_values": 0,
                    "non_null_values": 0,
                    "null_values": 0,
                    "unique_values": 0,
                    "duplicate_values": 0
                },
                "quality_issues": [],
                "ndmo_standard": "DG001",
                "description": "Primary key for unique identification"
            })
    
    def _add_audit_trail_fields(self, columns: List[Dict[str, Any]]):
        """Add audit trail fields (DS004 - Audit Trail)"""
        existing_names = [col.get("name", "").lower() for col in columns]
        
        audit_fields = [
            {
                "name": "created_date",
                "data_type": "datetime",
                "nullable": False,
                "constraints": {
                    "required": True,
                    "format": "YYYY-MM-DD HH:MM:SS"
                },
                "ndmo_standard": "DS004",
                "description": "Record creation timestamp"
            },
            {
                "name": "modified_date",
                "data_type": "datetime",
                "nullable": True,
                "constraints": {
                    "required": False,
                    "format": "YYYY-MM-DD HH:MM:SS"
                },
                "ndmo_standard": "DS004",
                "description": "Record modification timestamp"
            },
            {
                "name": "created_by",
                "data_type": "text",
                "nullable": False,
                "constraints": {
                    "required": True,
                    "max_length": 100
                },
                "ndmo_standard": "DS004",
                "description": "User who created the record"
            },
            {
                "name": "modified_by",
                "data_type": "text",
                "nullable": True,
                "constraints": {
                    "required": False,
                    "max_length": 100
                },
                "ndmo_standard": "DS004",
                "description": "User who last modified the record"
            }
        ]
        
        for field in audit_fields:
            if field["name"] not in existing_names:
                field.update({
                    "unique": False,
                    "primary_key": False,
                    "foreign_key": False,
                    "sample_values": [],
                    "statistics": {
                        "total_values": 0,
                        "non_null_values": 0,
                        "null_values": 0,
                        "unique_values": 0,
                        "duplicate_values": 0
                    },
                    "quality_issues": []
                })
                columns.append(field)
    
    def _improve_data_types_for_ndmo(self, columns: List[Dict[str, Any]]):
        """Improve data types for NDMO compliance (DQ005 - Data Validity)"""
        for column in columns:
            column_name = column.get("name", "").lower()
            current_type = column.get("data_type", "")
            
            # Improve specific field types
            if "date" in column_name or "time" in column_name:
                column["data_type"] = "datetime"
                column["constraints"]["format"] = "YYYY-MM-DD HH:MM:SS"
            elif "email" in column_name:
                column["data_type"] = "email"
                column["constraints"]["pattern"] = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            elif "phone" in column_name or "mobile" in column_name:
                column["data_type"] = "phone"
                column["constraints"]["pattern"] = r"^\+?[1-9]\d{1,14}$"
            elif "amount" in column_name or "price" in column_name or "charge" in column_name:
                column["data_type"] = "numeric"
                column["constraints"]["min_value"] = 0
                column["constraints"]["decimal_places"] = 2
    
    def _add_data_quality_constraints(self, columns: List[Dict[str, Any]]):
        """Add data quality constraints (DQ001-DQ006)"""
        for column in columns:
            column_name = column.get("name", "").lower()
            constraints = column.get("constraints", {})
            
            # Add completeness constraints
            if "id" in column_name or "key" in column_name:
                constraints["required"] = True
                column["nullable"] = False
            
            # Add validity constraints
            if column.get("data_type") == "text":
                if not constraints.get("max_length"):
                    constraints["max_length"] = 255
            
            # Add consistency constraints
            if "code" in column_name:
                constraints["pattern"] = r"^[A-Z0-9_]+$"
                constraints["case_sensitive"] = True
    
    def _add_security_fields(self, columns: List[Dict[str, Any]]):
        """Add security fields (DS001-DS003)"""
        existing_names = [col.get("name", "").lower() for col in columns]
        
        security_fields = [
            {
                "name": "data_classification",
                "data_type": "categorical",
                "nullable": False,
                "constraints": {
                    "required": True,
                    "allowed_values": ["Public", "Internal", "Confidential", "Restricted"]
                },
                "ndmo_standard": "DS001",
                "description": "Data classification level"
            },
            {
                "name": "access_level",
                "data_type": "categorical",
                "nullable": False,
                "constraints": {
                    "required": True,
                    "allowed_values": ["Read", "Write", "Admin"]
                },
                "ndmo_standard": "DS002",
                "description": "Required access level"
            }
        ]
        
        for field in security_fields:
            if field["name"] not in existing_names:
                field.update({
                    "unique": False,
                    "primary_key": False,
                    "foreign_key": False,
                    "sample_values": [],
                    "statistics": {
                        "total_values": 0,
                        "non_null_values": 0,
                        "null_values": 0,
                        "unique_values": 0,
                        "duplicate_values": 0
                    },
                    "quality_issues": []
                })
                columns.append(field)
    
    def _add_comprehensive_business_rules(self, schema_info: Dict[str, Any]):
        """Add comprehensive business rules (BR001-BR003)"""
        business_rules = [
            {
                "rule_id": "BR001",
                "rule_name": "Primary Key Constraint",
                "description": "Every record must have a unique primary key",
                "severity": "critical",
                "ndmo_standard": "DG001"
            },
            {
                "rule_id": "BR002",
                "rule_name": "Audit Trail Requirement",
                "description": "All records must have creation and modification tracking",
                "severity": "high",
                "ndmo_standard": "DS004"
            },
            {
                "rule_id": "BR003",
                "rule_name": "Data Classification",
                "description": "All data must be classified according to security levels",
                "severity": "high",
                "ndmo_standard": "DS001"
            },
            {
                "rule_id": "BR004",
                "rule_name": "Data Completeness",
                "description": "Critical fields must not be null",
                "severity": "medium",
                "ndmo_standard": "DQ001"
            },
            {
                "rule_id": "BR005",
                "rule_name": "Data Validity",
                "description": "Data must conform to defined formats and patterns",
                "severity": "medium",
                "ndmo_standard": "DQ005"
            }
        ]
        
        schema_info["business_rules"] = business_rules
    
    def _add_data_lineage_fields(self, columns: List[Dict[str, Any]]):
        """Add data lineage fields (DG002 - Data Lineage)"""
        existing_names = [col.get("name", "").lower() for col in columns]
        
        lineage_fields = [
            {
                "name": "source_system",
                "data_type": "text",
                "nullable": False,
                "constraints": {
                    "required": True,
                    "max_length": 100
                },
                "ndmo_standard": "DG002",
                "description": "Source system identifier"
            },
            {
                "name": "extraction_date",
                "data_type": "datetime",
                "nullable": False,
                "constraints": {
                    "required": True,
                    "format": "YYYY-MM-DD HH:MM:SS"
                },
                "ndmo_standard": "DG002",
                "description": "Data extraction timestamp"
            }
        ]
        
        for field in lineage_fields:
            if field["name"] not in existing_names:
                field.update({
                    "unique": False,
                    "primary_key": False,
                    "foreign_key": False,
                    "sample_values": [],
                    "statistics": {
                        "total_values": 0,
                        "non_null_values": 0,
                        "null_values": 0,
                        "unique_values": 0,
                        "duplicate_values": 0
                    },
                    "quality_issues": []
                })
                columns.append(field)
    
    def _add_data_ownership_fields(self, columns: List[Dict[str, Any]]):
        """Add data ownership fields (DG003 - Data Ownership)"""
        existing_names = [col.get("name", "").lower() for col in columns]
        
        ownership_fields = [
            {
                "name": "data_owner",
                "data_type": "text",
                "nullable": False,
                "constraints": {
                    "required": True,
                    "max_length": 100
                },
                "ndmo_standard": "DG003",
                "description": "Data owner department or person"
            },
            {
                "name": "data_steward",
                "data_type": "text",
                "nullable": True,
                "constraints": {
                    "required": False,
                    "max_length": 100
                },
                "ndmo_standard": "DG003",
                "description": "Data steward responsible for quality"
            }
        ]
        
        for field in ownership_fields:
            if field["name"] not in existing_names:
                field.update({
                    "unique": False,
                    "primary_key": False,
                    "foreign_key": False,
                    "sample_values": [],
                    "statistics": {
                        "total_values": 0,
                        "non_null_values": 0,
                        "null_values": 0,
                        "unique_values": 0,
                        "duplicate_values": 0
                    },
                    "quality_issues": []
                })
                columns.append(field)
    
    def _get_compliance_improvements(self) -> List[Dict[str, Any]]:
        """Get list of compliance improvements made"""
        return [
            {
                "improvement": "Added Primary Key",
                "ndmo_standard": "DG001",
                "description": "Ensures unique identification of records"
            },
            {
                "improvement": "Added Audit Trail Fields",
                "ndmo_standard": "DS004",
                "description": "Tracks record creation and modification"
            },
            {
                "improvement": "Improved Data Types",
                "ndmo_standard": "DQ005",
                "description": "Enhanced data validity and format compliance"
            },
            {
                "improvement": "Added Security Classification",
                "ndmo_standard": "DS001",
                "description": "Implements data security classification"
            },
            {
                "improvement": "Added Data Lineage Tracking",
                "ndmo_standard": "DG002",
                "description": "Tracks data source and extraction"
            },
            {
                "improvement": "Added Data Ownership",
                "ndmo_standard": "DG003",
                "description": "Defines data ownership and stewardship"
            }
        ]

if __name__ == "__main__":
    main()



