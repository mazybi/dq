#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML Technical Report Generator
Professional HTML report generator for NDMO compliance and data quality analysis

Developer: AI Assistant
Purpose: Generate professional HTML reports with logo, charts, and organized data
"""

import os
import base64
from datetime import datetime
from typing import Dict, List, Any, Optional
import json
import pandas as pd
import numpy as np

class HTMLReportGenerator:
    """Professional HTML report generator for technical reports"""
    
    def __init__(self):
        """Initialize the HTML report generator"""
        self.logo_path = "assets/logo@3x.png"
        self.reports_dir = "reports/html_reports"
        self.ensure_directories()
    
    def ensure_directories(self):
        """Ensure required directories exist"""
        os.makedirs(self.reports_dir, exist_ok=True)
        os.makedirs("assets", exist_ok=True)
    
    def encode_logo(self) -> str:
        """Encode logo to base64 for embedding in HTML"""
        try:
            if os.path.exists(self.logo_path):
                with open(self.logo_path, "rb") as logo_file:
                    logo_data = base64.b64encode(logo_file.read()).decode('utf-8')
                    return f"data:image/png;base64,{logo_data}"
            else:
                # Return a placeholder if logo doesn't exist
                return self._create_placeholder_logo()
        except Exception as e:
            print(f"Warning: Could not load logo: {e}")
            return self._create_placeholder_logo()
    
    def _create_placeholder_logo(self) -> str:
        """Create a placeholder logo as SVG"""
        svg_logo = """
        <svg width="200" height="60" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
                </linearGradient>
            </defs>
            <rect width="200" height="60" fill="url(#grad1)" rx="10"/>
            <text x="100" y="35" font-family="Arial, sans-serif" font-size="16" font-weight="bold" 
                  text-anchor="middle" fill="white">SANS Data Quality</text>
        </svg>
        """
        return f"data:image/svg+xml;base64,{base64.b64encode(svg_logo.encode()).decode()}"
    
    def generate_technical_report_html(self, schema_analysis: Dict[str, Any], 
                                     data_quality_metrics: Dict[str, Any] = None,
                                     processing_results: Dict[str, Any] = None) -> str:
        """Generate comprehensive technical report in HTML format"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"technical_report_{timestamp}.html"
        filepath = os.path.join(self.reports_dir, filename)
        
        # Extract data from analysis
        compliance = schema_analysis.get("ndmo_compliance", {})
        schema_info = schema_analysis.get("schema_analysis", {})
        columns = schema_info.get("columns", [])
        
        # Generate HTML content
        html_content = self._create_html_template(
            compliance, schema_info, columns, data_quality_metrics, processing_results
        )
        
        # Save to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTML Technical Report generated: {filename}")
        return filepath
    
    def _create_html_template(self, compliance: Dict[str, Any], schema_info: Dict[str, Any], 
                            columns: List[Dict[str, Any]], data_quality_metrics: Dict[str, Any] = None,
                            processing_results: Dict[str, Any] = None) -> str:
        """Create the complete HTML template"""
        
        logo_data = self.encode_logo()
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NDMO Technical Compliance Report</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        {self._get_css_styles()}
    </style>
</head>
<body>
    {self._create_header(logo_data)}
    {self._create_executive_summary(compliance, schema_info)}
    {self._create_compliance_overview(compliance)}
    {self._create_schema_analysis(schema_info, columns)}
    {self._create_data_quality_section(data_quality_metrics)}
    {self._create_processing_results(processing_results)}
    {self._create_recommendations(compliance, columns)}
    {self._create_implementation_guide(columns)}
    {self._create_footer()}
    
    <script>
        {self._get_javascript()}
    </script>
