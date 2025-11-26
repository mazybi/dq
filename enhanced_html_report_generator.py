#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced HTML Technical Report Generator
مولد التقارير التقنية HTML المحسن

Developer: AI Assistant
Purpose: Generate detailed HTML reports with all technical specifications
"""

import os
import base64
from datetime import datetime
from typing import Dict, List, Any, Optional
import json

class EnhancedHTMLReportGenerator:
    """Enhanced HTML report generator with detailed technical specifications"""
    
    def __init__(self):
        """Initialize the enhanced HTML report generator"""
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
    
    def generate_detailed_technical_report(self, report_data: Dict[str, Any]) -> str:
        """Generate comprehensive technical report in HTML format"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"detailed_technical_report_{timestamp}.html"
        filepath = os.path.join(self.reports_dir, filename)
        
        # Generate HTML content
        html_content = self._create_detailed_html_template(report_data)
        
        # Save to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Detailed HTML Technical Report generated: {filename}")
        return filepath
    
    def _create_detailed_html_template(self, report_data: Dict[str, Any]) -> str:
        """Create the complete detailed HTML template"""
        
        logo_data = self.encode_logo()
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NDMO Compliance Technical Report</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        {self._get_detailed_css_styles()}
    </style>
</head>
<body>
    {self._create_detailed_header(logo_data, report_data)}
    {self._create_executive_summary(report_data)}
    {self._create_detailed_analysis(report_data)}
    {self._create_ndmo_compliance_details(report_data)}
    {self._create_required_modifications(report_data)}
    {self._create_implementation_priority(report_data)}
    {self._create_code_examples(report_data)}
    {self._create_success_metrics(report_data)}
    {self._create_additional_resources(report_data)}
    {self._create_implementation_checklist(report_data)}
    {self._create_detailed_footer()}
    
    <script>
        {self._get_detailed_javascript()}
    </script>
