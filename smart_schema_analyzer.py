#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart Schema Analyzer and Validator
Intelligent schema analysis with NDMO compliance checking and auto-correction

Developer: AI Assistant
Purpose: Analyze Excel schemas, validate against NDMO standards, and auto-correct issues
"""

import pandas as pd
import numpy as np
import openpyxl
from datetime import datetime
import json
import re
from typing import Dict, List, Any, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

from ndmo_standards import NDMOStandardsManager, ComplianceStatus

class SmartSchemaAnalyzer:
    """Smart schema analyzer with NDMO compliance and auto-correction"""
    
    def __init__(self):
        """Initialize the smart schema analyzer"""
        self.ndmo_manager = NDMOStandardsManager()
        self.analysis_results = {}
        self.correction_log = []
        self.schema_metadata = {}
    
    def analyze_schema_file(self, file_path: str) -> Dict[str, Any]:
        """Analyze schema from Excel file"""
        print(f"🔍 Analyzing schema file: {file_path}")
        
        try:
            # Load Excel file
            workbook = openpyxl.load_workbook(file_path, data_only=True)
            sheet_names = workbook.sheetnames
            
            print(f"📊 Found sheets: {sheet_names}")
            
            # Find schema sheet
            schema_sheet = self._find_schema_sheet(sheet_names)
            if not schema_sheet:
                print("⚠️ No schema sheet found, analyzing all sheets")
                schema_sheet = sheet_names[0] if sheet_names else None
            
            if not schema_sheet:
                raise ValueError("No sheets found in the file")
            
            print(f"📋 Analyzing schema sheet: {schema_sheet}")
            
            # Load schema data
            schema_df = pd.read_excel(file_path, sheet_name=schema_sheet)
            
            # Analyze schema structure
            schema_analysis = self._analyze_schema_structure(schema_df, schema_sheet)
            
            # Validate against NDMO standards
            ndmo_compliance = self.ndmo_manager.validate_schema_compliance(schema_analysis)
            
            # Store results
            self.analysis_results = {
                "file_path": file_path,
                "schema_sheet": schema_sheet,
                "analysis_timestamp": datetime.now().isoformat(),
                "schema_analysis": schema_analysis,
                "ndmo_compliance": ndmo_compliance,
                "recommendations": self._generate_schema_recommendations(schema_analysis, ndmo_compliance)
            }
            
            print("✅ Schema analysis completed successfully")
            return self.analysis_results
            
        except Exception as e:
            print(f"❌ Error analyzing schema: {str(e)}")
            return {"error": str(e)}
    
    def _find_schema_sheet(self, sheet_names: List[str]) -> Optional[str]:
        """Find the schema sheet by name patterns"""
        schema_patterns = ['schema', 'structure', 'definition', 'metadata', 'template']
        
        for sheet_name in sheet_names:
            if any(pattern in sheet_name.lower() for pattern in schema_patterns):
                return sheet_name
        
        return None
    
    def _analyze_schema_structure(self, schema_df: pd.DataFrame, sheet_name: str) -> Dict[str, Any]:
        """Analyze the structure of the schema"""
        print(f"🔍 Analyzing schema structure for sheet: {sheet_name}")
        
        # Check if this is a schema definition (columns are in rows, not columns)
        is_schema_definition = self._is_schema_definition(schema_df)
        
        if is_schema_definition:
            # Schema definition format: each row represents a column
            return self._analyze_schema_definition_format(schema_df, sheet_name)
        else:
            # Regular data format: each column represents a column
            return self._analyze_regular_data_format(schema_df, sheet_name)
    
    def _is_schema_definition(self, schema_df: pd.DataFrame) -> bool:
        """Check if the data is in schema definition format"""
        # Look for common schema definition patterns
        if 'COLUMN_NAME' in schema_df.columns or 'column_name' in schema_df.columns:
            return True
        if 'DATA_TYPE' in schema_df.columns or 'data_type' in schema_df.columns:
            return True
        if 'TABLE_NAME' in schema_df.columns or 'table_name' in schema_df.columns:
            return True
        return False
    
    def _analyze_schema_definition_format(self, schema_df: pd.DataFrame, sheet_name: str) -> Dict[str, Any]:
        """Analyze schema in definition format (each row is a column)"""
        analysis = {
            "sheet_name": sheet_name,
            "total_rows": len(schema_df),
            "total_columns": len(schema_df),
            "columns": [],
            "business_rules": [],
            "relationships": [],
            "data_types": {},
            "constraints": {},
            "quality_metrics": {}
        }
        
        # Analyze each row as a column definition
        for index, row in schema_df.iterrows():
            column_analysis = self._analyze_schema_row(row, index)
            analysis["columns"].append(column_analysis)
            analysis["data_types"][column_analysis["name"]] = column_analysis["data_type"]
            analysis["constraints"][column_analysis["name"]] = column_analysis["constraints"]
        
        # Analyze business rules
        analysis["business_rules"] = self._extract_business_rules_from_schema(schema_df)
        
        # Analyze relationships
        analysis["relationships"] = self._analyze_relationships_from_schema(schema_df)
        
        # Calculate quality metrics
        analysis["quality_metrics"] = self._calculate_schema_quality_metrics(analysis)
        
        return analysis
    
    def _analyze_regular_data_format(self, schema_df: pd.DataFrame, sheet_name: str) -> Dict[str, Any]:
        """Analyze schema in regular data format (each column is a column)"""
        analysis = {
            "sheet_name": sheet_name,
            "total_rows": len(schema_df),
            "total_columns": len(schema_df.columns),
            "columns": [],
            "business_rules": [],
            "relationships": [],
            "data_types": {},
            "constraints": {},
            "quality_metrics": {}
        }
        
        # Analyze each column
        for column in schema_df.columns:
            column_analysis = self._analyze_column(schema_df[column], column)
            analysis["columns"].append(column_analysis)
            analysis["data_types"][column] = column_analysis["data_type"]
            analysis["constraints"][column] = column_analysis["constraints"]
        
        # Analyze business rules
        analysis["business_rules"] = self._extract_business_rules(schema_df)
        
        # Analyze relationships
        analysis["relationships"] = self._analyze_relationships(schema_df)
        
        # Calculate quality metrics
        analysis["quality_metrics"] = self._calculate_schema_quality_metrics(analysis)
        
        return analysis
    
    def _analyze_schema_row(self, row: pd.Series, index: int) -> Dict[str, Any]:
        """Analyze a single row as a column definition"""
        column_analysis = {
            "name": "",
            "data_type": "unknown",
            "nullable": True,
            "unique": False,
            "primary_key": False,
            "foreign_key": False,
            "constraints": {},
            "sample_values": [],
            "statistics": {},
            "quality_issues": []
        }
        
        # Extract column name
        if 'COLUMN_NAME' in row.index:
            column_analysis["name"] = str(row['COLUMN_NAME'])
        elif 'column_name' in row.index:
            column_analysis["name"] = str(row['column_name'])
        else:
            column_analysis["name"] = f"Column_{index + 1}"
        
        # Extract data type
        if 'DATA_TYPE' in row.index:
            data_type = str(row['DATA_TYPE']).lower()
            column_analysis["data_type"] = self._map_database_type_to_standard(data_type)
        elif 'data_type' in row.index:
            data_type = str(row['data_type']).lower()
            column_analysis["data_type"] = self._map_database_type_to_standard(data_type)
        
        # Extract nullable information
        if 'IS_NULLABLE' in row.index:
            column_analysis["nullable"] = str(row['IS_NULLABLE']).upper() == 'YES'
        elif 'is_nullable' in row.index:
            column_analysis["nullable"] = str(row['is_nullable']).upper() == 'YES'
        
        # Extract constraints
        constraints = {
            "required": not column_analysis["nullable"],
            "min_length": None,
            "max_length": None,
            "min_value": None,
            "max_value": None,
            "allowed_values": [],
            "pattern": None,
            "format": None
        }
        
        # Extract character length
        if 'CHARACTER_MAXIMUM_LENGTH' in row.index and pd.notna(row['CHARACTER_MAXIMUM_LENGTH']):
            constraints["max_length"] = int(row['CHARACTER_MAXIMUM_LENGTH'])
        elif 'character_maximum_length' in row.index and pd.notna(row['character_maximum_length']):
            constraints["max_length"] = int(row['character_maximum_length'])
        
        column_analysis["constraints"] = constraints
        
        # Set sample values
        column_analysis["sample_values"] = [column_analysis["name"]]
        
        # Set statistics
        column_analysis["statistics"] = {
            "total_values": 1,
            "non_null_values": 1,
            "null_values": 0,
            "unique_values": 1,
            "duplicate_values": 0
        }
        
        return column_analysis
    
    def _map_database_type_to_standard(self, db_type: str) -> str:
        """Map database types to standard types"""
        db_type = db_type.lower()
        
        if 'int' in db_type or 'bigint' in db_type or 'smallint' in db_type:
            return 'numeric'
        elif 'float' in db_type or 'double' in db_type or 'decimal' in db_type or 'numeric' in db_type:
            return 'numeric'
        elif 'varchar' in db_type or 'char' in db_type or 'text' in db_type or 'nvarchar' in db_type:
            return 'text'
        elif 'date' in db_type or 'time' in db_type or 'datetime' in db_type or 'timestamp' in db_type:
            return 'datetime'
        elif 'bool' in db_type or 'bit' in db_type:
            return 'boolean'
        else:
            return 'text'
    
    def _extract_business_rules_from_schema(self, schema_df: pd.DataFrame) -> List[Dict[str, Any]]:
        """Extract business rules from schema definition"""
        business_rules = []
        
        # Add primary key rule if found
        if 'IS_NULLABLE' in schema_df.columns:
            non_nullable_columns = schema_df[schema_df['IS_NULLABLE'] == 'NO']
            if len(non_nullable_columns) > 0:
                business_rules.append({
                    "rule_id": "BR001",
                    "rule_name": "Required Fields",
                    "description": "Fields that cannot be null",
                    "columns": non_nullable_columns['COLUMN_NAME'].tolist() if 'COLUMN_NAME' in non_nullable_columns.columns else [],
                    "severity": "high"
                })
        
        return business_rules
    
    def _analyze_relationships_from_schema(self, schema_df: pd.DataFrame) -> List[Dict[str, Any]]:
        """Analyze relationships from schema definition"""
        relationships = []
        
        # Look for foreign key patterns in column names
        if 'COLUMN_NAME' in schema_df.columns:
            for column_name in schema_df['COLUMN_NAME']:
                if 'id' in str(column_name).lower() and str(column_name).lower() != 'id':
                    relationships.append({
                        "type": "foreign_key",
                        "source_column": str(column_name),
                        "target_table": str(column_name).replace('_id', '').replace('ID', ''),
                        "description": f"Foreign key relationship to {str(column_name).replace('_id', '').replace('ID', '')} table"
                    })
        
        return relationships
    
    def _analyze_column(self, column_data: pd.Series, column_name: str) -> Dict[str, Any]:
        """Analyze individual column"""
        column_analysis = {
            "name": column_name,
            "data_type": "unknown",
            "nullable": True,
            "unique": False,
            "primary_key": False,
            "foreign_key": False,
            "constraints": {},
            "sample_values": [],
            "statistics": {},
            "quality_issues": []
        }
        
        # Basic statistics
        non_null_data = column_data.dropna()
        column_analysis["statistics"] = {
            "total_values": len(column_data),
            "non_null_values": len(non_null_data),
            "null_values": len(column_data) - len(non_null_data),
            "unique_values": column_data.nunique(),
            "duplicate_values": len(column_data) - column_data.nunique()
        }
        
        # Sample values
        column_analysis["sample_values"] = non_null_data.head(5).tolist()
        
        # Determine data type
        column_analysis["data_type"] = self._determine_data_type(non_null_data)
        
        # Check constraints
        column_analysis["constraints"] = self._analyze_column_constraints(column_data, column_name)
        
        # Check for primary key
        if self._is_primary_key(column_name, column_data):
            column_analysis["primary_key"] = True
            column_analysis["unique"] = True
        
        # Check for foreign key
        if self._is_foreign_key(column_name, column_data):
            column_analysis["foreign_key"] = True
        
        # Check for uniqueness
        if column_data.nunique() == len(column_data):
            column_analysis["unique"] = True
        
        # Check for nullability
        if column_data.isnull().any():
            column_analysis["nullable"] = True
        else:
            column_analysis["nullable"] = False
        
        # Identify quality issues
        column_analysis["quality_issues"] = self._identify_column_quality_issues(column_analysis)
        
        return column_analysis
    
    def _determine_data_type(self, data: pd.Series) -> str:
        """Determine the data type of a column"""
        if len(data) == 0:
            return "empty"
        
        # Check for numeric data
        try:
            pd.to_numeric(data)
            return "numeric"
        except:
            pass
        
        # Check for date data
        try:
            pd.to_datetime(data)
            return "datetime"
        except:
            pass
        
        # Check for boolean data
        if data.dtype == 'bool' or all(str(val).lower() in ['true', 'false', '1', '0', 'yes', 'no'] for val in data):
            return "boolean"
        
        # Check for categorical data
        if data.nunique() < len(data) * 0.5:  # Less than 50% unique values
            return "categorical"
        
        # Check for specific formats
        sample_values = data.head(10).astype(str)
        
        # Email format
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if any(re.match(email_pattern, val) for val in sample_values):
            return "email"
        
        # Phone format
        phone_pattern = r'^[\+]?[1-9][\d]{0,15}$'
        if any(re.match(phone_pattern, re.sub(r'[^\d+]', '', val)) for val in sample_values):
            return "phone"
        
        # ID format
        if any(re.match(r'^[A-Za-z0-9_-]+$', val) for val in sample_values):
            return "identifier"
        
        return "text"
    
    def _analyze_column_constraints(self, column_data: pd.Series, column_name: str) -> Dict[str, Any]:
        """Analyze constraints for a column"""
        constraints = {
            "required": False,
            "min_length": None,
            "max_length": None,
            "min_value": None,
            "max_value": None,
            "allowed_values": None,
            "pattern": None,
            "format": None
        }
        
        non_null_data = column_data.dropna()
        if len(non_null_data) == 0:
            return constraints
        
        # Check if required (no null values)
        if not column_data.isnull().any():
            constraints["required"] = True
        
        # Length constraints for text data
        if non_null_data.dtype == 'object':
            lengths = non_null_data.astype(str).str.len()
            constraints["min_length"] = int(lengths.min())
            constraints["max_length"] = int(lengths.max())
        
        # Value constraints for numeric data
        if non_null_data.dtype in ['int64', 'float64']:
            constraints["min_value"] = float(non_null_data.min())
            constraints["max_value"] = float(non_null_data.max())
        
        # Allowed values for categorical data
        if non_null_data.nunique() <= 20:  # If less than 20 unique values
            constraints["allowed_values"] = non_null_data.unique().tolist()
        
        # Pattern constraints
        if 'email' in column_name.lower():
            constraints["pattern"] = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            constraints["format"] = "email"
        elif 'phone' in column_name.lower():
            constraints["pattern"] = r'^[\+]?[1-9][\d]{0,15}$'
            constraints["format"] = "phone"
        elif 'date' in column_name.lower():
            constraints["format"] = "date"
        
        return constraints
    
    def _is_primary_key(self, column_name: str, column_data: pd.Series) -> bool:
        """Check if column is a primary key"""
        # Check by name patterns
        pk_patterns = ['id', 'key', 'pk', 'primary', 'serial']
        if any(pattern in column_name.lower() for pattern in pk_patterns):
            # Check if unique and not null
            if column_data.nunique() == len(column_data) and not column_data.isnull().any():
                return True
        
        return False
    
    def _is_foreign_key(self, column_name: str, column_data: pd.Series) -> bool:
        """Check if column is a foreign key"""
        # Check by name patterns
        fk_patterns = ['_id', '_key', 'ref_', 'foreign']
        if any(pattern in column_name.lower() for pattern in fk_patterns):
            return True
        
        return False
    
    def _identify_column_quality_issues(self, column_analysis: Dict[str, Any]) -> List[str]:
        """Identify quality issues in a column"""
        issues = []
        
        # Check for high null percentage
        null_percentage = column_analysis["statistics"]["null_values"] / column_analysis["statistics"]["total_values"]
        if null_percentage > 0.1:  # More than 10% nulls
            issues.append(f"High null percentage: {null_percentage:.1%}")
        
        # Check for low uniqueness in ID fields
        if 'id' in column_analysis["name"].lower():
            uniqueness = column_analysis["statistics"]["unique_values"] / column_analysis["statistics"]["total_values"]
            if uniqueness < 0.95:  # Less than 95% unique
                issues.append(f"Low uniqueness in ID field: {uniqueness:.1%}")
        
        # Check for inconsistent data types
        if column_analysis["data_type"] == "unknown":
            issues.append("Unable to determine data type")
        
        return issues
    
    def _extract_business_rules(self, schema_df: pd.DataFrame) -> List[Dict[str, Any]]:
        """Extract business rules from schema"""
        business_rules = []
        
        # Look for business rules in column names or data
        for column in schema_df.columns:
            if 'rule' in column.lower() or 'constraint' in column.lower():
                # This might be a business rule column
                business_rules.append({
                    "name": column,
                    "type": "constraint",
                    "description": f"Business rule defined in column: {column}",
                    "implemented": True
                })
        
        # Add common business rules
        common_rules = [
            {
                "name": "Unique Identifiers",
                "type": "uniqueness",
                "description": "All records must have unique identifiers",
                "implemented": False
            },
            {
                "name": "Data Validation",
                "type": "validation",
                "description": "Data must pass validation rules",
                "implemented": False
            },
            {
                "name": "Referential Integrity",
                "type": "integrity",
                "description": "Foreign key relationships must be maintained",
                "implemented": False
            }
        ]
        
        business_rules.extend(common_rules)
        return business_rules
    
    def _analyze_relationships(self, schema_df: pd.DataFrame) -> List[Dict[str, Any]]:
        """Analyze relationships between columns"""
        relationships = []
        
        # Look for foreign key relationships
        for column in schema_df.columns:
            if self._is_foreign_key(column, schema_df[column]):
                # Find potential parent table
                parent_table = column.replace('_id', '').replace('_key', '')
                relationships.append({
                    "type": "foreign_key",
                    "child_column": column,
                    "parent_table": parent_table,
                    "relationship_type": "many_to_one"
                })
        
        return relationships
    
    def _calculate_schema_quality_metrics(self, schema_analysis: Dict[str, Any]) -> Dict[str, float]:
        """Calculate quality metrics for the schema"""
        metrics = {
            "completeness": 0.0,
            "consistency": 0.0,
            "uniqueness": 0.0,
            "validity": 0.0,
            "overall_score": 0.0
        }
        
        columns = schema_analysis["columns"]
        if not columns:
            return metrics
        
        # Completeness: percentage of columns with proper definitions
        complete_columns = sum(1 for col in columns if col["data_type"] != "unknown")
        metrics["completeness"] = complete_columns / len(columns)
        
        # Consistency: percentage of columns with consistent naming
        consistent_columns = sum(1 for col in columns if self._is_consistent_naming(col["name"]))
        metrics["consistency"] = consistent_columns / len(columns)
        
        # Uniqueness: percentage of columns with proper uniqueness constraints
        unique_columns = sum(1 for col in columns if col["unique"] or col["primary_key"])
        metrics["uniqueness"] = unique_columns / len(columns)
        
        # Validity: percentage of columns with proper constraints
        valid_columns = sum(1 for col in columns if col["constraints"])
        metrics["validity"] = valid_columns / len(columns)
        
        # Overall score
        metrics["overall_score"] = np.mean(list(metrics.values()))
        
        return metrics
    
    def _is_consistent_naming(self, column_name: str) -> bool:
        """Check if column naming is consistent"""
        # Check for consistent naming patterns
        if re.match(r'^[a-z][a-z0-9_]*$', column_name.lower()):
            return True
        return False
    
    def _generate_schema_recommendations(self, schema_analysis: Dict[str, Any], ndmo_compliance: Dict[str, Any]) -> List[str]:
        """Generate recommendations for schema improvement"""
        recommendations = []
        
        # NDMO compliance recommendations
        if ndmo_compliance["status"] != "compliant":
            recommendations.extend(ndmo_compliance["recommendations"])
        
        # Schema-specific recommendations
        columns = schema_analysis["columns"]
        
        # Check for missing primary keys
        has_primary_key = any(col["primary_key"] for col in columns)
        if not has_primary_key:
            recommendations.append("Add a primary key column to ensure data uniqueness")
        
        # Check for inconsistent data types
        unknown_types = sum(1 for col in columns if col["data_type"] == "unknown")
        if unknown_types > 0:
            recommendations.append(f"Define data types for {unknown_types} columns with unknown types")
        
        # Check for missing constraints
        columns_without_constraints = sum(1 for col in columns if not col["constraints"])
        if columns_without_constraints > 0:
            recommendations.append(f"Add constraints for {columns_without_constraints} columns without constraints")
        
        return recommendations
    
    def auto_correct_schema(self, schema_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Auto-correct schema issues"""
        print("🔧 Starting schema auto-correction...")
        
        corrected_schema = schema_analysis.copy()
        corrections_made = []
        
        # Correct data types
        for column in corrected_schema["columns"]:
            if column["data_type"] == "unknown":
                # Try to infer data type from sample values
                inferred_type = self._infer_data_type_from_samples(column["sample_values"])
                if inferred_type != "unknown":
                    column["data_type"] = inferred_type
                    corrections_made.append(f"Corrected data type for {column['name']} to {inferred_type}")
        
        # Add missing primary key
        has_primary_key = any(col["primary_key"] for col in corrected_schema["columns"])
        if not has_primary_key:
            # Find the best candidate for primary key
            pk_candidate = self._find_primary_key_candidate(corrected_schema["columns"])
            if pk_candidate:
                pk_candidate["primary_key"] = True
                pk_candidate["unique"] = True
                corrections_made.append(f"Set {pk_candidate['name']} as primary key")
        
        # Add missing constraints
        for column in corrected_schema["columns"]:
            if not column["constraints"]:
                # Add basic constraints based on data type
                constraints = self._generate_basic_constraints(column)
                if constraints:
                    column["constraints"] = constraints
                    corrections_made.append(f"Added constraints for {column['name']}")
        
        # Log corrections
        self.correction_log.extend(corrections_made)
        
        print(f"✅ Schema auto-correction completed. {len(corrections_made)} corrections made.")
        
        return corrected_schema
    
    def _infer_data_type_from_samples(self, sample_values: List[Any]) -> str:
        """Infer data type from sample values"""
        if not sample_values:
            return "unknown"
        
        # Check for numeric
        try:
            [float(val) for val in sample_values]
            return "numeric"
        except:
            pass
        
        # Check for date
        try:
            [pd.to_datetime(val) for val in sample_values]
            return "datetime"
        except:
            pass
        
        # Check for boolean
        if all(str(val).lower() in ['true', 'false', '1', '0', 'yes', 'no'] for val in sample_values):
            return "boolean"
        
        return "text"
    
    def _find_primary_key_candidate(self, columns: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Find the best candidate for primary key"""
        candidates = []
        
        for column in columns:
            score = 0
            
            # Check name patterns
            if 'id' in column["name"].lower():
                score += 3
            if 'key' in column["name"].lower():
                score += 2
            if 'serial' in column["name"].lower():
                score += 2
            
            # Check uniqueness
            if column["unique"]:
                score += 2
            
            # Check data type
            if column["data_type"] in ["numeric", "identifier"]:
                score += 1
            
            if score > 0:
                candidates.append((column, score))
        
        if candidates:
            # Return the column with highest score
            candidates.sort(key=lambda x: x[1], reverse=True)
            return candidates[0][0]
        
        return None
    
    def _generate_basic_constraints(self, column: Dict[str, Any]) -> Dict[str, Any]:
        """Generate basic constraints for a column"""
        constraints = {}
        
        # Required constraint
        if not column["nullable"]:
            constraints["required"] = True
        
        # Length constraints for text
        if column["data_type"] == "text":
            if column["sample_values"]:
                lengths = [len(str(val)) for val in column["sample_values"]]
                constraints["min_length"] = min(lengths)
                constraints["max_length"] = max(lengths)
        
        # Value constraints for numeric
        if column["data_type"] == "numeric":
            if column["sample_values"]:
                try:
                    values = [float(val) for val in column["sample_values"]]
                    constraints["min_value"] = min(values)
                    constraints["max_value"] = max(values)
                except:
                    pass
        
        return constraints
    
    def export_analysis_results(self, filepath: str = None) -> str:
        """Export analysis results to JSON file"""
        if not filepath:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = f"schema_analysis_{timestamp}.json"
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.analysis_results, f, indent=2, ensure_ascii=False, default=str)
            
            print(f"✅ Analysis results exported to: {filepath}")
            return filepath
        except Exception as e:
            print(f"❌ Error exporting results: {str(e)}")
            return None

def main():
    """Test the smart schema analyzer"""
    analyzer = SmartSchemaAnalyzer()
    
    # Test with a sample file
    test_file = "schema.xlsx"  # Replace with actual file path
    
    try:
        results = analyzer.analyze_schema_file(test_file)
        
        if "error" not in results:
            print("\n📊 Analysis Results:")
            print(f"Schema Sheet: {results['schema_sheet']}")
            print(f"Total Columns: {results['schema_analysis']['total_columns']}")
            print(f"NDMO Compliance: {results['ndmo_compliance']['overall_score']:.1%}")
            print(f"Status: {results['ndmo_compliance']['status']}")
            
            # Export results
            export_file = analyzer.export_analysis_results()
            if export_file:
                print(f"Results saved to: {export_file}")
        else:
            print(f"Analysis failed: {results['error']}")
            
    except Exception as e:
        print(f"Test failed: {str(e)}")

if __name__ == "__main__":
    main()