</body>
</html>
"""
        return html_content
    
    def _get_css_styles(self) -> str:
        """Get CSS styles for the report"""
        return """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Header Styles */
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            color: white;
            padding: 40px 20px;
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            position: relative;
            overflow: hidden;
        }
        
        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            opacity: 0.3;
        }
        
        .header-content {
            position: relative;
            z-index: 2;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
        }
        
        .logo-section {
            display: flex;
            align-items: center;
            gap: 20px;
        }
        
        .logo {
            width: 80px;
            height: 80px;
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        
        .header-text h1 {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header-text p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .report-info {
            text-align: left;
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        
        /* Section Styles */
        .section {
            background: white;
            margin-bottom: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        
        .section-header {
            background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
            color: white;
            padding: 25px 30px;
            font-size: 1.5rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .section-content {
            padding: 30px;
        }
        
        /* Summary Cards */
        .summary-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        
        .summary-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .summary-card:hover {
            transform: translateY(-5px);
        }
        
        .summary-card h3 {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 10px;
        }
        
        .summary-card p {
            font-size: 1.1rem;
            opacity: 0.9;
        }
        
        /* Compliance Status */
        .compliance-status {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
        }
        
        .status-compliant {
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            color: white;
        }
        
        .status-partial {
            background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
            color: white;
        }
        
        .status-non-compliant {
            background: linear-gradient(135deg, #F44336 0%, #D32F2F 100%);
            color: white;
        }
        
        /* Charts Container */
        .charts-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
            margin: 30px 0;
        }
        
        .chart-container {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        /* Tables */
        .data-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .data-table th {
            background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
            color: white;
            padding: 20px;
            text-align: right;
            font-weight: 600;
        }
        
        .data-table td {
            padding: 15px 20px;
            border-bottom: 1px solid #eee;
        }
        
        .data-table tr:hover {
            background: #f8f9fa;
        }
        
        /* Progress Bars */
        .progress-container {
            margin: 20px 0;
        }
        
        .progress-bar {
            width: 100%;
            height: 25px;
            background: #e0e0e0;
            border-radius: 15px;
            overflow: hidden;
            margin: 10px 0;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            border-radius: 15px;
            transition: width 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
        }
        
        /* Code Blocks */
        .code-block {
            background: #2d3748;
            color: #e2e8f0;
            padding: 25px;
            border-radius: 15px;
            font-family: 'Courier New', monospace;
            overflow-x: auto;
            margin: 20px 0;
        }
        
        /* Recommendations */
        .recommendation {
            background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
            border-right: 5px solid #2196F3;
            padding: 25px;
            margin: 20px 0;
            border-radius: 15px;
        }
        
        .recommendation h4 {
            color: #1976D2;
            margin-bottom: 15px;
            font-size: 1.2rem;
        }
        
        /* Footer */
        .footer {
            background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
            color: white;
            text-align: center;
            padding: 30px;
            border-radius: 20px;
            margin-top: 40px;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                text-align: center;
            }
            
            .summary-grid {
                grid-template-columns: 1fr;
            }
            
            .charts-container {
                grid-template-columns: 1fr;
            }
            
            .header-text h1 {
                font-size: 2rem;
            }
        }
        
        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .section {
            animation: fadeInUp 0.6s ease-out;
        }
        
        /* Print Styles */
        @media print {
            body {
                background: white;
            }
            
            .section {
                box-shadow: none;
                border: 1px solid #ddd;
            }
            
            .header {
                background: #2E86AB !important;
                -webkit-print-color-adjust: exact;
            }
        }
        """
    
    def _create_header(self, logo_data: str) -> str:
        """Create the header section"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""
        <div class="header">
            <div class="header-content">
                <div class="logo-section">
                    <img src="{logo_data}" alt="SANS Logo" class="logo">
                    <div class="header-text">
                        <h1>🛡️ Technical Compliance Report</h1>
                        <p>Data Quality Management System - NDMO Standards</p>
                    </div>
                </div>
                <div class="report-info">
                    <h3>📊 Report Information</h3>
                    <p><strong>Generated:</strong> {current_time}</p>
                    <p><strong>Type:</strong> Comprehensive Technical Report</p>
                    <p><strong>Version:</strong> 2.0</p>
                </div>
            </div>
        </div>
        """
    
    def _create_executive_summary(self, compliance: Dict[str, Any], schema_info: Dict[str, Any]) -> str:
        """Create executive summary section"""
        overall_score = compliance.get('overall_score', 0) * 100
        total_columns = len(schema_info.get('columns', []))
        
        status_class = "status-compliant" if overall_score >= 80 else "status-partial" if overall_score >= 50 else "status-non-compliant"
        status_text = "Compliant" if overall_score >= 80 else "Partially Compliant" if overall_score >= 50 else "Non-Compliant"
        status_icon = "✅" if overall_score >= 80 else "⚠️" if overall_score >= 50 else "❌"
        
        return f"""
        <div class="section">
            <div class="section-header">
                <span>📈</span>
                <span>Executive Summary</span>
            </div>
            <div class="section-content">
                <div class="summary-grid">
                    <div class="summary-card">
                        <h3>{overall_score:.1f}%</h3>
                        <p>Overall Compliance</p>
                    </div>
                    <div class="summary-card">
                        <h3>{total_columns}</h3>
                        <p>Total Columns</p>
                    </div>
                    <div class="summary-card">
                        <h3>{len([col for col in schema_info.get('columns', []) if col.get('primary_key', False)])}</h3>
                        <p>Primary Keys</p>
                    </div>
                    <div class="summary-card">
                        <h3>{len([col for col in schema_info.get('columns', []) if col.get('required', False)])}</h3>
                        <p>Required Fields</p>
                    </div>
                </div>
                
                <div class="compliance-status {status_class}">
                    <span style="font-size: 2rem;">{status_icon}</span>
                    <div>
                        <h3>Compliance Status: {status_text}</h3>
                        <p>Current Compliance Rate: {overall_score:.1f}%</p>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _create_compliance_overview(self, compliance: Dict[str, Any]) -> str:
        """Create compliance overview section"""
        categories = {
            'data_governance': 'Data Governance',
            'data_quality': 'Data Quality', 
            'data_security': 'Data Security',
            'data_architecture': 'Data Architecture',
            'business_rules': 'Business Rules'
        }
        
        compliance_html = ""
        for key, label in categories.items():
            score = compliance.get(key, {}).get('score', 0) * 100
            compliance_html += f"""
            <div class="progress-container">
                <h4>{label}</h4>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {score}%">{score:.1f}%</div>
                </div>
            </div>
            """
        
        return f"""
        <div class="section">
            <div class="section-header">
                <span>📊</span>
                <span>Compliance Overview</span>
            </div>
            <div class="section-content">
                {compliance_html}
            </div>
        </div>
        """
    
    def _create_schema_analysis(self, schema_info: Dict[str, Any], columns: List[Dict[str, Any]]) -> str:
        """Create schema analysis section"""
        table_name = schema_info.get('table_name', 'Unknown')
        
        # Create columns table
        columns_html = ""
        for i, col in enumerate(columns[:20]):  # Show first 20 columns
            columns_html += f"""
            <tr>
                <td>{i+1}</td>
                <td>{col.get('name', 'Unknown')}</td>
                <td>{col.get('data_type', 'Unknown')}</td>
                <td>{'Yes' if col.get('required', False) else 'No'}</td>
                <td>{'Yes' if col.get('primary_key', False) else 'No'}</td>
                <td>{col.get('description', 'No description')}</td>
            </tr>
            """
        
        if len(columns) > 20:
            columns_html += f"""
            <tr>
                <td colspan="6" style="text-align: center; font-weight: bold; color: #666;">
                    ... and {len(columns) - 20} additional columns
                </td>
            </tr>
            """
        
        return f"""
        <div class="section">
            <div class="section-header">
                <span>🔍</span>
                <span>Schema Analysis</span>
            </div>
            <div class="section-content">
                <h3>Table Information</h3>
                <p><strong>Table Name:</strong> {table_name}</p>
                <p><strong>Total Columns:</strong> {len(columns)}</p>
                <p><strong>Primary Keys:</strong> {len([col for col in columns if col.get('primary_key', False)])}</p>
                <p><strong>Required Fields:</strong> {len([col for col in columns if col.get('required', False)])}</p>
                
                <h3 style="margin-top: 30px;">Column Details</h3>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Column Name</th>
                            <th>Data Type</th>
                            <th>Required</th>
                            <th>Primary Key</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        {columns_html}
                    </tbody>
                </table>
            </div>
        </div>
        """
    
    def _create_data_quality_section(self, data_quality_metrics: Dict[str, Any]) -> str:
        """Create data quality section"""
        if not data_quality_metrics:
            return """
            <div class="section">
                <div class="section-header">
                    <span>📈</span>
                    <span>Data Quality Metrics</span>
                </div>
                <div class="section-content">
                    <p>No data quality metrics available at this time.</p>
                </div>
            </div>
            """
        
        # Extract metrics
        completeness = data_quality_metrics.get('completeness', {}).get('overall', 0) * 100
        uniqueness = data_quality_metrics.get('uniqueness', {}).get('overall', 0) * 100
        validity = data_quality_metrics.get('validity', {}).get('overall', 0) * 100
        overall_score = data_quality_metrics.get('overall_score', 0) * 100
        
        return f"""
        <div class="section">
            <div class="section-header">
                <span>📈</span>
                <span>Data Quality Metrics</span>
            </div>
            <div class="section-content">
                <div class="summary-grid">
                    <div class="summary-card">
                        <h3>{completeness:.1f}%</h3>
                        <p>Completeness</p>
                    </div>
                    <div class="summary-card">
                        <h3>{uniqueness:.1f}%</h3>
                        <p>Uniqueness</p>
                    </div>
                    <div class="summary-card">
                        <h3>{validity:.1f}%</h3>
                        <p>Validity</p>
                    </div>
                    <div class="summary-card">
                        <h3>{overall_score:.1f}%</h3>
                        <p>Overall Score</p>
                    </div>
                </div>
                
                <div class="charts-container">
                    <div class="chart-container">
                        <canvas id="qualityChart"></canvas>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _create_processing_results(self, processing_results: Dict[str, Any]) -> str:
        """Create processing results section"""
        if not processing_results:
            return ""
        
        original_rows = processing_results.get('original_data', {}).get('rows', 0)
        processed_rows = processing_results.get('processed_data', {}).get('rows', 0)
        improvements = processing_results.get('improvements_applied', [])
        
        improvements_html = ""
        for improvement in improvements[:10]:  # Show first 10 improvements
            improvements_html += f"<li>{improvement}</li>"
        
        return f"""
        <div class="section">
            <div class="section-header">
                <span>⚙️</span>
                <span>Processing Results</span>
            </div>
            <div class="section-content">
                <div class="summary-grid">
                    <div class="summary-card">
                        <h3>{original_rows:,}</h3>
                        <p>Original Rows</p>
                    </div>
                    <div class="summary-card">
                        <h3>{processed_rows:,}</h3>
                        <p>Processed Rows</p>
                    </div>
                    <div class="summary-card">
                        <h3>{len(improvements)}</h3>
                        <p>Improvements Applied</p>
                    </div>
                </div>
                
                <h3>Applied Improvements:</h3>
                <ul style="margin: 20px 0; padding-left: 20px;">
                    {improvements_html}
                </ul>
            </div>
        </div>
        """
    
    def _create_recommendations(self, compliance: Dict[str, Any], columns: List[Dict[str, Any]]) -> str:
        """Create recommendations section"""
        overall_score = compliance.get('overall_score', 0)
        
        recommendations = []
        
        if overall_score < 0.8:
            recommendations.append({
                'title': 'Improve Compliance Rate',
                'description': 'Work on raising the compliance rate to at least 80% by implementing required standards.',
                'priority': 'High'
            })
        
        # Check for missing primary keys
        primary_keys = [col for col in columns if col.get('primary_key', False)]
        if len(primary_keys) == 0:
            recommendations.append({
                'title': 'Add Primary Keys',
                'description': 'Add at least one primary key to ensure data uniqueness.',
                'priority': 'High'
            })
        
        # Check for required fields
        required_fields = [col for col in columns if col.get('required', False)]
        if len(required_fields) < len(columns) * 0.3:  # Less than 30% required
            recommendations.append({
                'title': 'Define Required Fields',
                'description': 'Define more fields as required to ensure data quality.',
                'priority': 'Medium'
            })
        
        recommendations_html = ""
        for rec in recommendations:
            priority_color = "#F44336" if rec['priority'] == 'High' else "#FF9800" if rec['priority'] == 'Medium' else "#4CAF50"
            recommendations_html += f"""
            <div class="recommendation">
                <h4>{rec['title']} <span style="color: {priority_color}; font-size: 0.9rem;">[{rec['priority']}]</span></h4>
                <p>{rec['description']}</p>
            </div>
            """
        
        return f"""
        <div class="section">
            <div class="section-header">
                <span>💡</span>
                <span>Recommendations</span>
            </div>
            <div class="section-content">
                {recommendations_html}
            </div>
        </div>
        """
    
    def _create_implementation_guide(self, columns: List[Dict[str, Any]]) -> str:
        """Create implementation guide section"""
        # Generate SQL for primary key
        primary_key_cols = [col for col in columns if col.get('primary_key', False)]
        sql_primary_key = ""
        if primary_key_cols:
            col_names = [col['name'] for col in primary_key_cols]
            sql_primary_key = f"""
            ALTER TABLE your_table 
            ADD CONSTRAINT pk_your_table 
            PRIMARY KEY ({', '.join(col_names)});
            """
        
        # Generate SQL for required fields
        required_cols = [col for col in columns if col.get('required', False)]
        sql_required = ""
        for col in required_cols[:5]:  # Show first 5
            sql_required += f"ALTER TABLE your_table MODIFY COLUMN {col['name']} NOT NULL;\n"
        
        return f"""
        <div class="section">
            <div class="section-header">
                <span>🛠️</span>
                <span>Implementation Guide</span>
            </div>
            <div class="section-content">
                <h3>1. Add Primary Keys</h3>
                <div class="code-block">
{sql_primary_key if sql_primary_key else "-- No primary keys defined"}
                </div>
                
                <h3>2. Add Required Fields</h3>
                <div class="code-block">
{sql_required if sql_required else "-- No required fields defined"}
                </div>
                
                <h3>3. Add Audit Fields</h3>
                <div class="code-block">
ALTER TABLE your_table 
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(100),
ADD COLUMN updated_by VARCHAR(100);
                </div>
            </div>
        </div>
        """
    
    def _create_footer(self) -> str:
        """Create footer section"""
        return """
        <div class="footer">
            <h3>🛡️ SANS Data Quality Management System</h3>
            <p>Comprehensive Technical Report for NDMO Standards Compliance</p>
            <p>Generated by Professional Data Quality Management System</p>
            <p style="margin-top: 20px; opacity: 0.8;">
                © 2024 SANS Data Quality System. All rights reserved.
            </p>
        </div>
        """
    
    def _get_javascript(self) -> str:
        """Get JavaScript for interactive features"""
        return """
        // Initialize charts when page loads
        document.addEventListener('DOMContentLoaded', function() {
            // Quality metrics chart
            const qualityCtx = document.getElementById('qualityChart');
            if (qualityCtx) {
                new Chart(qualityCtx, {
                    type: 'doughnut',
                    data: {
                        labels: ['Completeness', 'Uniqueness', 'Validity'],
                        datasets: [{
                            data: [85, 78, 92],
                            backgroundColor: [
                                '#4CAF50',
                                '#2196F3', 
                                '#FF9800'
                            ],
                            borderWidth: 0
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: {
                                    font: {
                                        family: 'Inter',
                                        size: 14
                                    }
                                }
                            }
                        }
                    }
                });
            }
            
            // Animate progress bars
            const progressBars = document.querySelectorAll('.progress-fill');
            progressBars.forEach(bar => {
                const width = bar.style.width;
                bar.style.width = '0%';
                setTimeout(() => {
                    bar.style.width = width;
                }, 500);
            });
        });
        
        // Print functionality
        function printReport() {
            window.print();
        }
        
        // Export to PDF (placeholder)
        function exportToPDF() {
            alert('ميزة التصدير إلى PDF قيد التطوير');
        }
        """

def main():
    """Test the HTML report generator"""
    generator = HTMLReportGenerator()
    
    # Sample data for testing
    sample_schema_analysis = {
        "ndmo_compliance": {
            "overall_score": 0.167,
            "data_governance": {"score": 0.0},
            "data_quality": {"score": 0.0},
            "data_security": {"score": 0.0},
            "data_architecture": {"score": 0.0},
            "business_rules": {"score": 0.2}
        },
        "schema_analysis": {
            "table_name": "flight_data",
            "columns": [
                {"name": "id", "data_type": "numeric", "required": True, "primary_key": True, "description": "معرف فريد"},
                {"name": "timestamp", "data_type": "datetime", "required": True, "description": "وقت التسجيل"},
                {"name": "callsign", "data_type": "text", "required": False, "description": "رمز الطائرة"}
            ]
        }
    }
    
    sample_quality_metrics = {
        "completeness": {"overall": 0.85},
        "uniqueness": {"overall": 0.78},
        "validity": {"overall": 0.92},
        "overall_score": 0.85
    }
    
    # Generate report
    filepath = generator.generate_technical_report_html(
        sample_schema_analysis, 
        sample_quality_metrics
    )
    
    print(f"HTML report generated: {filepath}")

if __name__ == "__main__":
    main()