</body>
</html>
"""
        return html_content
    
    def _get_detailed_css_styles(self) -> str:
        """Get detailed CSS styles for the report"""
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
        
        /* Detailed Tables */
        .detailed-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .detailed-table th {
            background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
            color: white;
            padding: 20px;
            text-align: left;
            font-weight: 600;
        }
        
        .detailed-table td {
            padding: 15px 20px;
            border-bottom: 1px solid #eee;
        }
        
        .detailed-table tr:hover {
            background: #f8f9fa;
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
            position: relative;
        }
        
        .code-block::before {
            content: 'SQL';
            position: absolute;
            top: 10px;
            right: 15px;
            background: #4a5568;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.8rem;
            font-weight: bold;
        }
        
        /* Priority Sections */
        .priority-section {
            margin: 20px 0;
        }
        
        .priority-high {
            border-left: 5px solid #F44336;
            background: #ffebee;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
        }
        
        .priority-medium {
            border-left: 5px solid #FF9800;
            background: #fff3e0;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
        }
        
        .priority-low {
            border-left: 5px solid #4CAF50;
            background: #e8f5e8;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
        }
        
        /* Checklist */
        .checklist {
            list-style: none;
            padding: 0;
        }
        
        .checklist li {
            padding: 10px 0;
            border-bottom: 1px solid #eee;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .checklist li:before {
            content: '☐';
            font-size: 1.2rem;
            color: #666;
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
            
            .header-text h1 {
                font-size: 2rem;
            }
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
    
    def _create_detailed_header(self, logo_data: str, report_data: Dict[str, Any]) -> str:
        """Create the detailed header section"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""
        <div class="header">
            <div class="header-content">
                <div class="logo-section">
                    <img src="{logo_data}" alt="SANS Logo" class="logo">
                    <div class="header-text">
                        <h1>🛡️ NDMO Compliance Technical Report</h1>
                        <p>Professional NDMO Data Quality Dashboard</p>
                    </div>
                </div>
                <div class="report-info">
                    <h3>📊 Report Information</h3>
                    <p><strong>Generated on:</strong> {current_time}</p>
                    <p><strong>Project:</strong> Professional NDMO Data Quality Dashboard</p>
                    <p><strong>Version:</strong> 1.0</p>
                </div>
            </div>
        </div>
        """
    
    def _create_executive_summary(self, report_data: Dict[str, Any]) -> str:
        """Create executive summary section"""
        compliance = report_data.get("ndmo_compliance", {})
        schema_info = report_data.get("schema_analysis", {})
        columns = schema_info.get("columns", [])
        
        overall_score = compliance.get('overall_score', 0) * 100
        total_columns = len(columns)
        primary_keys = len([col for col in columns if col.get('primary_key', False)])
        required_fields = len([col for col in columns if col.get('required', False)])
        
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
                        <p>Current NDMO Compliance</p>
                    </div>
                    <div class="summary-card">
                        <h3>{total_columns}</h3>
                        <p>Total Columns</p>
                    </div>
                    <div class="summary-card">
                        <h3>{primary_keys}</h3>
                        <p>Primary Keys</p>
                    </div>
                    <div class="summary-card">
                        <h3>{required_fields}</h3>
                        <p>Required Fields</p>
                    </div>
                </div>
                
                <div class="compliance-status {status_class}">
                    <span style="font-size: 2rem;">{status_icon}</span>
                    <div>
                        <h3>Compliance Status: {status_text}</h3>
                        <p>Current NDMO Compliance: {overall_score:.1f}%</p>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _create_detailed_analysis(self, report_data: Dict[str, Any]) -> str:
        """Create detailed analysis section"""
        schema_info = report_data.get("schema_analysis", {})
        columns = schema_info.get("columns", [])
        table_name = schema_info.get('table_name', 'Unknown')
        
        # Create detailed columns table
        columns_html = ""
        for i, col in enumerate(columns):
            columns_html += f"""
            <tr>
                <td>{i+1}</td>
                <td><strong>{col.get('name', 'Unknown')}</strong></td>
                <td>{col.get('data_type', 'Unknown')}</td>
                <td>{'Yes' if col.get('required', False) else 'No'}</td>
                <td>{'Yes' if col.get('primary_key', False) else 'No'}</td>
                <td>{col.get('description', 'No description')}</td>
            </tr>
            """
        
        return f"""
        <div class="section">
            <div class="section-header">
                <span>🔍</span>
                <span>Detailed Analysis</span>
            </div>
            <div class="section-content">
                <h3>Schema Structure</h3>
                <div class="summary-grid">
                    <div class="summary-card">
                        <h3>{table_name}</h3>
                        <p>Table Name</p>
                    </div>
                    <div class="summary-card">
                        <h3>{len(columns)}</h3>
                        <p>Total Columns</p>
                    </div>
                    <div class="summary-card">
                        <h3>{len([col for col in columns if col.get('primary_key', False)])}</h3>
                        <p>Primary Keys</p>
                    </div>
                    <div class="summary-card">
                        <h3>{len([col for col in columns if col.get('required', False)])}</h3>
                        <p>Required Fields</p>
                    </div>
                </div>
                
                <h3 style="margin-top: 30px;">Complete Column Details</h3>
                <table class="detailed-table">
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
    
    def _create_ndmo_compliance_details(self, report_data: Dict[str, Any]) -> str:
        """Create NDMO compliance details section"""
        compliance = report_data.get("ndmo_compliance", {})
        
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
            status_icon = "✅" if score >= 80 else "⚠️" if score >= 50 else "❌"
            status_text = "Compliant" if score >= 80 else "Partially Compliant" if score >= 50 else "Non-Compliant"
            
            compliance_html += f"""
            <div class="progress-container">
                <h4>{status_icon} {label}: {score:.1f}% - {status_text}</h4>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {score}%">{score:.1f}%</div>
                </div>
            </div>
            """
        
        return f"""
        <div class="section">
            <div class="section-header">
                <span>📊</span>
                <span>NDMO Standards Compliance</span>
            </div>
            <div class="section-content">
                {compliance_html}
            </div>
        </div>
        """
    
    def _create_required_modifications(self, report_data: Dict[str, Any]) -> str:
        """Create required modifications section"""
        schema_info = report_data.get("schema_analysis", {})
        columns = schema_info.get("columns", [])
        
        # Primary Key Implementation
        primary_key_cols = [col for col in columns if col.get('primary_key', False)]
        sql_primary_key = ""
        if primary_key_cols:
            col_names = [col['name'] for col in primary_key_cols]
            sql_primary_key = f"""
ALTER TABLE your_table 
ADD CONSTRAINT pk_your_table 
PRIMARY KEY ({', '.join(col_names)});
"""
        else:
            sql_primary_key = """
-- Add primary key constraint
ALTER TABLE your_table 
ADD CONSTRAINT pk_your_table 
PRIMARY KEY (id);
"""
        
        # Data Type Standardization
        data_type_changes = ""
        for col in columns:
            current_type = col.get('data_type', 'unknown')
            col_name = col.get('name', 'Unknown')
            
            if current_type == 'numeric':
                new_type = 'NUMERIC'
            elif current_type == 'text':
                new_type = 'VARCHAR(255)'
            elif current_type == 'datetime':
                new_type = 'TIMESTAMP'
            elif current_type == 'boolean':
                new_type = 'BOOLEAN'
            else:
                new_type = 'VARCHAR(255)'
            
            data_type_changes += f"- **{col_name}:** {current_type} → {new_type}\n"
        
        # Constraint Implementation
        required_constraints = ""
        for col in columns:
            if col.get('required', False):
                col_name = col.get('name', 'Unknown')
                required_constraints += f"- **{col_name}:** Add NOT NULL constraint\n"
        
        # Data Quality Constraints
        validation_rules = ""
        for col in columns:
            col_name = col.get('name', 'Unknown')
            data_type = col.get('data_type', 'unknown')
            
            if data_type == 'text':
                validation_rules += f"- **{col_name}:** Length validation (None-255 characters)\n"
        
        return f"""
        <div class="section">
            <div class="section-header">
                <span>🔧</span>
                <span>Required Modifications</span>
            </div>
            <div class="section-content">
                <div class="priority-section">
                    <h3>1. Primary Key Implementation</h3>
                    <p><strong>Issue:</strong> Missing or insufficient primary key constraints</p>
                    <p><strong>Solution:</strong></p>
                    <div class="code-block">
{sql_primary_key}
                    </div>
                </div>
                
                <div class="priority-section">
                    <h3>2. Data Type Standardization</h3>
                    <p><strong>Issue:</strong> Inconsistent or non-standard data types</p>
                    <p><strong>Required Changes:</strong></p>
                    <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 15px 0;">
                        <pre style="white-space: pre-wrap; font-family: 'Inter', sans-serif;">{data_type_changes}</pre>
                    </div>
                </div>
                
                <div class="priority-section">
                    <h3>3. Constraint Implementation</h3>
                    <p><strong>Required Constraints:</strong></p>
                    <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 15px 0;">
                        <pre style="white-space: pre-wrap; font-family: 'Inter', sans-serif;">{required_constraints}</pre>
                    </div>
                </div>
                
                <div class="priority-section">
                    <h3>4. Audit Trail Fields</h3>
                    <p><strong>Missing Fields:</strong></p>
                    <ul style="margin: 15px 0; padding-left: 20px;">
                        <li><code>created_at</code> (TIMESTAMP)</li>
                        <li><code>updated_at</code> (TIMESTAMP)</li>
                        <li><code>created_by</code> (VARCHAR)</li>
                        <li><code>updated_by</code> (VARCHAR)</li>
                    </ul>
                    <p><strong>Implementation:</strong></p>
                    <div class="code-block">
ALTER TABLE your_table 
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(100),
ADD COLUMN updated_by VARCHAR(100);
                    </div>
                </div>
                
                <div class="priority-section">
                    <h3>5. Data Quality Constraints</h3>
                    <p><strong>Required Validations:</strong></p>
                    <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 15px 0;">
                        <pre style="white-space: pre-wrap; font-family: 'Inter', sans-serif;">{validation_rules}</pre>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _create_implementation_priority(self, report_data: Dict[str, Any]) -> str:
        """Create implementation priority section"""
        return """
        <div class="section">
            <div class="section-header">
                <span>🚀</span>
                <span>Implementation Priority</span>
            </div>
            <div class="section-content">
                <div class="priority-high">
                    <h3>High Priority (Critical)</h3>
                    <ol>
                        <li><strong>Primary Key Implementation</strong> - Required for data integrity</li>
                        <li><strong>Audit Trail Fields</strong> - Required for compliance tracking</li>
                        <li><strong>Data Type Standardization</strong> - Required for data consistency</li>
                    </ol>
                </div>
                
                <div class="priority-medium">
                    <h3>Medium Priority (Important)</h3>
                    <ol>
                        <li><strong>Constraint Implementation</strong> - Improves data quality</li>
                        <li><strong>Validation Rules</strong> - Ensures data accuracy</li>
                        <li><strong>Index Optimization</strong> - Improves performance</li>
                    </ol>
                </div>
                
                <div class="priority-low">
                    <h3>Low Priority (Enhancement)</h3>
                    <ol>
                        <li><strong>Documentation Updates</strong> - Improves maintainability</li>
                        <li><strong>Performance Monitoring</strong> - Optimizes system performance</li>
                    </ol>
                </div>
            </div>
        </div>
        """
    
    def _create_code_examples(self, report_data: Dict[str, Any]) -> str:
        """Create code examples section"""
        schema_info = report_data.get("schema_analysis", {})
        columns = schema_info.get("columns", [])
        
        # Generate migration script
        migration_script = """
