#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart Data Processor
Intelligent data processing with schema validation and quality improvement

Developer: AI Assistant
Purpose: Process data files according to schema standards and improve quality
"""

import pandas as pd
import numpy as np
from datetime import datetime
import json
import re
from typing import Dict, List, Any, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

from ndmo_standards import NDMOStandardsManager
from smart_schema_analyzer import SmartSchemaAnalyzer

class SmartDataProcessor:
    """Smart data processor with schema validation and quality improvement"""
    
    def __init__(self):
        """Initialize the smart data processor"""
        self.ndmo_manager = NDMOStandardsManager()
        self.schema_analyzer = SmartSchemaAnalyzer()
        self.processing_results = {}
        self.quality_metrics = {}
        self.improvement_log = []
    
    def process_data_file(self, data_file_path: str, schema_file_path: str = None) -> Dict[str, Any]:
        """Process data file according to schema standards"""
        print(f"🔄 Processing data file: {data_file_path}")
        
        try:
            # Load data file
            data_df = pd.read_excel(data_file_path)
            print(f"📊 Loaded data: {len(data_df)} rows, {len(data_df.columns)} columns")
            
            # Analyze schema if provided
            schema_analysis = None
            if schema_file_path:
                schema_analysis = self.schema_analyzer.analyze_schema_file(schema_file_path)
                print(f"📋 Schema analysis completed")
            
            # Process data according to schema
            processed_data = self._process_data_according_to_schema(data_df, schema_analysis)
            
            # Calculate quality metrics
            quality_metrics = self._calculate_quality_metrics(processed_data, schema_analysis)
            
            # Apply quality improvements
            improved_data = self._apply_quality_improvements(processed_data, quality_metrics)
            
            # Final quality assessment
            final_quality = self._calculate_quality_metrics(improved_data, schema_analysis)
            
            # Store results
            self.processing_results = {
                "data_file_path": data_file_path,
                "schema_file_path": schema_file_path,
                "processing_timestamp": datetime.now().isoformat(),
                "original_data": {
                    "rows": len(data_df),
                    "columns": len(data_df.columns),
                    "quality_metrics": quality_metrics
                },
                "processed_data": {
                    "rows": len(processed_data),
                    "columns": len(processed_data.columns),
                    "quality_metrics": final_quality
                },
                "improvements_applied": self.improvement_log,
                "schema_compliance": self._assess_schema_compliance(improved_data, schema_analysis),
                "ndmo_compliance": self._assess_ndmo_compliance(improved_data)
            }
            
            print("✅ Data processing completed successfully")
            return self.processing_results
            
        except Exception as e:
            print(f"❌ Error processing data: {str(e)}")
            return {"error": str(e)}
    
    def _process_data_according_to_schema(self, data_df: pd.DataFrame, schema_analysis: Dict[str, Any]) -> pd.DataFrame:
        """Process data according to schema requirements"""
        print("🔧 Processing data according to schema...")
        
        processed_df = data_df.copy()
        
        if not schema_analysis or "schema_analysis" not in schema_analysis:
            print("⚠️ No schema analysis provided, applying basic processing")
            return self._apply_basic_processing(processed_df)
        
        schema_info = schema_analysis["schema_analysis"]
        columns_info = schema_info.get("columns", [])
        
        # Process each column according to schema
        for column_info in columns_info:
            column_name = column_info["name"]
            if column_name in processed_df.columns:
                processed_df[column_name] = self._process_column_according_to_schema(
                    processed_df[column_name], column_info
                )
        
        return processed_df
    
    def _process_column_according_to_schema(self, column_data: pd.Series, column_info: Dict[str, Any]) -> pd.Series:
        """Process individual column according to schema"""
        try:
            column_name = column_info.get("name", "unknown")
            processed_column = column_data.copy()
            
            # Apply data type conversion
            target_data_type = column_info.get("data_type", "unknown")
            if target_data_type != "unknown":
                processed_column = self._convert_to_target_type(processed_column, target_data_type)
            
            # Apply constraints
            constraints = column_info.get("constraints", {})
            processed_column = self._apply_constraints(processed_column, constraints)
            
            # Apply business rules
            if column_info.get("primary_key", False):
                processed_column = self._ensure_primary_key_uniqueness(processed_column)
            
            return processed_column
        except Exception as e:
            print(f"⚠️ Error processing column {column_name}: {str(e)}")
            return column_data
    
    def _convert_to_target_type(self, column_data: pd.Series, target_type: str) -> pd.Series:
        """Convert column to target data type"""
        try:
            if target_type == "numeric":
                return pd.to_numeric(column_data, errors='coerce')
            elif target_type == "datetime":
                return pd.to_datetime(column_data, errors='coerce')
            elif target_type == "boolean":
                return column_data.astype('bool')
            elif target_type == "text":
                return column_data.astype(str)
            else:
                return column_data
        except Exception as e:
            print(f"⚠️ Error converting column to {target_type}: {str(e)}")
            return column_data
    
    def _apply_constraints(self, column_data: pd.Series, constraints: Dict[str, Any]) -> pd.Series:
        """Apply constraints to column data"""
        try:
            processed_column = column_data.copy()
            
            # Apply required constraint
            if constraints.get("required", False):
                # Fill null values with appropriate defaults
                if processed_column.dtype == 'object':
                    processed_column = processed_column.fillna("N/A")
                elif processed_column.dtype in ['int64', 'float64']:
                    processed_column = processed_column.fillna(0)
        except Exception as e:
            print(f"⚠️ Error in constraint application: {str(e)}")
            return column_data
        
        # Apply length constraints
        if constraints.get("min_length") is not None or constraints.get("max_length") is not None:
            if processed_column.dtype == 'object':
                min_len = constraints.get("min_length", 0)
                max_len = constraints.get("max_length", float('inf'))
                
                # Handle None values properly
                if min_len is None:
                    min_len = 0
                if max_len is None:
                    max_len = float('inf')
                
                processed_column = processed_column.apply(
                    lambda x: str(x)[:int(max_len)] if len(str(x)) > max_len else str(x).ljust(int(min_len)) if len(str(x)) < min_len else str(x)
                )
        
        # Apply value constraints
        if constraints.get("min_value") is not None or constraints.get("max_value") is not None:
            if processed_column.dtype in ['int64', 'float64']:
                min_val = constraints.get("min_value")
                max_val = constraints.get("max_value")
                
                # Handle None values properly
                if min_val is not None and max_val is not None:
                    processed_column = processed_column.clip(lower=min_val, upper=max_val)
                elif min_val is not None:
                    processed_column = processed_column.clip(lower=min_val)
                elif max_val is not None:
                    processed_column = processed_column.clip(upper=max_val)
        
        # Apply allowed values constraint
        if constraints.get("allowed_values"):
            allowed_values = constraints["allowed_values"]
            processed_column = processed_column.apply(
                lambda x: x if x in allowed_values else None
            )
        
        return processed_column
    
    def _ensure_primary_key_uniqueness(self, column_data: pd.Series) -> pd.Series:
        """Ensure primary key uniqueness"""
        processed_column = column_data.copy()
        
        # Handle duplicates
        if processed_column.duplicated().any():
            # Generate unique values for duplicates
            duplicates = processed_column.duplicated(keep=False)
            unique_counter = 1
            
            for idx in processed_column[duplicates].index:
                original_value = processed_column.iloc[idx]
                processed_column.iloc[idx] = f"{original_value}_{unique_counter}"
                unique_counter += 1
        
        return processed_column
    
    def _apply_basic_processing(self, data_df: pd.DataFrame) -> pd.DataFrame:
        """Apply basic data processing when no schema is provided"""
        print("🔧 Applying basic data processing...")
        
        processed_df = data_df.copy()
        
        # Clean column names
        processed_df.columns = [self._clean_column_name(col) for col in processed_df.columns]
        
        # Handle missing values
        for column in processed_df.columns:
            if processed_df[column].dtype == 'object':
                processed_df[column] = processed_df[column].fillna("N/A")
            elif processed_df[column].dtype in ['int64', 'float64']:
                processed_df[column] = processed_df[column].fillna(0)
        
        # Remove completely empty rows
        processed_df = processed_df.dropna(how='all')
        
        return processed_df
    
    def _clean_column_name(self, column_name: str) -> str:
        """Clean column name"""
        # Remove special characters and spaces
        cleaned = re.sub(r'[^\w\s]', '', str(column_name))
        cleaned = re.sub(r'\s+', '_', cleaned)
        return cleaned.lower()
    
    def _calculate_quality_metrics(self, data_df: pd.DataFrame, schema_analysis: Dict[str, Any] = None) -> Dict[str, Any]:
        """Calculate comprehensive quality metrics"""
        print("📊 Calculating quality metrics...")
        
        metrics = {
            "completeness": {},
            "accuracy": {},
            "consistency": {},
            "uniqueness": {},
            "validity": {},
            "overall_score": 0.0
        }
        
        # Calculate metrics for each column
        for column in data_df.columns:
            column_data = data_df[column]
            
            # Completeness
            null_count = column_data.isnull().sum()
            total_count = len(column_data)
            metrics["completeness"][column] = (total_count - null_count) / total_count if total_count > 0 else 0
            
            # Uniqueness
            unique_count = column_data.nunique()
            metrics["uniqueness"][column] = unique_count / total_count if total_count > 0 else 0
            
            # Validity (basic checks)
            if column_data.dtype == 'object':
                # Check for empty strings
                empty_count = (column_data == '').sum()
                metrics["validity"][column] = (total_count - empty_count) / total_count if total_count > 0 else 0
            else:
                # For numeric columns, check for infinite values
                inf_count = np.isinf(column_data).sum()
                metrics["validity"][column] = (total_count - inf_count) / total_count if total_count > 0 else 0
        
        # Calculate overall scores
        for metric_type in ["completeness", "uniqueness", "validity"]:
            if metrics[metric_type]:
                metrics[metric_type]["overall"] = np.mean(list(metrics[metric_type].values()))
        
        # Overall quality score
        overall_scores = [metrics[metric]["overall"] for metric in ["completeness", "uniqueness", "validity"] if "overall" in metrics[metric]]
        metrics["overall_score"] = np.mean(overall_scores) if overall_scores else 0.0
        
        return metrics
    
    def _apply_quality_improvements(self, data_df: pd.DataFrame, quality_metrics: Dict[str, Any]) -> pd.DataFrame:
        """Apply quality improvements based on metrics"""
        print("🔧 Applying quality improvements...")
        
        improved_df = data_df.copy()
        
        # Improve completeness
        improved_df = self._improve_completeness(improved_df, quality_metrics["completeness"])
        
        # Improve validity
        improved_df = self._improve_validity(improved_df, quality_metrics["validity"])
        
        # Improve consistency
        improved_df = self._improve_consistency(improved_df)
        
        return improved_df
    
    def _improve_completeness(self, data_df: pd.DataFrame, completeness_metrics: Dict[str, float]) -> pd.DataFrame:
        """Improve data completeness"""
        improved_df = data_df.copy()
        
        for column, completeness_score in completeness_metrics.items():
            if column == "overall":
                continue
                
            if completeness_score < 0.95:  # Less than 95% complete
                column_data = improved_df[column]
                null_count = column_data.isnull().sum()
                
                if null_count > 0:
                    # Fill missing values intelligently
                    if column_data.dtype == 'object':
                        # Use most frequent value
                        most_frequent = column_data.mode()
                        if len(most_frequent) > 0:
                            improved_df[column] = column_data.fillna(most_frequent[0])
                        else:
                            improved_df[column] = column_data.fillna("Unknown")
                    elif column_data.dtype in ['int64', 'float64']:
                        # Use median value
                        median_value = column_data.median()
                        improved_df[column] = column_data.fillna(median_value)
                    
                    self.improvement_log.append(f"Improved completeness for {column}: filled {null_count} missing values")
        
        return improved_df
    
    def _improve_validity(self, data_df: pd.DataFrame, validity_metrics: Dict[str, float]) -> pd.DataFrame:
        """Improve data validity"""
        improved_df = data_df.copy()
        
        for column, validity_score in validity_metrics.items():
            if column == "overall":
                continue
                
            if validity_score < 0.95:  # Less than 95% valid
                column_data = improved_df[column]
                
                if column_data.dtype == 'object':
                    # Remove empty strings
                    empty_mask = (column_data == '') | (column_data.isnull())
                    if empty_mask.any():
                        improved_df.loc[empty_mask, column] = "N/A"
                        self.improvement_log.append(f"Improved validity for {column}: replaced empty strings")
                
                elif column_data.dtype in ['int64', 'float64']:
                    # Handle infinite values
                    inf_mask = np.isinf(column_data)
                    if inf_mask.any():
                        median_value = column_data[~inf_mask].median()
                        improved_df.loc[inf_mask, column] = median_value
                        self.improvement_log.append(f"Improved validity for {column}: replaced infinite values")
        
        return improved_df
    
    def _improve_consistency(self, data_df: pd.DataFrame) -> pd.DataFrame:
        """Improve data consistency"""
        improved_df = data_df.copy()
        
        # Standardize text columns
        for column in improved_df.columns:
            if improved_df[column].dtype == 'object':
                # Remove extra whitespace
                improved_df[column] = improved_df[column].astype(str).str.strip()
                
                # Standardize case for categorical data
                if improved_df[column].nunique() < 50:  # Likely categorical
                    improved_df[column] = improved_df[column].str.title()
        
        return improved_df
    
    def _assess_schema_compliance(self, data_df: pd.DataFrame, schema_analysis: Dict[str, Any] = None) -> Dict[str, Any]:
        """Assess compliance with schema requirements"""
        if not schema_analysis:
            return {"status": "no_schema", "score": 0.0}
        
        schema_info = schema_analysis["schema_analysis"]
        columns_info = schema_info.get("columns", [])
        
        compliance_score = 0.0
        total_checks = 0
        
        for column_info in columns_info:
            column_name = column_info["name"]
            if column_name in data_df.columns:
                # Check data type compliance
                expected_type = column_info.get("data_type", "unknown")
                actual_type = self._get_actual_data_type(data_df[column_name])
                
                if expected_type == actual_type or expected_type == "unknown":
                    compliance_score += 1
                total_checks += 1
        
        final_score = compliance_score / total_checks if total_checks > 0 else 0.0
        
        return {
            "status": "compliant" if final_score >= 0.8 else "non_compliant",
            "score": final_score,
            "checks_performed": total_checks
        }
    
    def _get_actual_data_type(self, column_data: pd.Series) -> str:
        """Get actual data type of a column"""
        if column_data.dtype in ['int64', 'float64']:
            return "numeric"
        elif column_data.dtype == 'bool':
            return "boolean"
        elif column_data.dtype == 'object':
            # Try to detect more specific types
            try:
                pd.to_datetime(column_data.head(10))
                return "datetime"
            except:
                return "text"
        else:
            return "unknown"
    
    def _assess_ndmo_compliance(self, data_df: pd.DataFrame) -> Dict[str, Any]:
        """Assess NDMO compliance"""
        # Calculate basic NDMO metrics
        results = {}
        
        # Data completeness
        completeness = data_df.notnull().sum().sum() / (len(data_df) * len(data_df.columns))
        results["DQ001"] = completeness  # Data Completeness
        
        # Data uniqueness (check for primary key)
        has_unique_column = any(data_df[col].nunique() == len(data_df) for col in data_df.columns)
        results["DG001"] = 1.0 if has_unique_column else 0.0  # Unique Identifiers
        
        # Data validity (basic check)
        validity_scores = []
        for column in data_df.columns:
            if data_df[column].dtype == 'object':
                valid_count = (data_df[column] != '').sum()
            else:
                valid_count = (~np.isinf(data_df[column])).sum()
            validity_scores.append(valid_count / len(data_df))
        
        results["DQ005"] = np.mean(validity_scores) if validity_scores else 0.0  # Data Validity
        
        # Calculate overall compliance
        compliance = self.ndmo_manager.calculate_compliance_score(results)
        
        return compliance
    
    def export_processed_data(self, data_df: pd.DataFrame, filepath: str = None) -> str:
        """Export processed data to Excel file"""
        if not filepath:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = f"processed_data_{timestamp}.xlsx"
        
        try:
            data_df.to_excel(filepath, index=False)
            print(f"✅ Processed data exported to: {filepath}")
            return filepath
        except Exception as e:
            print(f"❌ Error exporting data: {str(e)}")
            return None
    
    def export_processing_results(self, filepath: str = None) -> str:
        """Export processing results to JSON file"""
        if not filepath:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = f"processing_results_{timestamp}.json"
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.processing_results, f, indent=2, ensure_ascii=False, default=str)
            
            print(f"✅ Processing results exported to: {filepath}")
            return filepath
        except Exception as e:
            print(f"❌ Error exporting results: {str(e)}")
            return None

def main():
    """Test the smart data processor"""
    processor = SmartDataProcessor()
    
    # Test with sample files
    data_file = "Billing August.xlsx"  # Replace with actual file path
    schema_file = "schema.xlsx"  # Replace with actual file path
    
    try:
        results = processor.process_data_file(data_file, schema_file)
        
        if "error" not in results:
            print("\n📊 Processing Results:")
            print(f"Original Rows: {results['original_data']['rows']}")
            print(f"Processed Rows: {results['processed_data']['rows']}")
            print(f"Quality Improvement: {results['processed_data']['quality_metrics']['overall_score']:.1%}")
            print(f"NDMO Compliance: {results['ndmo_compliance']['overall_score']:.1%}")
            
            # Export results
            export_file = processor.export_processing_results()
            if export_file:
                print(f"Results saved to: {export_file}")
        else:
            print(f"Processing failed: {results['error']}")
            
    except Exception as e:
        print(f"Test failed: {str(e)}")

if __name__ == "__main__":
    main()