-- Migration script for NDMO compliance
BEGIN TRANSACTION;

-- Add primary key
ALTER TABLE your_table 
ADD CONSTRAINT pk_your_table 
PRIMARY KEY (id);

-- Add audit fields
ALTER TABLE your_table 
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(100),
ADD COLUMN updated_by VARCHAR(100);

-- Add constraints"""
        
        for col in columns:
            if col.get('required', False):
                col_name = col.get('name', 'Unknown')
                migration_script += f"\nALTER TABLE your_table MODIFY COLUMN {col_name} NOT NULL;"
        
        migration_script += "\n\nCOMMIT;"
        
        # Generate Python validation code
        required_fields = [col['name'] for col in columns if col.get('required', False)]
        python_code = f"""
# Python example for data validation
def validate_data(data):
    errors = []
    
    # Required field validation
    required_fields = {required_fields}
    for field in required_fields:
        if not data.get(field):
            errors.append(f"{{field}} is required")
    
    # Data type validation
    for col in columns:
        field_name = col.get('name', 'Unknown')
        field_type = col.get('data_type', 'Unknown')
        value = data.get(field_name)
        
        if value is not None:
            if field_type == 'INTEGER' and not isinstance(value, int):
                errors.append(f"{{field_name}} must be an integer")
            elif field_type == 'VARCHAR' and not isinstance(value, str):
                errors.append(f"{{field_name}} must be a string")
    
    return errors
"""
        
        return f"""
        <div class="section">
            <div class="section-header">
                <span>📝</span>
                <span>Code Examples</span>
            </div>
            <div class="section-content">
                <h3>Database Migration Script</h3>
                <div class="code-block">
{migration_script}
                </div>
                
                <h3>Application Code Updates</h3>
                <div class="code-block">
{python_code}
                </div>
            </div>
        </div>
        """
    
    def _create_success_metrics(self, report_data: Dict[str, Any]) -> str:
        """Create success metrics section"""
        return """
        <div class="section">
            <div class="section-header">
                <span>🎯</span>
                <span>Success Metrics</span>
            </div>
            <div class="section-content">
                <h3>Compliance Targets</h3>
                <div class="summary-grid">
                    <div class="summary-card">
                        <h3>95%+</h3>
                        <p>Overall NDMO Compliance</p>
                    </div>
                    <div class="summary-card">
                        <h3>90%+</h3>
                        <p>Data Quality Score</p>
                    </div>
                    <div class="summary-card">
                        <h3>100%</h3>
                        <p>Audit Trail Coverage</p>
                    </div>
                    <div class="summary-card">
                        <h3>95%+</h3>
                        <p>Constraint Coverage</p>
                    </div>
                </div>
                
                <h3>Performance Targets</h3>
                <div class="summary-grid">
                    <div class="summary-card">
                        <h3>&lt; 100ms</h3>
                        <p>Query Response Time</p>
                    </div>
                    <div class="summary-card">
                        <h3>&lt; 50ms</h3>
                        <p>Data Validation Time</p>
                    </div>
                    <div class="summary-card">
                        <h3>&lt; 10ms</h3>
                        <p>Audit Log Performance</p>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _create_additional_resources(self, report_data: Dict[str, Any]) -> str:
        """Create additional resources section"""
        return """
        <div class="section">
            <div class="section-header">
                <span>📚</span>
                <span>Additional Resources</span>
            </div>
            <div class="section-content">
                <h3>NDMO Standards Documentation</h3>
                <ul style="margin: 20px 0; padding-left: 20px;">
                    <li><a href="https://ndmo.gov.sa/standards/data-governance" target="_blank">Data Governance Standards</a></li>
                    <li><a href="https://ndmo.gov.sa/standards/data-quality" target="_blank">Data Quality Guidelines</a></li>
                    <li><a href="https://ndmo.gov.sa/standards/security" target="_blank">Security Requirements</a></li>
                </ul>
            </div>
        </div>
        """
    
    def _create_implementation_checklist(self, report_data: Dict[str, Any]) -> str:
        """Create implementation checklist section"""
        return """
        <div class="section">
            <div class="section-header">
                <span>✅</span>
                <span>Implementation Checklist</span>
            </div>
            <div class="section-content">
                <ul class="checklist">
                    <li>Primary key implementation</li>
                    <li>Audit trail fields added</li>
                    <li>Data type standardization</li>
                    <li>Constraint implementation</li>
                    <li>Validation rules added</li>
                    <li>Performance testing completed</li>
                    <li>Documentation updated</li>
                    <li>Compliance testing passed</li>
                </ul>
            </div>
        </div>
        """
    
    def _create_detailed_footer(self) -> str:
        """Create detailed footer section"""
        return """
        <div class="footer">
            <h3>🛡️ Professional NDMO Data Quality Dashboard</h3>
            <p>Comprehensive Technical Report for NDMO Standards Compliance</p>
            <p>Generated by Professional Data Quality Management System</p>
            <p style="margin-top: 20px; opacity: 0.8;">
                <strong>Report Generated by:</strong> Professional NDMO Data Quality Dashboard<br>
                <strong>Version:</strong> 1.0<br>
                <strong>Contact:</strong> Technical Team
            </p>
        </div>
        """
    
    def _get_detailed_javascript(self) -> str:
        """Get JavaScript for interactive features"""
        return """
        // Initialize interactive features when page loads
        document.addEventListener('DOMContentLoaded', function() {
            // Animate progress bars
            const progressBars = document.querySelectorAll('.progress-fill');
            progressBars.forEach(bar => {
                const width = bar.style.width;
                bar.style.width = '0%';
                setTimeout(() => {
                    bar.style.width = width;
                }, 500);
            });
            
            // Add click handlers for code blocks
            const codeBlocks = document.querySelectorAll('.code-block');
            codeBlocks.forEach(block => {
                block.addEventListener('click', function() {
                    // Copy to clipboard functionality could be added here
                    console.log('Code block clicked');
                });
            });
        });
        
        // Print functionality
        function printReport() {
            window.print();
        }
        
        // Export to PDF (placeholder)
        function exportToPDF() {
            alert('PDF export functionality coming soon');
        }
        """

def main():
    """Test the enhanced HTML report generator"""
    
    # Sample data based on the technical report
    report_data = {
        "ndmo_compliance": {
            "overall_score": 0.167,  # 16.7%
            "data_governance": {"score": 0.0},  # 0.0%
            "data_quality": {"score": 0.15},    # 15.0%
            "data_security": {"score": 0.0},    # 0.0%
            "data_architecture": {"score": 0.0}, # 0.0%
            "business_rules": {"score": 0.0}    # 0.0%
        },
        "schema_analysis": {
            "table_name": "Unknown",
            "columns": [
                {"name": "Serial", "data_type": "numeric", "required": True, "primary_key": False, "description": "Serial number"},
                {"name": "FName", "data_type": "text", "required": True, "primary_key": False, "description": "File name"},
                {"name": "FYInvoice", "data_type": "text", "required": True, "primary_key": False, "description": "Fiscal year invoice"},
                {"name": "BillingReference", "data_type": "text", "required": True, "primary_key": False, "description": "Billing reference"},
                {"name": "FYCust", "data_type": "text", "required": True, "primary_key": False, "description": "Fiscal year customer"},
                {"name": "PID", "data_type": "text", "required": True, "primary_key": False, "description": "Process ID"},
                {"name": "DirectID", "data_type": "text", "required": True, "primary_key": False, "description": "Direct ID"},
                {"name": "AirlineCode", "data_type": "text", "required": True, "primary_key": False, "description": "Airline code"},
                {"name": "Airline", "data_type": "text", "required": True, "primary_key": False, "description": "Airline name"},
                {"name": "GSA", "data_type": "text", "required": True, "primary_key": False, "description": "General Sales Agent"},
                {"name": "FlightDate", "data_type": "text", "required": True, "primary_key": False, "description": "Flight date"},
                {"name": "FlightTime", "data_type": "text", "required": True, "primary_key": False, "description": "Flight time"},
                {"name": "AircraftType", "data_type": "text", "required": True, "primary_key": False, "description": "Aircraft type"},
                {"name": "CallSign", "data_type": "text", "required": True, "primary_key": False, "description": "Call sign"},
                {"name": "Reg", "data_type": "text", "required": True, "primary_key": False, "description": "Registration"},
                {"name": "ICAOfrom", "data_type": "text", "required": True, "primary_key": False, "description": "ICAO departure code"},
                {"name": "ICAOto", "data_type": "text", "required": True, "primary_key": False, "description": "ICAO arrival code"},
                {"name": "ICAOFromToPair", "data_type": "text", "required": True, "primary_key": False, "description": "ICAO route pair"},
                {"name": "EntryPoint", "data_type": "text", "required": True, "primary_key": False, "description": "Entry point"},
                {"name": "ExitPoint", "data_type": "text", "required": True, "primary_key": False, "description": "Exit point"},
                {"name": "Distance", "data_type": "numeric", "required": True, "primary_key": False, "description": "Flight distance"},
                {"name": "DistFactor", "data_type": "numeric", "required": True, "primary_key": False, "description": "Distance factor"},
                {"name": "CraftWeight", "data_type": "numeric", "required": True, "primary_key": False, "description": "Aircraft weight"},
                {"name": "WeightFactor", "data_type": "numeric", "required": True, "primary_key": False, "description": "Weight factor"},
                {"name": "Seats", "data_type": "numeric", "required": True, "primary_key": False, "description": "Number of seats"},
                {"name": "TypeHLO", "data_type": "text", "required": True, "primary_key": False, "description": "Type HLO"},
                {"name": "Exempt", "data_type": "text", "required": True, "primary_key": False, "description": "Exemption status"},
                {"name": "EnRoute", "data_type": "numeric", "required": True, "primary_key": False, "description": "En route charge"},
                {"name": "Approach", "data_type": "numeric", "required": True, "primary_key": False, "description": "Approach charge"},
                {"name": "NetCharge", "data_type": "numeric", "required": True, "primary_key": False, "description": "Net charge"},
                {"name": "VATcharge", "data_type": "numeric", "required": True, "primary_key": False, "description": "VAT charge"},
                {"name": "TotalCharge", "data_type": "numeric", "required": True, "primary_key": False, "description": "Total charge"},
                {"name": "GACAInvNum", "data_type": "text", "required": True, "primary_key": False, "description": "GACA invoice number"},
                {"name": "TypeGMNSX", "data_type": "text", "required": True, "primary_key": False, "description": "Type GMNSX"}
            ]
        }
    }
    
    generator = EnhancedHTMLReportGenerator()
    filepath = generator.generate_detailed_technical_report(report_data)
    
    print(f"Enhanced HTML report generated: {filepath}")

if __name__ == "__main__":
    main()
