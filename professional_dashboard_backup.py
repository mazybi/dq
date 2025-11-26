#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Professional NDMO Data Quality Dashboard
Interactive dashboard for schema analysis, data processing, and quality assessment

Developer: AI Assistant
Purpose: Professional dashboard for comprehensive data quality management
"""

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
import os
import json
import glob
import base64
from typing import List, Dict, Any
import warnings
warnings.filterwarnings('ignore')

# Import our custom modules
from ndmo_standards import NDMOStandardsManager, ComplianceStatus
from smart_schema_analyzer import SmartSchemaAnalyzer
from smart_data_processor import SmartDataProcessor
from schema_problem_analyzer import SchemaProblemAnalyzer
from sql_schema_generator import SQLSchemaGenerator

class ProfessionalNDMODashboard:
    """Professional NDMO Data Quality Dashboard"""
    
    def __init__(self):
        """Initialize the dashboard"""
        self.setup_page_config()
        self.initialize_session_state()
        self.setup_custom_css()
        
        # Initialize components
        self.ndmo_manager = NDMOStandardsManager()
        self.schema_analyzer = SmartSchemaAnalyzer()
        self.data_processor = SmartDataProcessor()
        self.problem_analyzer = SchemaProblemAnalyzer()
        self.sql_generator = SQLSchemaGenerator()
    
    def setup_page_config(self):
        """Setup Streamlit page configuration"""
        st.set_page_config(
            page_title="SANS Data Quality System - NDMO Compliance Dashboard",
            page_icon="🛡️",
            layout="wide",
            initial_sidebar_state="expanded"
        )
    
    def setup_custom_css(self):
        """Setup custom CSS styling"""
        st.markdown("""
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        /* Global Styles */
        .main {
            font-family: 'Inter', sans-serif;
        }
        
        /* Main Header with Enhanced Design - Fixed Position */
        .main-header {
            text-align: center;
            padding: 2rem 1.5rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            color: white;
            border-radius: 0 0 25px 25px;
            margin-bottom: 1.5rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
            position: sticky;
            top: 0;
            z-index: 1000;
            overflow: hidden;
        }
        
        .main-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/><circle cx="50" cy="10" r="0.5" fill="white" opacity="0.1"/><circle cx="10" cy="60" r="0.5" fill="white" opacity="0.1"/><circle cx="90" cy="40" r="0.5" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            opacity: 0.3;
        }
        
        .main-header h1 {
            font-size: 2rem;
            font-weight: 800;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            position: relative;
            z-index: 1;
        }
        
        .main-header p {
            font-size: 1rem;
            font-weight: 400;
            margin: 0.5rem 0 0 0;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }
        
        /* Enhanced Metric Cards */
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem 1.5rem;
            border-radius: 20px;
            color: white;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            margin-bottom: 1.5rem;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .metric-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transform: rotate(45deg);
            transition: all 0.6s;
            opacity: 0;
        }
        
        .metric-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
        }
        
        .metric-card:hover::before {
            opacity: 1;
            animation: shimmer 1.5s ease-in-out;
        }
        
        @keyframes shimmer {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }
        
        .metric-card h3 {
            font-size: 2.5rem;
            font-weight: 700;
            margin: 0;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
        }
        
        .metric-card p {
            font-size: 1rem;
            font-weight: 500;
            margin: 0.5rem 0 0 0;
            opacity: 0.9;
        }
        
        /* Enhanced Status Cards */
        .status-card {
            padding: 2rem;
            border-radius: 20px;
            margin-bottom: 1.5rem;
            border-left: 6px solid;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .status-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .status-card:hover::before {
            opacity: 1;
        }
        
        .status-success {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            border-left-color: #00d4aa;
            color: white;
        }
        
        .status-warning {
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            border-left-color: #ffc107;
            color: white;
        }
        
        .status-error {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            border-left-color: #dc3545;
            color: white;
        }
        
        .status-info {
            background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
            border-left-color: #17a2b8;
            color: white;
        }
        
        /* Enhanced Tabs Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 6px;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 6px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            overflow-x: auto;
            white-space: nowrap;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border-radius: 12px;
            padding: 10px 16px;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            border: 2px solid transparent;
            position: relative;
            overflow: visible;
            min-width: fit-content;
            white-space: nowrap;
            flex-shrink: 0;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-color: #667eea;
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
        }
        
        .stTabs [aria-selected="true"]:hover {
            background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
        }
        
        /* Enhanced Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            font-size: 0.95rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }
        
        .stButton > button:active {
            transform: translateY(0);
        }
        
        /* Primary Button */
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #00b894 0%, #00a085 100%);
            box-shadow: 0 4px 15px rgba(0, 184, 148, 0.3);
        }
        
        .stButton > button[kind="primary"]:hover {
            background: linear-gradient(135deg, #00a085 0%, #008f7a 100%);
            box-shadow: 0 6px 20px rgba(0, 184, 148, 0.4);
        }
        
        /* Secondary Button */
        .stButton > button[kind="secondary"] {
            background: linear-gradient(135deg, #6c5ce7 0%, #5f3dc4 100%);
            box-shadow: 0 4px 15px rgba(108, 92, 231, 0.3);
        }
        
        .stButton > button[kind="secondary"]:hover {
            background: linear-gradient(135deg, #5f3dc4 0%, #4c2c9a 100%);
            box-shadow: 0 6px 20px rgba(108, 92, 231, 0.4);
        }
        
        /* Enhanced DataFrames */
        .dataframe {
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(0, 0, 0, 0.05);
        }
        
        .dataframe thead th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: 600;
            padding: 1rem;
            border: none;
        }
        
        .dataframe tbody tr {
            transition: background-color 0.3s ease;
        }
        
        .dataframe tbody tr:hover {
            background-color: rgba(102, 126, 234, 0.05);
        }
        
        .dataframe tbody tr:nth-child(even) {
            background-color: rgba(0, 0, 0, 0.02);
        }
        
        /* Enhanced Sidebar */
        .css-1d391kg {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-right: 3px solid #667eea;
        }
        
        /* Enhanced File Uploader */
        .stFileUploader > div {
            border: 2px dashed #667eea;
            border-radius: 15px;
            padding: 2rem;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
            transition: all 0.3s ease;
        }
        
        .stFileUploader > div:hover {
            border-color: #5a6fd8;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        }
        
        /* Enhanced Selectbox */
        .stSelectbox > div > div {
            border-radius: 12px;
            border: 2px solid #e9ecef;
            transition: all 0.3s ease;
        }
        
        .stSelectbox > div > div:hover {
            border-color: #667eea;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.1);
        }
        
        /* Enhanced Text Input */
        .stTextInput > div > div > input {
            border-radius: 12px;
            border: 2px solid #e9ecef;
            padding: 0.75rem 1rem;
            transition: all 0.3s ease;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        /* Enhanced Progress Bar */
        .stProgress > div > div > div {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
        }
        
        /* Enhanced Expander */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 12px;
            border: 1px solid #dee2e6;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .streamlit-expanderHeader:hover {
            background: linear-gradient(135deg, #e9ecef 0%, #dee2e6 100%);
        }
        
        /* Enhanced Alert Boxes */
        .stAlert {
            border-radius: 15px;
            border: none;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        
        /* Custom Loading Animation */
        .loading-spinner {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(102, 126, 234, 0.3);
            border-radius: 50%;
            border-top-color: #667eea;
            animation: spin 1s ease-in-out infinite;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        /* Enhanced Charts Container */
        .chart-container {
            background: white;
            border-radius: 20px;
            padding: 1.5rem;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(0, 0, 0, 0.05);
            margin-bottom: 1.5rem;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .main-header h1 {
                font-size: 1.5rem;
            }
            
            .main-header p {
                font-size: 0.9rem;
            }
            
            .metric-card {
                padding: 1.5rem 1rem;
            }
            
            .metric-card h3 {
                font-size: 2rem;
            }
            
            .stTabs [data-baseweb="tab"] {
                padding: 8px 12px;
                font-size: 0.8rem;
            }
            
            .stTabs [data-baseweb="tab-list"] {
                gap: 4px;
                padding: 4px;
            }
        }
        
        @media (max-width: 480px) {
            .main-header {
                padding: 1rem 1rem;
            }
            
            .main-header h1 {
                font-size: 1.3rem;
            }
            
            .main-header p {
                font-size: 0.8rem;
            }
            
            .stTabs [data-baseweb="tab"] {
                padding: 6px 8px;
                font-size: 0.75rem;
            }
        }
        
        /* Dark Mode Support */
        @media (prefers-color-scheme: dark) {
            .main-header {
                background: linear-gradient(135deg, #2d3748 0%, #4a5568 50%, #718096 100%);
            }
            
            .metric-card {
                background: linear-gradient(135deg, #2d3748 0%, #4a5568 100%);
            }
        }
        }
        
        .status-danger {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            border-left-color: #dc3545;
            color: white;
        }
        
        .chart-container {
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
        }
        
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.5rem 1rem;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        
        .company-logo {
            max-width: 200px;
            height: auto;
            margin-bottom: 1rem;
            filter: brightness(0) invert(1);
        }
        
        .report-section {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
            border: 1px solid #dee2e6;
        }
        
        .file-list {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #dee2e6;
            margin: 0.5rem 0;
        }
        
        .file-item {
            padding: 0.5rem;
            border-bottom: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .file-item:last-child {
            border-bottom: none;
        }
        
        .download-btn {
            background: #28a745;
            color: white;
            border: none;
            padding: 0.25rem 0.75rem;
            border-radius: 5px;
            font-size: 0.8rem;
            cursor: pointer;
        }
        
        .download-btn:hover {
            background: #218838;
        }
        </style>
        """, unsafe_allow_html=True)
    
    def display_company_header(self):
        """Display enhanced company header with logo and status"""
        try:
            # Try to load the company logo
            logo_base64 = self.get_logo_base64()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if logo_base64:
                st.markdown(f"""
                <div class="main-header">
                    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 0.5rem;">
                        <img src="data:image/png;base64,{logo_base64}" class="company-logo" alt="SANS Data Quality System" style="max-width: 60px; height: auto; margin-right: 1rem;">
                        <div>
                            <h1 style="margin: 0; font-size: 2rem;">🛡️ SANS Data Quality System</h1>
                            <p style="margin: 0.25rem 0 0 0; font-size: 1rem; opacity: 0.9;">Professional NDMO Compliance Dashboard</p>
                        </div>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 0.5rem; padding-top: 0.5rem; border-top: 1px solid rgba(255,255,255,0.2);">
                        <div style="text-align: left;">
                            <p style="margin: 0; font-size: 0.85rem; opacity: 0.8;">📊 Advanced Data Quality Management</p>
                            <p style="margin: 0; font-size: 0.85rem; opacity: 0.8;">🔒 Enterprise Security & Compliance</p>
                        </div>
                        <div style="text-align: right;">
                            <p style="margin: 0; font-size: 0.8rem; opacity: 0.7;">🕒 {current_time}</p>
                            <p style="margin: 0; font-size: 0.8rem; opacity: 0.7;">🌐 System Status: Online</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                # Fallback header without logo
                st.markdown(f"""
                <div class="main-header">
                    <h1 style="font-size: 2rem; margin-bottom: 0.25rem;">🛡️ SANS Data Quality System</h1>
                    <h3 style="margin: 0.25rem 0; font-size: 1.2rem; opacity: 0.9;">Professional NDMO Compliance Dashboard</h3>
                    <p style="margin: 0.25rem 0; font-size: 1rem; opacity: 0.8;">Advanced Data Quality Management & Compliance Monitoring</p>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 0.5rem; padding-top: 0.5rem; border-top: 1px solid rgba(255,255,255,0.2);">
                        <div style="text-align: left;">
                            <p style="margin: 0; font-size: 0.85rem; opacity: 0.8;">📊 Advanced Data Quality Management</p>
                            <p style="margin: 0; font-size: 0.85rem; opacity: 0.8;">🔒 Enterprise Security & Compliance</p>
                        </div>
                        <div style="text-align: right;">
                            <p style="margin: 0; font-size: 0.8rem; opacity: 0.7;">🕒 {current_time}</p>
                            <p style="margin: 0; font-size: 0.8rem; opacity: 0.7;">🌐 System Status: Online</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            # Fallback header
            st.markdown(f"""
            <div class="main-header">
                <h1 style="font-size: 2rem; margin-bottom: 0.25rem;">🛡️ SANS Data Quality System</h1>
                <h3 style="margin: 0.25rem 0; font-size: 1.2rem; opacity: 0.9;">Professional NDMO Compliance Dashboard</h3>
                <p style="margin: 0.25rem 0; font-size: 1rem; opacity: 0.8;">Advanced Data Quality Management & Compliance Monitoring</p>
            </div>
            """, unsafe_allow_html=True)
    
    def get_logo_base64(self) -> str:
        """Get logo as base64 string"""
        try:
            logo_path = "assets/logo@3x.png"
            if os.path.exists(logo_path):
                with open(logo_path, "rb") as f:
                    logo_data = f.read()
                    return base64.b64encode(logo_data).decode()
            return ""
        except Exception:
            return ""
    
    def ensure_reports_directories(self):
        """Ensure reports directories exist"""
        directories = [
            "reports/technical_reports",
            "reports/compliance_reports", 
            "reports/html_reports",
            "reports/exports"
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    def get_report_path(self, report_type: str, filename: str) -> str:
        """Get the full path for a report file"""
        self.ensure_reports_directories()
        
        if report_type == "technical":
            return f"reports/technical_reports/{filename}"
        elif report_type == "compliance":
            return f"reports/compliance_reports/{filename}"
        elif report_type == "html":
            return f"reports/html_reports/{filename}"
        elif report_type == "export":
            return f"reports/exports/{filename}"
        else:
            return filename
    
    def list_report_files(self, report_type: str = None) -> List[Dict[str, Any]]:
        """List all report files"""
        self.ensure_reports_directories()
        
        files = []
        
        if report_type is None or report_type == "technical":
            tech_files = glob.glob("reports/technical_reports/*")
            for file in tech_files:
                files.append({
                    "name": os.path.basename(file),
                    "path": file,
                    "type": "technical",
                    "size": os.path.getsize(file),
                    "modified": datetime.fromtimestamp(os.path.getmtime(file))
                })
        
        if report_type is None or report_type == "compliance":
            comp_files = glob.glob("reports/compliance_reports/*")
            for file in comp_files:
                files.append({
                    "name": os.path.basename(file),
                    "path": file,
                    "type": "compliance",
                    "size": os.path.getsize(file),
                    "modified": datetime.fromtimestamp(os.path.getmtime(file))
                })
        
        if report_type is None or report_type == "html":
            html_files = glob.glob("reports/html_reports/*")
            for file in html_files:
                files.append({
                    "name": os.path.basename(file),
                    "path": file,
                    "type": "html",
                    "size": os.path.getsize(file),
                    "modified": datetime.fromtimestamp(os.path.getmtime(file))
                })
        
        if report_type is None or report_type == "export":
            exp_files = glob.glob("reports/exports/*")
            for file in exp_files:
                files.append({
                    "name": os.path.basename(file),
                    "path": file,
                    "type": "export",
                    "size": os.path.getsize(file),
                    "modified": datetime.fromtimestamp(os.path.getmtime(file))
                })
        
        # Sort by modification time (newest first)
        files.sort(key=lambda x: x["modified"], reverse=True)
        return files
    
    def create_reports_viewer_tab(self):
        """Create reports viewer tab"""
        st.markdown("### 📁 Saved Reports Viewer")
        
        # Filter options
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            report_type_filter = st.selectbox(
                "Filter by Report Type:",
                ["All", "Technical Reports", "Compliance Reports", "HTML Reports", "Exports"],
                key="report_type_filter"
            )
        
        with col2:
            if st.button("🔄 Refresh", key="refresh_reports"):
                st.rerun()
        
        with col3:
            if st.button("🗑️ Clear All", key="clear_all_reports"):
                self.clear_all_reports()
                st.rerun()
        
        # Get filtered files
        if report_type_filter == "All":
            files = self.list_report_files()
        elif report_type_filter == "Technical Reports":
            files = self.list_report_files("technical")
        elif report_type_filter == "Compliance Reports":
            files = self.list_report_files("compliance")
        elif report_type_filter == "HTML Reports":
            files = self.list_report_files("html")
        elif report_type_filter == "Exports":
            files = self.list_report_files("export")
        
        if not files:
            st.info("📭 No reports found. Generate some reports first!")
            return
        
        # Display files
        st.markdown(f"**Found {len(files)} report(s)**")
        
        for file_info in files:
            with st.container():
                col1, col2, col3, col4 = st.columns([3, 2, 1, 1])
                
                with col1:
                    # File name and type
                    type_icon = {
                        "technical": "🔧",
                        "compliance": "🛡️", 
                        "html": "📄",
                        "export": "📊"
                    }.get(file_info["type"], "📄")
                    
                    st.markdown(f"**{type_icon} {file_info['name']}**")
                    st.caption(f"Type: {file_info['type'].title()}")
                
                with col2:
                    # File details
                    size_mb = file_info["size"] / (1024 * 1024)
                    st.markdown(f"**Size:** {size_mb:.2f} MB")
                    st.markdown(f"**Modified:** {file_info['modified'].strftime('%Y-%m-%d %H:%M')}")
                
                with col3:
                    # Download button
                    if st.button("⬇️ Download", key=f"download_{file_info['name']}"):
                        self.download_file(file_info["path"], file_info["name"])
                
                with col4:
                    # View button
                    if st.button("👁️ View", key=f"view_{file_info['name']}"):
                        self.view_report_file(file_info["path"], file_info["type"])
                
                st.divider()
    
    def download_file(self, file_path: str, filename: str):
        """Download a file"""
        try:
            with open(file_path, "rb") as f:
                file_data = f.read()
            
            st.download_button(
                label="📥 Download File",
                data=file_data,
                file_name=filename,
                mime="application/octet-stream",
                key=f"download_{filename}_{datetime.now().timestamp()}"
            )
        except Exception as e:
            st.error(f"❌ Error downloading file: {str(e)}")
    
    def view_report_file(self, file_path: str, file_type: str):
        """View a report file"""
        try:
            if file_type == "html":
                # For HTML files, display in an iframe
                with open(file_path, "r", encoding="utf-8") as f:
                    html_content = f.read()
                
                st.markdown("### 📄 Report Preview")
                components.html(html_content, height=600, scrolling=True)
            
            else:
                # For other files, display as text
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                st.markdown("### 📄 Report Content")
                st.text_area("Report Content:", content, height=400)
                
        except Exception as e:
            st.error(f"❌ Error viewing file: {str(e)}")
    
    def clear_all_reports(self):
        """Clear all report files"""
        try:
            directories = [
                "reports/technical_reports",
                "reports/compliance_reports", 
                "reports/html_reports",
                "reports/exports"
            ]
            
            for directory in directories:
                if os.path.exists(directory):
                    for file in os.listdir(directory):
                        file_path = os.path.join(directory, file)
                        if os.path.isfile(file_path):
                            os.remove(file_path)
            
            st.success("✅ All reports cleared successfully!")
            
        except Exception as e:
            st.error(f"❌ Error clearing reports: {str(e)}")
    
    def create_sql_generator_tab(self):
        """Create SQL Generator tab"""
        st.markdown("## 🗄️ SQL Schema Generator")
        st.markdown("Generate SQL scripts for creating tables and managing database schemas")
        
        # Two main sections
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 📝 Generate SQL Script")
            self.create_sql_generation_section()
        
        with col2:
            st.markdown("### 📋 Schema Template")
            self.create_schema_template_section()
    
    def create_sql_generation_section(self):
        """Create SQL generation section"""
        
        # Table name input
        table_name = st.text_input(
            "Table Name:",
            value="my_table",
            help="Enter the name for your database table"
        )
        
        # Database type selection
        database_type = st.selectbox(
            "Database Type:",
            options=['mysql', 'postgresql', 'sqlserver', 'oracle', 'sqlite'],
            format_func=lambda x: {
                'mysql': 'MySQL',
                'postgresql': 'PostgreSQL',
                'sqlserver': 'SQL Server',
                'oracle': 'Oracle',
                'sqlite': 'SQLite'
            }[x],
            help="Select the target database system"
        )
        
        # Check if schema analysis is available
        if hasattr(st.session_state, 'schema_analysis') and st.session_state.schema_analysis:
            schema_info = st.session_state.schema_analysis.get('schema_analysis', {})
            total_columns = len(schema_info.get('columns', []))
            st.success(f"✅ Schema analysis available - {total_columns} columns found")
            st.caption("Using analyzed schema data for SQL generation")
            schema_source = "analyzed"
        else:
            st.info("💡 No schema analysis found - Will use template structure")
            st.caption("Template includes 10 sample columns with various data types and constraints")
            schema_source = "template"
        
        # Show schema preview
        with st.expander("📋 Preview Schema Structure"):
            if schema_source == "analyzed":
                self.show_analyzed_schema_preview()
            else:
                self.show_template_schema_preview()
        
        # Generate buttons
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔨 Generate CREATE TABLE", type="primary"):
                self.generate_create_table_sql(table_name, database_type, schema_source)
        
        with col2:
            if st.button("🔍 Generate Schema Query"):
                self.generate_schema_query_sql(table_name, database_type)
        
        # Display generated SQL if available
        if hasattr(st.session_state, 'generated_sql') and st.session_state.generated_sql:
            st.markdown("### 📄 Generated SQL Script")
            
            # SQL type tabs
            sql_tab1, sql_tab2 = st.tabs(["📝 SQL Code", "💾 Download"])
            
            with sql_tab1:
                st.code(st.session_state.generated_sql, language='sql')
            
            with sql_tab2:
                self.download_sql_script()
    
    def create_schema_template_section(self):
        """Create schema template section"""
        
        st.markdown("### 📋 Download Schema Template")
        st.markdown("Download a template Excel file to define your schema structure.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📥 Download Template", type="secondary"):
                self.download_schema_template()
        
        with col2:
            if st.button("📖 View Template Structure"):
                self.show_template_structure()
        
        # Template instructions
        st.markdown("### 📖 Template Instructions")
        st.markdown("""
        **How to use the template:**
        
        1. **Download** the template Excel file
        2. **Fill in** your column definitions:
           - `COLUMN_NAME`: Name of the column
           - `DATA_TYPE`: Data type (VARCHAR, INTEGER, etc.)
           - `NULLABLE`: YES/NO for nullable columns
           - `PRIMARY_KEY`: YES/NO for primary key columns
           - `UNIQUE`: YES/NO for unique constraints
           - `DEFAULT_VALUE`: Default value for the column
           - `DESCRIPTION`: Description of the column
           - `MIN_LENGTH`/`MAX_LENGTH`: Length constraints
           - `MIN_VALUE`/`MAX_VALUE`: Value range constraints
           - `INDEXED`: YES/NO for indexed columns
        
        3. **Upload** the filled template back to the system
        4. **Generate** SQL scripts from your schema
        """)
    
    def generate_create_table_sql(self, table_name: str, database_type: str, schema_source: str = "analyzed"):
        """Generate CREATE TABLE SQL script"""
        try:
            if not table_name.strip():
                st.error("❌ Please enter a table name")
                return
            
            with st.spinner("🔨 Generating SQL script..."):
                if schema_source == "analyzed" and hasattr(st.session_state, 'schema_analysis') and st.session_state.schema_analysis:
                    # Use analyzed schema
                    sql_script = self.sql_generator.generate_create_table_sql(
                        st.session_state.schema_analysis,
                        table_name,
                        database_type
                    )
                    st.success("✅ Using analyzed schema data")
                else:
                    # Use template structure
                    template_schema = self.create_template_schema_analysis()
                    sql_script = self.sql_generator.generate_create_table_sql(
                        template_schema,
                        table_name,
                        database_type
                    )
                    st.info("💡 Using template schema structure")
                
                st.session_state.generated_sql = sql_script
                st.session_state.sql_type = "create_table"
                st.session_state.sql_table_name = table_name
                st.session_state.sql_database_type = database_type
                
                st.success(f"✅ SQL script generated successfully for {database_type.upper()}!")
                st.balloons()
                
        except Exception as e:
            st.error(f"❌ Error generating SQL script: {str(e)}")
    
    def generate_schema_query_sql(self, table_name: str, database_type: str):
        """Generate schema query SQL script"""
        try:
            if not table_name.strip():
                st.error("❌ Please enter a table name")
                return
            
            with st.spinner("🔍 Generating schema query..."):
                sql_script = self.sql_generator.generate_schema_query(table_name, database_type)
                
                st.session_state.generated_sql = sql_script
                st.session_state.sql_type = "schema_query"
                st.session_state.sql_table_name = table_name
                st.session_state.sql_database_type = database_type
                
                st.success(f"✅ Schema query generated successfully for {database_type.upper()}!")
                
        except Exception as e:
            st.error(f"❌ Error generating schema query: {str(e)}")
    
    def download_sql_script(self):
        """Download SQL script as file"""
        try:
            if not hasattr(st.session_state, 'generated_sql') or not st.session_state.generated_sql:
                st.error("❌ No SQL script available to download")
                return
            
            # Generate filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            sql_type = st.session_state.get('sql_type', 'script')
            table_name = st.session_state.get('sql_table_name', 'table')
            db_type = st.session_state.get('sql_database_type', 'mysql')
            
            filename = f"{sql_type}_{table_name}_{db_type}_{timestamp}.sql"
            filepath = self.get_report_path("export", filename)
            
            # Save SQL script
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(st.session_state.generated_sql)
            
            # Provide download button
            with open(filepath, 'r', encoding='utf-8') as f:
                sql_content = f.read()
            
            st.download_button(
                label="📥 Download SQL Script",
                data=sql_content,
                file_name=filename,
                mime="text/plain",
                key=f"download_sql_{timestamp}"
            )
            
            st.success(f"✅ SQL script saved as: {filename}")
            
        except Exception as e:
            st.error(f"❌ Error downloading SQL script: {str(e)}")
    
    def download_schema_template(self):
        """Download schema template Excel file"""
        try:
            with st.spinner("📥 Creating schema template..."):
                # Get template data
                template_data = self.sql_generator.create_schema_template()
                
                # Create DataFrame
                df = pd.DataFrame(template_data)
                
                # Generate filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"schema_template_{timestamp}.xlsx"
                filepath = self.get_report_path("export", filename)
                
                # Save to Excel
                with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                    df.to_excel(writer, sheet_name='Schema_Template', index=False)
                    
                    # Add instructions sheet
                    instructions = {
                        'Field': [
                            'COLUMN_NAME',
                            'DATA_TYPE', 
                            'NULLABLE',
                            'PRIMARY_KEY',
                            'UNIQUE',
                            'DEFAULT_VALUE',
                            'DESCRIPTION',
                            'MIN_LENGTH',
                            'MAX_LENGTH',
                            'MIN_VALUE',
                            'MAX_VALUE',
                            'INDEXED'
                        ],
                        'Description': [
                            'Name of the database column',
                            'Data type (VARCHAR, INTEGER, DATE, etc.)',
                            'YES if column can be NULL, NO otherwise',
                            'YES if column is primary key, NO otherwise',
                            'YES if column has unique constraint, NO otherwise',
                            'Default value for the column',
                            'Description or comment for the column',
                            'Minimum length for text columns',
                            'Maximum length for text columns',
                            'Minimum value for numeric columns',
                            'Maximum value for numeric columns',
                            'YES if column should be indexed, NO otherwise'
                        ],
                        'Example': [
                            'user_id',
                            'INTEGER',
                            'NO',
                            'YES',
                            'YES',
                            'AUTO_INCREMENT',
                            'Unique identifier for user',
                            '',
                            '',
                            '1',
                            '',
                            'YES'
                        ]
                    }
                    
                    instructions_df = pd.DataFrame(instructions)
                    instructions_df.to_excel(writer, sheet_name='Instructions', index=False)
                
                # Provide download button
                with open(filepath, 'rb') as f:
                    excel_data = f.read()
                
                st.download_button(
                    label="📥 Download Schema Template",
                    data=excel_data,
                    file_name=filename,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    key=f"download_template_{timestamp}"
                )
                
                st.success(f"✅ Schema template created: {filename}")
                st.info("💡 Fill in the template and upload it back to generate SQL scripts!")
                
        except Exception as e:
            st.error(f"❌ Error creating schema template: {str(e)}")
    
    def show_template_structure(self):
        """Show template structure"""
        try:
            template_data = self.sql_generator.create_schema_template()
            df = pd.DataFrame(template_data)
            
            st.markdown("### 📋 Template Structure Preview")
            st.dataframe(df, use_container_width=True)
            
            st.markdown("### 📊 Template Statistics")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Columns", len(df))
            
            with col2:
                st.metric("Primary Keys", len(df[df['PRIMARY_KEY'] == 'YES']))
            
            with col3:
                st.metric("Unique Columns", len(df[df['UNIQUE'] == 'YES']))
            
        except Exception as e:
            st.error(f"❌ Error showing template structure: {str(e)}")
    
    def create_template_schema_analysis(self) -> Dict[str, Any]:
        """Create schema analysis from template structure"""
        template_data = self.sql_generator.create_schema_template()
        
        # Convert template data to schema analysis format
        columns = []
        for i in range(len(template_data['COLUMN_NAME'])):
            column = {
                'name': template_data['COLUMN_NAME'][i],
                'data_type': template_data['DATA_TYPE'][i],
                'nullable': template_data['NULLABLE'][i] == 'YES',
                'primary_key': template_data['PRIMARY_KEY'][i] == 'YES',
                'unique': template_data['UNIQUE'][i] == 'YES',
                'indexed': template_data['INDEXED'][i] == 'YES',
                'description': template_data['DESCRIPTION'][i],
                'constraints': {
                    'required': template_data['NULLABLE'][i] == 'NO',
                    'unique': template_data['UNIQUE'][i] == 'YES',
                    'default_value': template_data['DEFAULT_VALUE'][i] if template_data['DEFAULT_VALUE'][i] else None,
                    'min_length': int(template_data['MIN_LENGTH'][i]) if template_data['MIN_LENGTH'][i] else None,
                    'max_length': int(template_data['MAX_LENGTH'][i]) if template_data['MAX_LENGTH'][i] else None,
                    'min_value': float(template_data['MIN_VALUE'][i]) if template_data['MIN_VALUE'][i] else None,
                    'max_value': float(template_data['MAX_VALUE'][i]) if template_data['MAX_VALUE'][i] else None
                }
            }
            columns.append(column)
        
        # Create schema analysis structure
        schema_analysis = {
            'schema_analysis': {
                'table_name': 'template_table',
                'columns': columns,
                'description': 'Template schema structure for SQL generation',
                'total_columns': len(columns),
                'primary_keys': [col for col in columns if col.get('primary_key', False)],
                'unique_columns': [col for col in columns if col.get('unique', False)],
                'indexed_columns': [col for col in columns if col.get('indexed', False)]
            },
            'ndmo_compliance': {
                'overall_score': 0.75,  # Template has good structure
                'category_scores': {
                    'Data Governance': 0.8,
                    'Data Quality': 0.7,
                    'Data Security': 0.6,
                    'Data Architecture': 0.8,
                    'Business Rules': 0.7
                }
            }
        }
        
        return schema_analysis
    
    def show_analyzed_schema_preview(self):
        """Show preview of analyzed schema"""
        try:
            schema_info = st.session_state.schema_analysis.get('schema_analysis', {})
            columns = schema_info.get('columns', [])
            
            if not columns:
                st.warning("No columns found in analyzed schema")
                return
            
            # Create preview data
            preview_data = []
            for col in columns[:10]:  # Show first 10 columns
                preview_data.append({
                    'Column Name': col.get('name', ''),
                    'Data Type': col.get('data_type', ''),
                    'Nullable': 'YES' if col.get('nullable', True) else 'NO',
                    'Primary Key': 'YES' if col.get('primary_key', False) else 'NO',
                    'Unique': 'YES' if col.get('unique', False) else 'NO',
                    'Description': col.get('description', '')[:50] + '...' if len(col.get('description', '')) > 50 else col.get('description', '')
                })
            
            df = pd.DataFrame(preview_data)
            st.dataframe(df, use_container_width=True)
            
            if len(columns) > 10:
                st.caption(f"Showing first 10 of {len(columns)} columns")
            
        except Exception as e:
            st.error(f"Error showing schema preview: {str(e)}")
    
    def show_template_schema_preview(self):
        """Show preview of template schema"""
        try:
            template_data = self.sql_generator.create_schema_template()
            
            # Create preview data
            preview_data = []
            for i in range(len(template_data['COLUMN_NAME'])):
                preview_data.append({
                    'Column Name': template_data['COLUMN_NAME'][i],
                    'Data Type': template_data['DATA_TYPE'][i],
                    'Nullable': template_data['NULLABLE'][i],
                    'Primary Key': template_data['PRIMARY_KEY'][i],
                    'Unique': template_data['UNIQUE'][i],
                    'Description': template_data['DESCRIPTION'][i][:50] + '...' if len(template_data['DESCRIPTION'][i]) > 50 else template_data['DESCRIPTION'][i]
                })
            
            df = pd.DataFrame(preview_data)
            st.dataframe(df, use_container_width=True)
            
            st.caption("Template schema with 10 sample columns")
            
        except Exception as e:
            st.error(f"Error showing template preview: {str(e)}")
    
    def initialize_session_state(self):
        """Initialize session state variables"""
        if 'schema_file' not in st.session_state:
            st.session_state.schema_file = None
        if 'data_file' not in st.session_state:
            st.session_state.data_file = None
        if 'schema_analysis' not in st.session_state:
            st.session_state.schema_analysis = None
        if 'data_processing' not in st.session_state:
            st.session_state.data_processing = None
        if 'problem_analysis' not in st.session_state:
            st.session_state.problem_analysis = None
        if 'processing_stage' not in st.session_state:
            st.session_state.processing_stage = 'upload'
    
    def run_dashboard(self):
        """Run the main dashboard"""
        # Display company header with logo
        self.display_company_header()
        
        # Sidebar
        self.create_sidebar()
        
        # Main content
        self.create_main_content()
    
    def create_sidebar(self):
        """Create enhanced sidebar"""
        with st.sidebar:
            # Enhanced sidebar header
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; margin-bottom: 1.5rem; color: white;">
                <h2 style="margin: 0; font-size: 1.5rem;">🎛️ Control Panel</h2>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;">System Management</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Enhanced file upload section
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 1rem; border-radius: 12px; margin-bottom: 1.5rem;">
                <h3 style="color: #667eea; margin: 0 0 1rem 0; text-align: center;">📁 File Upload</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Schema file upload with enhanced styling
            st.markdown("**📋 Schema Definition**")
            schema_file = st.file_uploader(
                "Choose Schema File",
                type=['xlsx', 'xls'],
                key="schema_upload",
                help="Upload your schema definition file (Excel format)",
                label_visibility="collapsed"
            )
            
            if schema_file is not None:
                st.session_state.schema_file = schema_file
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #00b894 0%, #00a085 100%); color: white; padding: 0.75rem; border-radius: 10px; margin: 0.5rem 0;">
                    <div style="display: flex; align-items: center;">
                        <span style="font-size: 1.2rem; margin-right: 0.5rem;">✅</span>
                        <div>
                            <strong>Schema Uploaded</strong><br>
                            <small>{schema_file.name}</small>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Data file upload with enhanced styling
            st.markdown("**📊 Data File**")
            data_file = st.file_uploader(
                "Choose Data File",
                type=['xlsx', 'xls'],
                key="data_upload",
                help="Upload your data file for processing (Excel format)",
                label_visibility="collapsed"
            )
            
            if data_file is not None:
                st.session_state.data_file = data_file
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #6c5ce7 0%, #5f3dc4 100%); color: white; padding: 0.75rem; border-radius: 10px; margin: 0.5rem 0;">
                    <div style="display: flex; align-items: center;">
                        <span style="font-size: 1.2rem; margin-right: 0.5rem;">✅</span>
                        <div>
                            <strong>Data Uploaded</strong><br>
                            <small>{data_file.name}</small>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Enhanced separator
            st.markdown("""
            <div style="height: 2px; background: linear-gradient(90deg, transparent, #667eea, transparent); margin: 1.5rem 0;"></div>
            """, unsafe_allow_html=True)
            
            # Enhanced processing controls
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 1rem; border-radius: 12px; margin-bottom: 1.5rem;">
                <h3 style="color: #667eea; margin: 0 0 1rem 0; text-align: center;">🔄 Processing Controls</h3>
            </div>
            """, unsafe_allow_html=True)
            
            if st.session_state.schema_file:
            if st.button("🔍 Analyze Schema", type="primary"):
                self.analyze_schema()
            
            if st.session_state.schema_analysis:
                if st.button("🔧 Analyze Problems"):
                    self.analyze_schema_problems()
                
                if st.button("🛡️ Make NDMO Compliant", type="secondary"):
                    self.make_schema_ndmo_compliant()
            
            if st.session_state.data_file and st.session_state.schema_analysis:
                if st.button("⚙️ Process Data", type="primary"):
                    self.process_data()
            
            if st.session_state.schema_file and st.session_state.data_file:
                if st.button("🚀 Complete Analysis", type="secondary"):
                    self.run_complete_analysis()
            
            st.markdown("---")
            
            # Processing status
            st.markdown("### 📊 Processing Status")
            self.display_processing_status()
            
            st.markdown("---")
            
            # System info
            st.markdown("### ℹ️ System Information")
            st.info(f"""
            **Version:** 2.0 Professional  
            **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  
            **Status:** Active  
            **NDMO Standards:** {len(self.ndmo_manager.standards)} Standards
            """)
    
    def display_processing_status(self):
        """Display processing status"""
        status_items = [
            ("📋 Schema Analysis", st.session_state.schema_analysis is not None),
            ("🔧 Problem Analysis", st.session_state.problem_analysis is not None),
            ("⚙️ Data Processing", st.session_state.data_processing is not None),
            ("📊 Quality Assessment", st.session_state.data_processing is not None and "ndmo_compliance" in st.session_state.data_processing)
        ]
        
        for item_name, is_completed in status_items:
            if is_completed:
                st.success(f"✅ {item_name}")
            else:
                st.info(f"⏳ {item_name}")
    
    def create_main_content(self):
        """Create main content area"""
        # Create enhanced tabs with better organization and shorter names
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
            "🏠 Overview", 
            "🔍 Schema", 
            "🔧 Problems",
            "⚙️ Processing",
            "📈 Quality",
            "🔄 Compare",
            "📋 Reports",
            "📁 Files",
            "🗄️ SQL"
        ])
        
        with tab1:
            self.create_overview_tab()
        
        with tab2:
            self.create_schema_analysis_tab()
        
        with tab3:
            self.create_problem_analysis_tab()
        
        with tab4:
            self.create_data_processing_tab()
        
        with tab5:
            self.create_quality_metrics_tab()
        
        with tab6:
            self.create_before_after_comparison_tab()
        
        with tab7:
            self.create_reports_tab()
        
        with tab8:
            self.create_reports_viewer_tab()
        
        with tab9:
            self.create_sql_generator_tab()
    
    def create_overview_tab(self):
        """Create enhanced overview tab"""
        # Welcome section
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="color: #667eea; font-size: 2.2rem; margin-bottom: 0.5rem;">🏠 Dashboard Overview</h2>
            <p style="color: #666; font-size: 1.1rem; margin: 0;">Comprehensive Data Quality & NDMO Compliance Monitoring</p>
        </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.schema_analysis and not st.session_state.data_processing:
            st.markdown("""
            <div style="text-align: center; padding: 3rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 20px; margin: 2rem 0;">
                <div style="font-size: 4rem; margin-bottom: 1rem;">📊</div>
                <h3 style="color: #667eea; margin-bottom: 1rem;">Welcome to SANS Data Quality System</h3>
                <p style="color: #666; font-size: 1.1rem; margin-bottom: 2rem;">Get started by uploading your data and schema files from the sidebar</p>
                <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                    <div style="background: white; padding: 1rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); min-width: 200px;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">📁</div>
                        <h4 style="margin: 0; color: #667eea;">Upload Files</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666; font-size: 0.9rem;">Data & Schema files</p>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); min-width: 200px;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔍</div>
                        <h4 style="margin: 0; color: #667eea;">Analyze</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666; font-size: 0.9rem;">Run quality analysis</p>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); min-width: 200px;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">📈</div>
                        <h4 style="margin: 0; color: #667eea;">Monitor</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666; font-size: 0.9rem;">Track compliance</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            return
        
        # Key metrics with enhanced styling
        self.create_key_metrics()
        
        # Enhanced charts section
        st.markdown("""
        <div style="margin: 2rem 0;">
            <h3 style="color: #667eea; text-align: center; margin-bottom: 1.5rem;">📊 Quality & Compliance Analytics</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            self.create_quality_overview_chart()
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            self.create_compliance_chart()
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Enhanced summary section
        st.markdown("""
        <div style="margin: 2rem 0;">
            <h3 style="color: #667eea; text-align: center; margin-bottom: 1.5rem;">📋 Analysis Summary</h3>
        </div>
        """, unsafe_allow_html=True)
        
        self.create_summary_table()
    
    def create_key_metrics(self):
        """Create enhanced key metrics cards"""
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
            <h3 style="color: #667eea; font-size: 1.8rem; margin-bottom: 1rem;">🎯 Key Performance Indicators</h3>
            <p style="color: #666; font-size: 1rem; margin: 0;">Real-time monitoring of data quality and compliance metrics</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Calculate metrics
        metrics = self.calculate_overview_metrics()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            quality_color = "#00b894" if metrics['data_quality'] >= 0.8 else "#fdcb6e" if metrics['data_quality'] >= 0.6 else "#e17055"
            st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, {quality_color} 0%, {quality_color}dd 100%);">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📊</div>
                <h2 style="font-size: 2.8rem; margin: 0.5rem 0; font-weight: 800;">{metrics['data_quality']:.1%}</h2>
                <h4 style="margin: 0; font-size: 1.1rem; font-weight: 600;">Data Quality</h4>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;">Overall Quality Score</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            compliance_color = "#00b894" if metrics['ndmo_compliance'] >= 0.8 else "#fdcb6e" if metrics['ndmo_compliance'] >= 0.6 else "#e17055"
            st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, {compliance_color} 0%, {compliance_color}dd 100%);">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🛡️</div>
                <h2 style="font-size: 2.8rem; margin: 0.5rem 0; font-weight: 800;">{metrics['ndmo_compliance']:.1%}</h2>
                <h4 style="margin: 0; font-size: 1.1rem; font-weight: 600;">NDMO Compliance</h4>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;">Compliance Score</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #6c5ce7 0%, #5f3dc4 100%);">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📈</div>
                <h2 style="font-size: 2.8rem; margin: 0.5rem 0; font-weight: 800;">{metrics['records_processed']:,}</h2>
                <h4 style="margin: 0; font-size: 1.1rem; font-weight: 600;">Records Processed</h4>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;">Total Records</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            improvement_color = "#00b894" if metrics['improvements_applied'] > 0 else "#74b9ff"
            st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, {improvement_color} 0%, {improvement_color}dd 100%);">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔧</div>
                <h2 style="font-size: 2.8rem; margin: 0.5rem 0; font-weight: 800;">{metrics['improvements_applied']}</h2>
                <h4 style="margin: 0; font-size: 1.1rem; font-weight: 600;">Improvements</h4>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;">Quality Improvements</p>
            </div>
            """, unsafe_allow_html=True)
    
    def calculate_overview_metrics(self):
        """Calculate overview metrics"""
        metrics = {
            'data_quality': 0.0,
            'ndmo_compliance': 0.0,
            'records_processed': 0,
            'improvements_applied': 0
        }
        
        if st.session_state.data_processing:
            processing_data = st.session_state.data_processing
            
            # Data quality
            if 'processed_data' in processing_data and 'quality_metrics' in processing_data['processed_data']:
                metrics['data_quality'] = processing_data['processed_data']['quality_metrics'].get('overall_score', 0.0)
            
            # NDMO compliance
            if 'ndmo_compliance' in processing_data:
                metrics['ndmo_compliance'] = processing_data['ndmo_compliance'].get('overall_score', 0.0)
            
            # Records processed
            if 'processed_data' in processing_data:
                metrics['records_processed'] = processing_data['processed_data'].get('rows', 0)
            
            # Improvements applied
            if 'improvements_applied' in processing_data:
                metrics['improvements_applied'] = len(processing_data['improvements_applied'])
        
        return metrics
    
    def create_quality_overview_chart(self):
        """Create enhanced quality overview chart"""
        st.markdown("""
        <div style="text-align: center; margin-bottom: 1rem;">
            <h4 style="color: #667eea; margin: 0;">📊 Data Quality Distribution</h4>
            <p style="color: #666; font-size: 0.9rem; margin: 0.5rem 0 0 0;">Comprehensive quality metrics analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.data_processing and 'processed_data' in st.session_state.data_processing:
            quality_metrics = st.session_state.data_processing['processed_data']['quality_metrics']
            
            # Create enhanced radar chart
            categories = ['Completeness', 'Uniqueness', 'Validity', 'Consistency', 'Accuracy']
            values = [
                quality_metrics.get('completeness', {}).get('overall', 0.0),
                quality_metrics.get('uniqueness', {}).get('overall', 0.0),
                quality_metrics.get('validity', {}).get('overall', 0.0),
                quality_metrics.get('consistency', {}).get('overall', 0.0),
                quality_metrics.get('accuracy', {}).get('overall', 0.0)
            ]
            
            # Create multiple traces for better visualization
            fig = go.Figure()
            
            # Main quality trace
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                name='Current Quality',
                line_color='#667eea',
                fillcolor='rgba(102, 126, 234, 0.3)',
                line_width=3
            ))
            
            # Target quality trace
            target_values = [0.95] * len(categories)
            fig.add_trace(go.Scatterpolar(
                r=target_values,
                theta=categories,
                fill='toself',
                name='Target Quality',
                line_color='#00b894',
                fillcolor='rgba(0, 184, 148, 0.1)',
                line_width=2,
                line_dash='dash'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 1],
                        tickfont=dict(size=12),
                        gridcolor='rgba(102, 126, 234, 0.2)',
                        linecolor='rgba(102, 126, 234, 0.3)'
                    ),
                    angularaxis=dict(
                        tickfont=dict(size=12, color='#667eea'),
                        linecolor='rgba(102, 126, 234, 0.3)'
                    )
                ),
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                title=dict(
                    text="Data Quality Metrics Analysis",
                    font=dict(size=16, color='#667eea'),
                    x=0.5
                ),
                height=450,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Add quality insights
            avg_quality = sum(values) / len(values)
            quality_status = "Excellent" if avg_quality >= 0.9 else "Good" if avg_quality >= 0.7 else "Needs Improvement"
            status_color = "#00b894" if avg_quality >= 0.9 else "#fdcb6e" if avg_quality >= 0.7 else "#e17055"
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {status_color}20 0%, {status_color}10 100%); padding: 1rem; border-radius: 12px; border-left: 4px solid {status_color}; margin-top: 1rem;">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <h5 style="margin: 0; color: {status_color};">Overall Quality: {avg_quality:.1%}</h5>
                        <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">Status: {quality_status}</p>
                    </div>
                    <div style="font-size: 2rem;">{"🎯" if avg_quality >= 0.9 else "⚠️" if avg_quality >= 0.7 else "🔧"}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 15px;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">No Quality Metrics Available</h4>
                <p style="color: #666; margin: 0;">Please process data to view quality metrics</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_compliance_chart(self):
        """Create enhanced NDMO compliance chart"""
        st.markdown("""
        <div style="text-align: center; margin-bottom: 1rem;">
            <h4 style="color: #667eea; margin: 0;">🛡️ NDMO Compliance Status</h4>
            <p style="color: #666; font-size: 0.9rem; margin: 0.5rem 0 0 0;">Regulatory compliance monitoring</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.data_processing and 'ndmo_compliance' in st.session_state.data_processing:
            compliance_data = st.session_state.data_processing['ndmo_compliance']
            
            # Get actual compliance scores
            overall_score = compliance_data.get('overall_score', 0.0)
            compliant_percentage = overall_score
            non_compliant_percentage = 1.0 - overall_score
            
            # Create enhanced donut chart
            categories = ['Compliant', 'Non-Compliant']
            values = [compliant_percentage, non_compliant_percentage]
            colors = ['#00b894', '#e17055']
            
            fig = go.Figure(data=[go.Pie(
                labels=categories,
                values=values,
                hole=0.4,
                marker_colors=colors,
                textinfo='label+percent',
                textfont_size=14,
                textfont_color='white',
                hovertemplate='<b>%{label}</b><br>Score: %{percent}<br>Value: %{value:.2f}<extra></extra>'
            )])
            
            # Add center text
            fig.add_annotation(
                text=f"<b>{overall_score:.1%}</b><br>Overall<br>Compliance",
                x=0.5, y=0.5,
                font_size=16,
                font_color='#667eea',
                showarrow=False
            )
            
            fig.update_layout(
                title=dict(
                    text="NDMO Compliance Status",
                    font=dict(size=16, color='#667eea'),
                    x=0.5
                ),
                height=450,
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Add compliance insights
            compliance_status = "Fully Compliant" if overall_score >= 0.95 else "Mostly Compliant" if overall_score >= 0.8 else "Partially Compliant" if overall_score >= 0.6 else "Non-Compliant"
            status_color = "#00b894" if overall_score >= 0.95 else "#fdcb6e" if overall_score >= 0.8 else "#e17055" if overall_score >= 0.6 else "#e84393"
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {status_color}20 0%, {status_color}10 100%); padding: 1rem; border-radius: 12px; border-left: 4px solid {status_color}; margin-top: 1rem;">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <h5 style="margin: 0; color: {status_color};">Compliance Status: {compliance_status}</h5>
                        <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">Score: {overall_score:.1%}</p>
                    </div>
                    <div style="font-size: 2rem;">{"🛡️" if overall_score >= 0.95 else "⚠️" if overall_score >= 0.8 else "🔧" if overall_score >= 0.6 else "❌"}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 15px;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🛡️</div>
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">No Compliance Data Available</h4>
                <p style="color: #666; margin: 0;">Please process data to view compliance metrics</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_summary_table(self):
        """Create enhanced summary table"""
        st.markdown("""
        <div style="text-align: center; margin-bottom: 1rem;">
            <h4 style="color: #667eea; margin: 0;">📋 Processing Summary</h4>
            <p style="color: #666; font-size: 0.9rem; margin: 0.5rem 0 0 0;">Comprehensive analysis overview</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.data_processing:
            processing_data = st.session_state.data_processing
            
            # Enhanced summary data with more metrics
            summary_data = {
                'Metric': [
                    '📊 Original Records',
                    '🔄 Processed Records',
                    '📈 Data Quality Score',
                    '🛡️ NDMO Compliance Score',
                    '✅ Quality Improvements',
                    '⚠️ Issues Identified',
                    '🔧 Schema Modifications',
                    '📋 Business Rules Applied'
                ],
                'Value': [
                    f"{processing_data.get('original_records', 0):,}",
                    f"{processing_data.get('processed_records', 0):,}",
                    f"{processing_data.get('data_quality_score', 0.0):.1%}",
                    f"{processing_data.get('ndmo_compliance_score', 0.0):.1%}",
                    f"{len(processing_data.get('improvements_applied', []))}",
                    f"{len(processing_data.get('issues_identified', []))}",
                    f"{len(processing_data.get('schema_modifications', []))}",
                    f"{len(processing_data.get('business_rules_applied', []))}"
                ],
                'Status': [
                    "📁 Source Data",
                    "✅ Processed",
                    "🎯 Quality Target",
                    "🛡️ Compliance Target",
                    "🔧 Applied",
                    "⚠️ Resolved",
                    "📋 Updated",
                    "📝 Implemented"
                ]
            }
            
            # Create enhanced DataFrame with styling
            summary_df = pd.DataFrame(summary_data)
            
            # Display with enhanced styling
            st.markdown("""
            <div style="background: white; border-radius: 15px; padding: 1rem; box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin: 1rem 0;">
            """, unsafe_allow_html=True)
            
            st.dataframe(
                summary_df, 
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Metric": st.column_config.TextColumn(
                        "📊 Metric",
                        help="Analysis metric name",
                        width="medium"
                    ),
                    "Value": st.column_config.TextColumn(
                        "📈 Value",
                        help="Metric value",
                        width="medium"
                    ),
                    "Status": st.column_config.TextColumn(
                        "✅ Status",
                        help="Current status",
                        width="medium"
                    )
                }
            )
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Add processing insights
            if processing_data.get('processing_timestamp'):
                processing_time = processing_data.get('processing_timestamp', 'Unknown')
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea20 0%, #667eea10 100%); padding: 1rem; border-radius: 12px; border-left: 4px solid #667eea; margin-top: 1rem;">
                    <div style="display: flex; align-items: center; justify-content: space-between;">
                        <div>
                            <h5 style="margin: 0; color: #667eea;">Processing Completed</h5>
                            <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">Timestamp: {processing_time}</p>
                        </div>
                        <div style="font-size: 2rem;">✅</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 15px;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📋</div>
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">No Processing Data Available</h4>
                <p style="color: #666; margin: 0;">Please process data to view summary metrics</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_schema_analysis_tab(self):
        """Create schema analysis tab"""
        st.markdown("## 🔍 Schema Analysis")
        
        if not st.session_state.schema_analysis:
            st.warning("⚠️ No schema analysis completed. Please upload a schema file and run analysis.")
            return
        
        schema_data = st.session_state.schema_analysis
        
        # Schema overview
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Schema Sheet", schema_data.get('schema_sheet', 'N/A'))
        
        with col2:
            st.metric("Total Columns", schema_data.get('schema_analysis', {}).get('total_columns', 0))
        
        with col3:
            st.metric("NDMO Compliance", f"{schema_data.get('ndmo_compliance', {}).get('overall_score', 0.0):.1%}")
        
        # Schema details
        st.markdown("### 📊 Schema Details")
        
        if 'schema_analysis' in schema_data and 'columns' in schema_data['schema_analysis']:
            columns_data = []
            for column in schema_data['schema_analysis']['columns']:
                columns_data.append({
                    'Name': column.get('name', ''),
                    'Data Type': column.get('data_type', ''),
                    'Primary Key': 'Yes' if column.get('primary_key', False) else 'No',
                    'Unique': 'Yes' if column.get('unique', False) else 'No',
                    'Nullable': 'Yes' if column.get('nullable', True) else 'No',
                    'Quality Issues': len(column.get('quality_issues', []))
                })
            
            columns_df = pd.DataFrame(columns_data)
            st.dataframe(columns_df, use_container_width=True)
        
        # NDMO compliance details
        st.markdown("### 🛡️ NDMO Compliance Details")
        
        if 'ndmo_compliance' in schema_data:
            compliance = schema_data['ndmo_compliance']
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Overall Score", f"{compliance.get('overall_score', 0.0):.1%}")
                st.metric("Status", compliance.get('status', 'Unknown'))
            
            with col2:
                if 'category_scores' in compliance:
                    for category, score in compliance['category_scores'].items():
                        st.metric(category, f"{score:.1%}")
        
        # Recommendations
        st.markdown("### 💡 Recommendations")
        
        if 'recommendations' in schema_data:
            for recommendation in schema_data['recommendations']:
                st.info(f"• {recommendation}")
    
    def create_problem_analysis_tab(self):
        """Create problem analysis tab"""
        st.markdown("## 🔧 Schema Problem Analysis")
        
        if not st.session_state.problem_analysis:
            st.warning("⚠️ No problem analysis completed. Please run problem analysis from the sidebar.")
            return
        
        problem_data = st.session_state.problem_analysis
        
        # Problem summary
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Critical Problems", len(problem_data.get("critical_problems", [])))
        
        with col2:
            st.metric("Major Problems", len(problem_data.get("major_problems", [])))
        
        with col3:
            st.metric("Minor Problems", len(problem_data.get("minor_problems", [])))
        
        # Critical problems
        if problem_data.get("critical_problems"):
            st.markdown("### 🚨 Critical Problems")
            for problem in problem_data["critical_problems"]:
                with st.expander(f"❌ {problem['name']} ({problem['id']})"):
                    st.error(f"**Impact:** {problem['impact']}")
                    st.write(f"**Description:** {problem['description']}")
                    st.success(f"**Solution:** {problem['solution']}")
                    st.info(f"**Example:** {problem['example']}")
        
        # Major problems
        if problem_data.get("major_problems"):
            st.markdown("### ⚠️ Major Problems")
            for problem in problem_data["major_problems"]:
                with st.expander(f"⚠️ {problem['name']} ({problem['id']})"):
                    st.warning(f"**Impact:** {problem['impact']}")
                    st.write(f"**Description:** {problem['description']}")
                    st.success(f"**Solution:** {problem['solution']}")
                    st.info(f"**Example:** {problem['example']}")
        
        # Minor problems
        if problem_data.get("minor_problems"):
            st.markdown("### ℹ️ Minor Problems")
            for problem in problem_data["minor_problems"]:
                with st.expander(f"ℹ️ {problem['name']} ({problem['id']})"):
                    st.info(f"**Impact:** {problem['impact']}")
                    st.write(f"**Description:** {problem['description']}")
                    st.success(f"**Solution:** {problem['solution']}")
                    st.info(f"**Example:** {problem['example']}")
        
        # Correction plan
        if problem_data.get("correction_plan"):
            st.markdown("### 📋 Correction Plan")
            correction_plan = problem_data["correction_plan"]
            
            # Immediate actions
            if correction_plan.get("immediate_actions"):
                st.markdown("#### 🚨 Immediate Actions (Critical)")
                for action in correction_plan["immediate_actions"]:
                    st.error(f"**{action['problem_id']}:** {action['action']}")
            
            # Short-term actions
            if correction_plan.get("short_term_actions"):
                st.markdown("#### ⚠️ Short-term Actions (Major)")
                for action in correction_plan["short_term_actions"]:
                    st.warning(f"**{action['problem_id']}:** {action['action']}")
            
            # Long-term actions
            if correction_plan.get("long_term_actions"):
                st.markdown("#### ℹ️ Long-term Actions (Minor)")
                for action in correction_plan["long_term_actions"]:
                    st.info(f"**{action['problem_id']}:** {action['action']}")
            
            # Effort estimation
            if correction_plan.get("estimated_effort"):
                effort = correction_plan["estimated_effort"]
                st.markdown("#### ⏱️ Effort Estimation")
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Immediate", f"{effort.get('immediate', 0)}h")
                
                with col2:
                    st.metric("Short-term", f"{effort.get('short_term', 0)}h")
                
                with col3:
                    st.metric("Long-term", f"{effort.get('long_term', 0)}h")
                
                with col4:
                    st.metric("Total", f"{effort.get('total', 0)}h")
        
        # Priority actions
        if problem_data.get("priority_actions"):
            st.markdown("### 🎯 Priority Actions")
            priority_df = pd.DataFrame(problem_data["priority_actions"])
            st.dataframe(priority_df, use_container_width=True)
    
    def create_data_processing_tab(self):
        """Create data processing tab"""
        st.markdown("## ⚙️ Data Processing")
        
        if not st.session_state.data_processing:
            st.warning("⚠️ No data processing completed. Please upload files and run processing.")
            return
        
        processing_data = st.session_state.data_processing
        
        # Processing overview
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Original Records", processing_data.get('original_data', {}).get('rows', 0))
        
        with col2:
            st.metric("Processed Records", processing_data.get('processed_data', {}).get('rows', 0))
        
        with col3:
            st.metric("Quality Improvement", f"{processing_data.get('processed_data', {}).get('quality_metrics', {}).get('overall_score', 0.0):.1%}")
        
        # Quality metrics comparison
        st.markdown("### 📊 Quality Metrics Comparison")
        
        if 'original_data' in processing_data and 'processed_data' in processing_data:
            original_quality = processing_data['original_data'].get('quality_metrics', {})
            processed_quality = processing_data['processed_data'].get('quality_metrics', {})
            
            comparison_data = {
                'Metric': ['Completeness', 'Uniqueness', 'Validity', 'Overall Score'],
                'Before': [
                    original_quality.get('completeness', {}).get('overall', 0.0),
                    original_quality.get('uniqueness', {}).get('overall', 0.0),
                    original_quality.get('validity', {}).get('overall', 0.0),
                    original_quality.get('overall_score', 0.0)
                ],
                'After': [
                    processed_quality.get('completeness', {}).get('overall', 0.0),
                    processed_quality.get('uniqueness', {}).get('overall', 0.0),
                    processed_quality.get('validity', {}).get('overall', 0.0),
                    processed_quality.get('overall_score', 0.0)
                ]
            }
            
            comparison_df = pd.DataFrame(comparison_data)
            st.dataframe(comparison_df, use_container_width=True)
        
        # Improvements applied
        st.markdown("### 🔧 Improvements Applied")
        
        if 'improvements_applied' in processing_data:
            for improvement in processing_data['improvements_applied']:
                st.success(f"✅ {improvement}")
        else:
            st.info("No improvements applied")
    
    def create_quality_metrics_tab(self):
        """Create quality metrics tab"""
        st.markdown("## 📈 Quality Metrics")
        
        if not st.session_state.data_processing:
            st.warning("⚠️ No quality metrics available. Please run data processing first.")
            return
        
        processing_data = st.session_state.data_processing
        
        # Quality metrics charts
        if 'processed_data' in processing_data and 'quality_metrics' in processing_data['processed_data']:
            quality_metrics = processing_data['processed_data']['quality_metrics']
            
            # Create quality metrics chart
            metrics = ['Completeness', 'Uniqueness', 'Validity']
            values = [
                quality_metrics.get('completeness', {}).get('overall', 0.0),
                quality_metrics.get('uniqueness', {}).get('overall', 0.0),
                quality_metrics.get('validity', {}).get('overall', 0.0)
            ]
            
            fig = go.Figure(data=[
                go.Bar(
                    x=metrics,
                    y=values,
                    text=[f"{v:.1%}" for v in values],
                    textposition='auto',
                    marker_color=['#4facfe', '#00f2fe', '#43e97b']
                )
            ])
            
            fig.update_layout(
                title="Quality Metrics Overview",
                xaxis_title="Metric",
                yaxis_title="Score",
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # NDMO compliance details
        st.markdown("### 🛡️ NDMO Compliance Details")
        
        if 'ndmo_compliance' in processing_data:
            compliance = processing_data['ndmo_compliance']
            
            # Compliance status
            status = compliance.get('status', 'unknown')
            if status == 'compliant':
                st.markdown('<div class="status-card status-success"><h4>✅ COMPLIANT</h4><p>Data meets NDMO standards</p></div>', unsafe_allow_html=True)
            elif status == 'non_compliant':
                st.markdown('<div class="status-card status-danger"><h4>❌ NON-COMPLIANT</h4><p>Data does not meet NDMO standards</p></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="status-card status-warning"><h4>⚠️ PARTIALLY COMPLIANT</h4><p>Data partially meets NDMO standards</p></div>', unsafe_allow_html=True)
            
            # Compliance score
            st.metric("Compliance Score", f"{compliance.get('overall_score', 0.0):.1%}")
            
            # Critical failures
            if 'critical_failures' in compliance and compliance['critical_failures']:
                st.error(f"Critical Failures: {', '.join(compliance['critical_failures'])}")
            
            # Recommendations
            if 'recommendations' in compliance:
                st.markdown("#### 💡 Recommendations")
                for recommendation in compliance['recommendations']:
                    st.info(f"• {recommendation}")
    
    def create_before_after_comparison_tab(self):
        """Create before/after comparison tab"""
        st.markdown("## 🔄 Schema Before/After Comparison")
        
        if not hasattr(st.session_state, 'schema_comparison') or not st.session_state.schema_comparison:
            st.warning("⚠️ No schema comparison available. Please make schema NDMO compliant first.")
            return
        
        comparison = st.session_state.schema_comparison
        summary = comparison.get("summary", {})
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Original Columns", 
                summary.get("original_columns", 0),
                delta=None
            )
        
        with col2:
            st.metric(
                "Compliant Columns", 
                summary.get("compliant_columns", 0),
                delta=f"+{summary.get('added_columns', 0)}"
            )
        
        with col3:
            original_compliance = summary.get("original_compliance", 0)
            st.metric(
                "Original Compliance", 
                f"{original_compliance:.1%}",
                delta=None
            )
        
        with col4:
            compliant_compliance = summary.get("compliant_compliance", 0)
            improvement = summary.get("improvement", 0)
            st.metric(
                "Compliant Compliance", 
                f"{compliant_compliance:.1%}",
                delta=f"+{improvement:.1%}"
            )
        
        # Detailed comparison
        st.markdown("### 📋 Detailed Changes")
        
        # Added columns
        if comparison.get("added_columns"):
            st.markdown("#### ➕ Added Columns")
            added_df = pd.DataFrame(comparison["added_columns"])
            st.dataframe(added_df, use_container_width=True)
        
        # Modified columns
        if comparison.get("modified_columns"):
            st.markdown("#### 🔄 Modified Columns")
            for col in comparison["modified_columns"]:
                with st.expander(f"🔧 {col['name']}"):
                    for change in col["changes"]:
                        st.write(f"• {change}")
        
        # Compliance improvements
        if comparison.get("compliance_improvements"):
            st.markdown("### 🛡️ NDMO Compliance Improvements")
            improvements_df = pd.DataFrame(comparison["compliance_improvements"])
            st.dataframe(improvements_df, use_container_width=True)
        
        # Visual comparison
        st.markdown("### 📊 Visual Comparison")
        
        # Compliance comparison chart
        compliance_data = {
            "Metric": ["Original Compliance", "Compliant Compliance"],
            "Score": [summary.get("original_compliance", 0), summary.get("compliant_compliance", 0)]
        }
        
        compliance_df = pd.DataFrame(compliance_data)
        st.bar_chart(compliance_df.set_index("Metric"))
        
        # Column count comparison
        column_data = {
            "Type": ["Original", "Added", "Modified", "Unchanged"],
            "Count": [
                summary.get("original_columns", 0),
                summary.get("added_columns", 0),
                summary.get("modified_columns", 0),
                summary.get("unchanged_columns", 0)
            ]
        }
        
        column_df = pd.DataFrame(column_data)
        st.bar_chart(column_df.set_index("Type"))
    
    def create_reports_tab(self):
        """Create enhanced reports tab with organized layout"""
        # Enhanced header
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="color: #667eea; font-size: 2.2rem; margin-bottom: 0.5rem;">📋 Reports & Export Center</h2>
            <p style="color: #666; font-size: 1.1rem; margin: 0;">Professional reporting and data export tools</p>
        </div>
        """, unsafe_allow_html=True)
        
        # System Status Overview
        self.create_system_status_overview()
        
        # Main Export Sections
        st.markdown("""
        <div style="margin: 2rem 0;">
            <h3 style="color: #667eea; text-align: center; margin-bottom: 1.5rem;">📊 Export & Report Generation</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Section 1: Analysis Reports
        self.create_analysis_reports_section()
        
        # Section 2: Quality & Compliance Reports
        self.create_quality_compliance_section()
        
        # Section 3: Technical Documentation
        self.create_technical_documentation_section()
        
        # Section 4: File Management
        self.create_file_management_section()
    
    def create_system_status_overview(self):
        """Create system status overview section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;">
            <h4 style="color: #667eea; margin: 0 0 1rem 0; text-align: center;">🔍 System Status Overview</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            # Schema Status
            if hasattr(st.session_state, 'schema_analysis') and st.session_state.schema_analysis:
                status_color = "#00b894"
                status_icon = "✅"
                status_text = "Analyzed"
            else:
                status_color = "#e17055"
                status_icon = "⚠️"
                status_text = "Not Analyzed"
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {status_color}20 0%, {status_color}10 100%); padding: 1rem; border-radius: 12px; text-align: center; border-left: 4px solid {status_color};">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{status_icon}</div>
                <h5 style="margin: 0; color: {status_color};">Schema Analysis</h5>
                <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{status_text}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Data Processing Status
            if hasattr(st.session_state, 'data_processing') and st.session_state.data_processing:
                status_color = "#00b894"
                status_icon = "✅"
                status_text = "Processed"
            else:
                status_color = "#e17055"
                status_icon = "⚠️"
                status_text = "Not Processed"
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {status_color}20 0%, {status_color}10 100%); padding: 1rem; border-radius: 12px; text-align: center; border-left: 4px solid {status_color};">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{status_icon}</div>
                <h5 style="margin: 0; color: {status_color};">Data Processing</h5>
                <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{status_text}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            # NDMO Compliance Status
            if hasattr(st.session_state, 'compliant_schema') and st.session_state.compliant_schema:
                compliance_score = st.session_state.compliant_schema.get('ndmo_compliance', {}).get('overall_score', 0)
                if compliance_score >= 0.8:
                    status_color = "#00b894"
                    status_icon = "🛡️"
                    status_text = f"{compliance_score:.1%} Compliant"
                else:
                    status_color = "#fdcb6e"
                    status_icon = "⚠️"
                    status_text = f"{compliance_score:.1%} Partial"
            else:
                status_color = "#e17055"
                status_icon = "❌"
                status_text = "Not Compliant"
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {status_color}20 0%, {status_color}10 100%); padding: 1rem; border-radius: 12px; text-align: center; border-left: 4px solid {status_color};">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{status_icon}</div>
                <h5 style="margin: 0; color: {status_color};">NDMO Compliance</h5>
                <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{status_text}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            # Quality Score Status
            if hasattr(st.session_state, 'data_processing') and st.session_state.data_processing:
                quality_score = st.session_state.data_processing.get('processed_data', {}).get('quality_metrics', {}).get('overall_score', 0)
                if quality_score >= 0.8:
                    status_color = "#00b894"
                    status_icon = "🎯"
                    status_text = f"{quality_score:.1%} Quality"
                else:
                    status_color = "#fdcb6e"
                    status_icon = "📊"
                    status_text = f"{quality_score:.1%} Quality"
            else:
                status_color = "#e17055"
                status_icon = "❓"
                status_text = "No Data"
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {status_color}20 0%, {status_color}10 100%); padding: 1rem; border-radius: 12px; text-align: center; border-left: 4px solid {status_color};">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{status_icon}</div>
                <h5 style="margin: 0; color: {status_color};">Data Quality</h5>
                <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{status_text}</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_analysis_reports_section(self):
        """Create analysis reports section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea20 0%, #667eea10 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem; border-left: 4px solid #667eea;">
            <h4 style="color: #667eea; margin: 0 0 1rem 0;">🔍 Analysis Reports</h4>
            <p style="color: #666; margin: 0; font-size: 0.95rem;">Export detailed analysis results and findings</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📊 Export Schema Analysis", type="primary", use_container_width=True):
                self.export_schema_analysis()
        
        with col2:
            if st.button("🔧 Export Problem Analysis", type="secondary", use_container_width=True):
                self.export_problem_analysis()
        
        with col3:
            if st.button("📈 Export Quality Report", type="secondary", use_container_width=True):
                self.export_quality_report()
        
    def create_quality_compliance_section(self):
        """Create quality and compliance section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #00b89420 0%, #00b89410 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem; border-left: 4px solid #00b894;">
            <h4 style="color: #00b894; margin: 0 0 1rem 0;">🛡️ Quality & Compliance Reports</h4>
            <p style="color: #666; margin: 0; font-size: 0.95rem;">Generate compliance reports and export processed data</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            disabled = not (hasattr(st.session_state, 'compliant_schema') and st.session_state.compliant_schema)
            if st.button("📋 Export Compliant Schema", type="primary", use_container_width=True, disabled=disabled):
                self.export_compliant_schema()
        
        with col2:
            if st.button("📊 Export Processed Data", type="secondary", use_container_width=True):
                self.export_processed_data()
        
        with col3:
            if st.button("📄 Generate HTML Report", type="secondary", use_container_width=True):
                self.generate_html_report()
    
    def create_technical_documentation_section(self):
        """Create technical documentation section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #6c5ce720 0%, #6c5ce710 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem; border-left: 4px solid #6c5ce7;">
            <h4 style="color: #6c5ce7; margin: 0 0 1rem 0;">👨‍💻 Technical Documentation</h4>
            <p style="color: #666; margin: 0; font-size: 0.95rem;">Generate technical reports and implementation guides</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📋 Generate Technical Report", type="primary", use_container_width=True):
                self.generate_technical_report()
        
        with col2:
            if st.button("🔧 Implementation Guide", type="secondary", use_container_width=True):
                self.generate_implementation_guide()
    
    def create_file_management_section(self):
        """Create file management section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fdcb6e20 0%, #fdcb6e10 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem; border-left: 4px solid #fdcb6e;">
            <h4 style="color: #fdcb6e; margin: 0 0 1rem 0;">📁 File Management</h4>
            <p style="color: #666; margin: 0; font-size: 0.95rem;">Manage exported files and re-analyze data</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show exported files status
        if hasattr(st.session_state, 'exported_schema_file') or hasattr(st.session_state, 'exported_data_file'):
            st.markdown("### 📁 Exported Files Status")
            col1, col2 = st.columns(2)
            
            with col1:
                if hasattr(st.session_state, 'exported_schema_file'):
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #00b89420 0%, #00b89410 100%); padding: 1rem; border-radius: 12px; border-left: 4px solid #00b894;">
                        <div style="display: flex; align-items: center;">
                            <span style="font-size: 1.5rem; margin-right: 0.5rem;">📋</span>
                            <div>
                                <h6 style="margin: 0; color: #00b894;">Schema File Exported</h6>
                                <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{st.session_state.exported_schema_file}</p>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    # Show file size if possible
                    try:
                        import os
                        if os.path.exists(st.session_state.exported_schema_file):
                            size = os.path.getsize(st.session_state.exported_schema_file)
                            st.caption(f"📏 Size: {size:,} bytes")
                    except:
                        pass
                else:
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1rem; border-radius: 12px; border-left: 4px solid #e17055;">
                        <div style="display: flex; align-items: center;">
                            <span style="font-size: 1.5rem; margin-right: 0.5rem;">📋</span>
                            <div>
                                <h6 style="margin: 0; color: #e17055;">No Schema File Exported</h6>
                                <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">Export compliant schema first</p>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                if hasattr(st.session_state, 'exported_data_file'):
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #6c5ce720 0%, #6c5ce710 100%); padding: 1rem; border-radius: 12px; border-left: 4px solid #6c5ce7;">
                        <div style="display: flex; align-items: center;">
                            <span style="font-size: 1.5rem; margin-right: 0.5rem;">📊</span>
                            <div>
                                <h6 style="margin: 0; color: #6c5ce7;">Data File Exported</h6>
                                <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{st.session_state.exported_data_file}</p>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    # Show file size if possible
                    try:
                        import os
                        if os.path.exists(st.session_state.exported_data_file):
                            size = os.path.getsize(st.session_state.exported_data_file)
                            st.caption(f"📏 Size: {size:,} bytes")
                    except:
                        pass
                else:
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1rem; border-radius: 12px; border-left: 4px solid #e17055;">
                        <div style="display: flex; align-items: center;">
                            <span style="font-size: 1.5rem; margin-right: 0.5rem;">📊</span>
                            <div>
                                <h6 style="margin: 0; color: #e17055;">No Data File Exported</h6>
                                <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">Export processed data first</p>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # File management actions
        col1, col2 = st.columns(2)
        
        with col1:
            disabled = not (hasattr(st.session_state, 'exported_schema_file') and hasattr(st.session_state, 'exported_data_file'))
            if st.button("🔄 Re-analyze Exported Files", type="primary", use_container_width=True, disabled=disabled):
                self.reanalyze_exported_files()
        
        with col2:
            if st.button("📁 View Saved Reports", type="secondary", use_container_width=True):
                st.info("💡 Use the 'Saved Reports' tab to view all generated reports")
        
        # Enhanced report previews
        if hasattr(st.session_state, 'schema_analysis') and st.session_state.schema_analysis:
            st.markdown("### 🔍 Schema Analysis Preview")
            with st.expander("📊 View Schema Analysis Details", expanded=False):
                st.markdown("""
                <div style="background: white; padding: 1rem; border-radius: 10px; border: 1px solid #e9ecef;">
                """, unsafe_allow_html=True)
                st.json(st.session_state.schema_analysis)
                st.markdown("</div>", unsafe_allow_html=True)
        
        if hasattr(st.session_state, 'data_processing') and st.session_state.data_processing:
            st.markdown("### ⚙️ Data Processing Preview")
            with st.expander("📈 View Processing Results", expanded=False):
                st.markdown("""
                <div style="background: white; padding: 1rem; border-radius: 10px; border: 1px solid #e9ecef;">
                """, unsafe_allow_html=True)
                st.json(st.session_state.data_processing)
                st.markdown("</div>", unsafe_allow_html=True)
    
    def analyze_schema(self):
        """Enhanced schema analysis with better UI feedback"""
        if not st.session_state.schema_file:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #e17055; margin: 1rem 0;">
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 2rem; margin-right: 1rem;">❌</span>
                    <div>
                        <h4 style="margin: 0; color: #e17055;">No Schema File Uploaded</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666;">Please upload a schema file from the sidebar to begin analysis</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            return
        
        # Save uploaded file temporarily
        temp_file = self.save_uploaded_file(st.session_state.schema_file)
        
        try:
            # Enhanced progress indicator
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.markdown("""
            <div style="background: linear-gradient(135deg, #667eea20 0%, #667eea10 100%); padding: 1rem; border-radius: 12px; border-left: 4px solid #667eea; margin: 1rem 0;">
                <div style="display: flex; align-items: center;">
                    <div class="loading-spinner" style="margin-right: 1rem;"></div>
                    <div>
                        <h5 style="margin: 0; color: #667eea;">🔍 Analyzing Schema...</h5>
                        <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">Processing schema structure and validation rules</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            progress_bar.progress(25)
            
            # Analyze schema
            schema_analysis = self.schema_analyzer.analyze_schema_file(temp_file)
            
            progress_bar.progress(75)
            
            if "error" not in schema_analysis:
                st.session_state.schema_analysis = schema_analysis
            progress_bar.progress(100)
            
            # Enhanced success message
            columns_count = len(schema_analysis.get('schema_analysis', {}).get('columns', []))
            compliance_score = schema_analysis.get('ndmo_compliance', {}).get('overall_score', 0)
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #00b89420 0%, #00b89410 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #00b894; margin: 1rem 0;">
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 2rem; margin-right: 1rem;">✅</span>
                    <div>
                        <h4 style="margin: 0; color: #00b894;">Schema Analysis Completed Successfully!</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666;">
                            📊 Found {columns_count} columns | 🛡️ NDMO Compliance: {compliance_score:.1%}
                        </p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()
            
        else:
            progress_bar.empty()
            status_text.empty()
            
            # Enhanced error message
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #e17055; margin: 1rem 0;">
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 2rem; margin-right: 1rem;">❌</span>
                    <div>
                        <h4 style="margin: 0; color: #e17055;">Schema Analysis Failed</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666;">{schema_analysis['error']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        except Exception as e:
            # Enhanced exception handling
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #e17055; margin: 1rem 0;">
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 2rem; margin-right: 1rem;">⚠️</span>
                    <div>
                        <h4 style="margin: 0; color: #e17055;">Analysis Error</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666;">{str(e)}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        finally:
            # Clean up temporary file
            if os.path.exists(temp_file):
                os.remove(temp_file)
    
    def analyze_schema_problems(self):
        """Analyze schema problems"""
        if not st.session_state.schema_analysis:
            st.error("❌ No schema analysis available")
            return
        
        try:
            with st.spinner("🔧 Analyzing schema problems..."):
                # Analyze problems
                problem_analysis = self.problem_analyzer.analyze_schema_problems(st.session_state.schema_analysis)
                
                if problem_analysis:
                    st.session_state.problem_analysis = problem_analysis
                    st.success("✅ Schema problem analysis completed successfully!")
                else:
                    st.error("❌ Problem analysis failed")
        
        except Exception as e:
            st.error(f"❌ Error analyzing problems: {str(e)}")
    
    def make_schema_ndmo_compliant(self):
        """Enhanced NDMO compliance with progress tracking"""
        if not st.session_state.schema_analysis:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #e17055; margin: 1rem 0;">
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 2rem; margin-right: 1rem;">❌</span>
                    <div>
                        <h4 style="margin: 0; color: #e17055;">No Schema Analysis Available</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666;">Please analyze the schema first before making it NDMO compliant</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            return
        
        try:
            # Create NDMO compliance progress UI
            st.markdown("""
            <div style="background: linear-gradient(135deg, #00b89420 0%, #00b89410 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #00b894; margin: 1rem 0;">
                <h4 style="margin: 0 0 1rem 0; color: #00b894;">🛡️ NDMO Compliance Enhancement</h4>
                <p style="margin: 0; color: #666; font-size: 0.95rem;">Applying NDMO standards and compliance requirements to schema</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Progress tracking
            compliance_progress = st.progress(0)
            compliance_status = st.empty()
            
            # NDMO compliance steps
            compliance_steps = [
                {"name": "📋 Schema Backup", "description": "Creating backup of original schema", "progress": 10},
                {"name": "🔍 Compliance Analysis", "description": "Analyzing current compliance status", "progress": 25},
                {"name": "🔧 Primary Key Enhancement", "description": "Adding and validating primary keys", "progress": 40},
                {"name": "📊 Audit Trail Fields", "description": "Adding audit trail and metadata fields", "progress": 55},
                {"name": "🛠️ Data Type Optimization", "description": "Optimizing data types for NDMO standards", "progress": 70},
                {"name": "🛡️ Security & Constraints", "description": "Adding security fields and constraints", "progress": 85},
                {"name": "✅ Compliance Validation", "description": "Validating final NDMO compliance", "progress": 100}
            ]
            
            # Process each compliance step
            for i, step in enumerate(compliance_steps):
                compliance_status.markdown(f"""
                <div style="background: white; padding: 1rem; border-radius: 10px; border: 1px solid #e9ecef; margin: 0.5rem 0;">
                    <div style="display: flex; align-items: center;">
                        <div class="loading-spinner" style="margin-right: 1rem;"></div>
                        <div>
                            <h5 style="margin: 0; color: #00b894;">{step['name']}</h5>
                            <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{step['description']}</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                compliance_progress.progress(step['progress'] / 100)
                
                # Simulate processing time
                import time
                time.sleep(0.4)
            
            # Clear status
            compliance_status.empty()
            compliance_progress.empty()
            
            # Execute actual compliance processing
            with st.spinner("🔄 Executing NDMO compliance enhancement..."):
                from schema_problem_analyzer import SchemaNDMOComplianceProcessor
                
                # Store original schema for comparison
                original_schema = st.session_state.schema_analysis.copy()
                st.session_state.original_schema = original_schema
                
                processor = SchemaNDMOComplianceProcessor()
                compliant_schema = processor.make_schema_ndmo_compliant(st.session_state.schema_analysis)
                
                # Store compliant schema
                st.session_state.compliant_schema = compliant_schema
                
                # Update session state with compliant schema
                st.session_state.schema_analysis = compliant_schema
                
                # Re-analyze NDMO compliance
                ndmo_manager = NDMOStandardsManager()
                compliance = ndmo_manager.validate_schema_compliance(compliant_schema)
                st.session_state.schema_analysis["ndmo_compliance"] = compliance
                
                # Generate comparison report
                comparison_report = self.generate_schema_comparison_report(original_schema, compliant_schema)
                st.session_state.schema_comparison = comparison_report
                
                # Enhanced success message with compliance statistics
                original_compliance = original_schema.get('ndmo_compliance', {}).get('overall_score', 0)
                new_compliance = compliance.get('overall_score', 0)
                improvement = new_compliance - original_compliance
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #00b89420 0%, #00b89410 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #00b894; margin: 1rem 0;">
                    <div style="display: flex; align-items: center;">
                        <span style="font-size: 2rem; margin-right: 1rem;">✅</span>
                        <div>
                            <h4 style="margin: 0; color: #00b894;">Schema Made NDMO Compliant Successfully!</h4>
                            <div style="margin: 0.5rem 0 0 0; color: #666;">
                                <p style="margin: 0.25rem 0; font-size: 0.9rem;">📊 Original Compliance: {original_compliance:.1%}</p>
                                <p style="margin: 0.25rem 0; font-size: 0.9rem;">🛡️ New Compliance: {new_compliance:.1%}</p>
                                <p style="margin: 0.25rem 0; font-size: 0.9rem;">📈 Improvement: +{improvement:.1%}</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.balloons()
                
        except Exception as e:
            st.error(f"❌ Error making schema NDMO compliant: {str(e)}")
    
    def generate_schema_comparison_report(self, original_schema: dict, compliant_schema: dict) -> dict:
        """Generate detailed comparison report between original and compliant schemas"""
        original_columns = original_schema.get("schema_analysis", {}).get("columns", [])
        compliant_columns = compliant_schema.get("schema_analysis", {}).get("columns", [])
        
        # Calculate changes
        added_columns = []
        modified_columns = []
        unchanged_columns = []
        
        original_column_names = {col.get("name", ""): col for col in original_columns}
        compliant_column_names = {col.get("name", ""): col for col in compliant_columns}
        
        # Find added columns
        for col_name, col_data in compliant_column_names.items():
            if col_name not in original_column_names:
                added_columns.append({
                    "name": col_name,
                    "data_type": col_data.get("data_type", ""),
                    "ndmo_standard": col_data.get("ndmo_standard", ""),
                    "description": col_data.get("description", ""),
                    "change_type": "added"
                })
        
        # Find modified and unchanged columns
        for col_name, original_col in original_column_names.items():
            if col_name in compliant_column_names:
                compliant_col = compliant_column_names[col_name]
                
                # Check for modifications
                changes = []
                if original_col.get("data_type") != compliant_col.get("data_type"):
                    changes.append(f"Data type: {original_col.get('data_type')} → {compliant_col.get('data_type')}")
                
                if original_col.get("nullable") != compliant_col.get("nullable"):
                    changes.append(f"Nullable: {original_col.get('nullable')} → {compliant_col.get('nullable')}")
                
                if original_col.get("primary_key") != compliant_col.get("primary_key"):
                    changes.append(f"Primary key: {original_col.get('primary_key')} → {compliant_col.get('primary_key')}")
                
                if changes:
                    modified_columns.append({
                        "name": col_name,
                        "changes": changes,
                        "change_type": "modified"
                    })
                else:
                    unchanged_columns.append({
                        "name": col_name,
                        "change_type": "unchanged"
                    })
        
        # Calculate compliance improvements
        original_compliance = original_schema.get("ndmo_compliance", {}).get("overall_score", 0)
        compliant_compliance = compliant_schema.get("ndmo_compliance", {}).get("overall_score", 0)
        
        return {
            "summary": {
                "original_columns": len(original_columns),
                "compliant_columns": len(compliant_columns),
                "added_columns": len(added_columns),
                "modified_columns": len(modified_columns),
                "unchanged_columns": len(unchanged_columns),
                "original_compliance": original_compliance,
                "compliant_compliance": compliant_compliance,
                "improvement": compliant_compliance - original_compliance
            },
            "added_columns": added_columns,
            "modified_columns": modified_columns,
            "unchanged_columns": unchanged_columns,
            "compliance_improvements": compliant_schema.get("schema_analysis", {}).get("compliance_improvements", [])
        }
    
    def process_data(self):
        """Enhanced data processing with detailed progress tracking"""
        if not st.session_state.data_file:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #e17055; margin: 1rem 0;">
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 2rem; margin-right: 1rem;">❌</span>
                    <div>
                        <h4 style="margin: 0; color: #e17055;">No Data File Uploaded</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666;">Please upload a data file from the sidebar to begin processing</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            return
        
        if not st.session_state.schema_analysis:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #e17055; margin: 1rem 0;">
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 2rem; margin-right: 1rem;">⚠️</span>
                    <div>
                        <h4 style="margin: 0; color: #e17055;">No Schema Analysis Available</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666;">Please analyze the schema first before processing data</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            return
        
        # Save uploaded files temporarily
        data_temp_file = self.save_uploaded_file(st.session_state.data_file)
        schema_temp_file = self.save_uploaded_file(st.session_state.schema_file) if st.session_state.schema_file else None
        
        try:
            # Create progress tracking UI
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea20 0%, #667eea10 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #667eea; margin: 1rem 0;">
                <h4 style="margin: 0 0 1rem 0; color: #667eea;">⚙️ Data Processing Pipeline</h4>
                <p style="margin: 0; color: #666; font-size: 0.95rem;">Processing data according to schema requirements with quality improvements</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Main progress bar
            main_progress = st.progress(0)
            status_container = st.empty()
            
            # Pipeline steps
            pipeline_steps = [
                {"name": "📁 Loading Data File", "description": "Reading and validating data file structure", "progress": 10},
                {"name": "🔍 Schema Validation", "description": "Validating data against schema requirements", "progress": 25},
                {"name": "🔧 Data Type Conversion", "description": "Converting data types according to schema", "progress": 40},
                {"name": "📊 Quality Analysis", "description": "Analyzing data quality metrics", "progress": 55},
                {"name": "🛠️ Quality Improvements", "description": "Applying data quality enhancements", "progress": 70},
                {"name": "🛡️ NDMO Compliance Check", "description": "Validating NDMO compliance standards", "progress": 85},
                {"name": "✅ Finalizing Results", "description": "Preparing processing results and reports", "progress": 100}
            ]
            
            # Process each step
            for i, step in enumerate(pipeline_steps):
                # Update status
                status_container.markdown(f"""
                <div style="background: white; padding: 1rem; border-radius: 10px; border: 1px solid #e9ecef; margin: 0.5rem 0;">
                    <div style="display: flex; align-items: center;">
                        <div class="loading-spinner" style="margin-right: 1rem;"></div>
                        <div>
                            <h5 style="margin: 0; color: #667eea;">{step['name']}</h5>
                            <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{step['description']}</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Update progress
                main_progress.progress(step['progress'] / 100)
                
                # Simulate processing time for each step
                import time
                time.sleep(0.5)
            
            # Clear status and show completion
            status_container.empty()
            main_progress.empty()
            
            # Process data with the actual processor
            with st.spinner("🔄 Executing data processing..."):
                processing_results = self.data_processor.process_data_file(data_temp_file, schema_temp_file)
                
                if "error" not in processing_results:
                    st.session_state.data_processing = processing_results
                
                # Enhanced success message with statistics
                processed_data = processing_results.get('processed_data', {})
                quality_metrics = processed_data.get('quality_metrics', {})
                ndmo_compliance = processing_results.get('ndmo_compliance', {})
                
                rows_processed = processed_data.get('rows', 0)
                columns_processed = processed_data.get('columns', 0)
                quality_score = quality_metrics.get('overall_score', 0)
                compliance_score = ndmo_compliance.get('overall_score', 0)
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #00b89420 0%, #00b89410 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #00b894; margin: 1rem 0;">
                    <div style="display: flex; align-items: center;">
                        <span style="font-size: 2rem; margin-right: 1rem;">✅</span>
                        <div>
                            <h4 style="margin: 0; color: #00b894;">Data Processing Completed Successfully!</h4>
                            <div style="margin: 0.5rem 0 0 0; color: #666;">
                                <p style="margin: 0.25rem 0; font-size: 0.9rem;">📊 Processed: {rows_processed:,} rows × {columns_processed} columns</p>
                                <p style="margin: 0.25rem 0; font-size: 0.9rem;">🎯 Quality Score: {quality_score:.1%}</p>
                                <p style="margin: 0.25rem 0; font-size: 0.9rem;">🛡️ NDMO Compliance: {compliance_score:.1%}</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
        else:
            # Enhanced error message
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #e17055; margin: 1rem 0;">
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 2rem; margin-right: 1rem;">❌</span>
                    <div>
                        <h4 style="margin: 0; color: #e17055;">Data Processing Failed</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666;">{processing_results['error']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        except Exception as e:
            # Enhanced exception handling
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #e17055; margin: 1rem 0;">
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 2rem; margin-right: 1rem;">⚠️</span>
                    <div>
                        <h4 style="margin: 0; color: #e17055;">Processing Error</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666;">{str(e)}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        finally:
            # Clean up temporary files
            for temp_file in [data_temp_file, schema_temp_file]:
                if temp_file and os.path.exists(temp_file):
                    os.remove(temp_file)
    
    def run_complete_analysis(self):
        """Run complete analysis with comprehensive pipeline"""
        if not st.session_state.schema_file or not st.session_state.data_file:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #e17055; margin: 1rem 0;">
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 2rem; margin-right: 1rem;">❌</span>
                    <div>
                        <h4 style="margin: 0; color: #e17055;">Missing Required Files</h4>
                        <p style="margin: 0.5rem 0 0 0; color: #666;">Both schema and data files are required for complete analysis</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            return
        
        # Create comprehensive pipeline UI
        st.markdown("""
        <div style="background: linear-gradient(135deg, #6c5ce720 0%, #6c5ce710 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #6c5ce7; margin: 1rem 0;">
            <h4 style="margin: 0 0 1rem 0; color: #6c5ce7;">🚀 Complete Analysis Pipeline</h4>
            <p style="margin: 0; color: #666; font-size: 0.95rem;">Running comprehensive data quality analysis and NDMO compliance assessment</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Main pipeline progress
        pipeline_progress = st.progress(0)
        pipeline_status = st.empty()
        
        # Complete pipeline steps
        complete_pipeline = [
            {"name": "📋 Schema Analysis", "description": "Analyzing schema structure and validation rules", "progress": 15, "function": self.analyze_schema},
            {"name": "🔧 Problem Analysis", "description": "Identifying schema problems and compliance issues", "progress": 30, "function": self.analyze_schema_problems},
            {"name": "🛡️ NDMO Compliance", "description": "Making schema NDMO compliant", "progress": 45, "function": self.make_schema_ndmo_compliant},
            {"name": "⚙️ Data Processing", "description": "Processing data according to compliant schema", "progress": 70, "function": self.process_data},
            {"name": "📊 Quality Assessment", "description": "Generating comprehensive quality reports", "progress": 85, "function": None},
            {"name": "✅ Pipeline Complete", "description": "All analysis steps completed successfully", "progress": 100, "function": None}
        ]
        
        try:
            # Execute each step in the pipeline
            for i, step in enumerate(complete_pipeline):
                # Update status
                pipeline_status.markdown(f"""
                <div style="background: white; padding: 1rem; border-radius: 10px; border: 1px solid #e9ecef; margin: 0.5rem 0;">
                    <div style="display: flex; align-items: center;">
                        <div class="loading-spinner" style="margin-right: 1rem;"></div>
                        <div>
                            <h5 style="margin: 0; color: #6c5ce7;">{step['name']}</h5>
                            <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{step['description']}</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Update progress
                pipeline_progress.progress(step['progress'] / 100)
                
                # Execute step function if available
                if step['function']:
                    step['function']()
                
                # Small delay for visual effect
                import time
                time.sleep(0.3)
            
            # Clear status and show completion
            pipeline_status.empty()
            pipeline_progress.empty()
            
            # Final success message
        if st.session_state.data_processing:
                processed_data = st.session_state.data_processing.get('processed_data', {})
                quality_metrics = processed_data.get('quality_metrics', {})
                ndmo_compliance = st.session_state.data_processing.get('ndmo_compliance', {})
                
                rows_processed = processed_data.get('rows', 0)
                columns_processed = processed_data.get('columns', 0)
                quality_score = quality_metrics.get('overall_score', 0)
                compliance_score = ndmo_compliance.get('overall_score', 0)
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #00b89420 0%, #00b89410 100%); padding: 2rem; border-radius: 20px; border-left: 4px solid #00b894; margin: 1rem 0; text-align: center;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🎉</div>
                    <h3 style="margin: 0 0 1rem 0; color: #00b894;">Complete Analysis Pipeline Finished Successfully!</h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1.5rem;">
                        <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📊</div>
                            <h5 style="margin: 0; color: #667eea;">Data Processed</h5>
                            <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{rows_processed:,} rows × {columns_processed} columns</p>
                        </div>
                        <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🎯</div>
                            <h5 style="margin: 0; color: #667eea;">Quality Score</h5>
                            <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{quality_score:.1%}</p>
                        </div>
                        <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🛡️</div>
                            <h5 style="margin: 0; color: #667eea;">NDMO Compliance</h5>
                            <p style="margin: 0.25rem 0 0 0; color: #666; font-size: 0.9rem;">{compliance_score:.1%}</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
    except Exception as e:
        # Enhanced error handling
        pipeline_status.empty()
        pipeline_progress.empty()
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #e1705520 0%, #e1705510 100%); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #e17055; margin: 1rem 0;">
            <div style="display: flex; align-items: center;">
                <span style="font-size: 2rem; margin-right: 1rem;">⚠️</span>
                <div>
                    <h4 style="margin: 0; color: #e17055;">Pipeline Error</h4>
                    <p style="margin: 0.5rem 0 0 0; color: #666;">{str(e)}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def save_uploaded_file(self, uploaded_file) -> str:
        """Save uploaded file temporarily"""
        temp_file = f"temp_{uploaded_file.name}"
        
        with open(temp_file, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        return temp_file
    
    def export_schema_analysis(self):
        """Export schema analysis"""
        if st.session_state.schema_analysis:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"schema_analysis_{timestamp}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(st.session_state.schema_analysis, f, indent=2, ensure_ascii=False, default=str)
            
            st.success(f"✅ Schema analysis exported to: {filename}")
        else:
            st.warning("⚠️ No schema analysis to export")
    
    def export_processing_results(self):
        """Export processing results"""
        if st.session_state.data_processing:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"processing_results_{timestamp}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(st.session_state.data_processing, f, indent=2, ensure_ascii=False, default=str)
            
            st.success(f"✅ Processing results exported to: {filename}")
        else:
            st.warning("⚠️ No processing results to export")
    
    def export_quality_report(self):
        """Export quality report"""
        if st.session_state.data_processing:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"quality_report_{timestamp}.json"
            
            # Create comprehensive quality report
            quality_report = {
                "report_timestamp": datetime.now().isoformat(),
                "schema_analysis": st.session_state.schema_analysis,
                "data_processing": st.session_state.data_processing,
                "summary": {
                    "overall_quality": st.session_state.data_processing.get('processed_data', {}).get('quality_metrics', {}).get('overall_score', 0.0),
                    "ndmo_compliance": st.session_state.data_processing.get('ndmo_compliance', {}).get('overall_score', 0.0),
                    "records_processed": st.session_state.data_processing.get('processed_data', {}).get('rows', 0)
                }
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(quality_report, f, indent=2, ensure_ascii=False, default=str)
            
            st.success(f"✅ Quality report exported to: {filename}")
        else:
            st.warning("⚠️ No quality data to export")
    
    def export_problem_analysis(self):
        """Export problem analysis"""
        if st.session_state.problem_analysis:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"problem_analysis_{timestamp}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(st.session_state.problem_analysis, f, indent=2, ensure_ascii=False, default=str)
            
            st.success(f"✅ Problem analysis exported to: {filename}")
        else:
            st.warning("⚠️ No problem analysis to export")
    
    def export_corrected_schema(self):
        """Export corrected schema"""
        if st.session_state.schema_analysis and st.session_state.problem_analysis:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"corrected_schema_{timestamp}.json"
            
            # Generate corrected schema
            corrected_schema = self.problem_analyzer.generate_corrected_schema(st.session_state.schema_analysis)
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(corrected_schema, f, indent=2, ensure_ascii=False, default=str)
            
            st.success(f"✅ Corrected schema exported to: {filename}")
        else:
            st.warning("⚠️ No schema analysis or problem analysis available")
    
    def generate_html_report(self):
        """Generate comprehensive HTML report"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ndmo_compliance_report_{timestamp}.html"
            filepath = self.get_report_path("html", filename)
            
            # Generate HTML content
            html_content = self.create_html_report_content()
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            st.success(f"✅ HTML report generated successfully!")
            st.info(f"📄 Report saved as: {filename}")
            
            # Provide download link
            with open(filename, 'r', encoding='utf-8') as f:
                st.download_button(
                    label="📥 Download HTML Report",
                    data=f.read(),
                    file_name=filename,
                    mime="text/html"
                )
                
        except Exception as e:
            st.error(f"❌ Error generating HTML report: {str(e)}")
    
    def create_html_report_content(self) -> str:
        """Create comprehensive HTML report content"""
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>NDMO Compliance Report</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    margin: 0;
                    padding: 20px;
                    background-color: #f5f5f5;
                }
                .container {
                    max-width: 1200px;
                    margin: 0 auto;
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 0 20px rgba(0,0,0,0.1);
                }
                .header {
                    text-align: center;
                    border-bottom: 3px solid #2E86AB;
                    padding-bottom: 20px;
                    margin-bottom: 30px;
                }
                .header h1 {
                    color: #2E86AB;
                    margin: 0;
                    font-size: 2.5em;
                }
                .header p {
                    color: #666;
                    font-size: 1.2em;
                    margin: 10px 0;
                }
                .summary-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                    gap: 20px;
                    margin: 30px 0;
                }
                .summary-card {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                }
                .summary-card h3 {
                    margin: 0 0 10px 0;
                    font-size: 1.5em;
                }
                .summary-card .value {
                    font-size: 2em;
                    font-weight: bold;
                    margin: 10px 0;
                }
                .section {
                    margin: 40px 0;
                    padding: 20px;
                    border-left: 4px solid #2E86AB;
                    background: #f8f9fa;
                }
                .section h2 {
                    color: #2E86AB;
                    margin-top: 0;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin: 20px 0;
                    background: white;
                }
                th, td {
                    padding: 12px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }
                th {
                    background-color: #2E86AB;
                    color: white;
                    font-weight: bold;
                }
                tr:hover {
                    background-color: #f5f5f5;
                }
                .compliance-badge {
                    display: inline-block;
                    padding: 5px 15px;
                    border-radius: 20px;
                    font-weight: bold;
                    text-transform: uppercase;
                }
                .compliant {
                    background-color: #28a745;
                    color: white;
                }
                .non-compliant {
                    background-color: #dc3545;
                    color: white;
                }
                .partially-compliant {
                    background-color: #ffc107;
                    color: black;
                }
                .improvement {
                    color: #28a745;
                    font-weight: bold;
                }
                .footer {
                    text-align: center;
                    margin-top: 50px;
                    padding-top: 20px;
                    border-top: 1px solid #ddd;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <img src="data:image/png;base64,""" + self.get_logo_base64() + """" alt="SANS Data Quality System" style="max-width: 200px; height: auto; margin-bottom: 1rem;">
                    <h1>🛡️ SANS Data Quality System</h1>
                    <h2>NDMO Compliance Report</h2>
                    <p>Professional Data Quality Assessment</p>
                    <p>Generated on: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
                </div>
        """
        
        # Add summary section
        if hasattr(st.session_state, 'schema_comparison') and st.session_state.schema_comparison:
            comparison = st.session_state.schema_comparison
            summary = comparison.get("summary", {})
            
            html_content += f"""
                <div class="summary-grid">
                    <div class="summary-card">
                        <h3>📊 Original Compliance</h3>
                        <div class="value">{summary.get("original_compliance", 0):.1%}</div>
                    </div>
                    <div class="summary-card">
                        <h3>🛡️ Compliant Score</h3>
                        <div class="value">{summary.get("compliant_compliance", 0):.1%}</div>
                    </div>
                    <div class="summary-card">
                        <h3>📈 Improvement</h3>
                        <div class="value improvement">+{summary.get("improvement", 0):.1%}</div>
                    </div>
                    <div class="summary-card">
                        <h3>🔧 Added Columns</h3>
                        <div class="value">{summary.get("added_columns", 0)}</div>
                    </div>
                </div>
            """
        
        # Add detailed sections
        html_content += """
                <div class="section">
                    <h2>📋 Schema Analysis Summary</h2>
                    <p>This report provides a comprehensive analysis of your data schema's compliance with NDMO standards.</p>
                </div>
                
                <div class="section">
                    <h2>🛡️ NDMO Standards Compliance</h2>
                    <p>The following table shows compliance with each NDMO standard category:</p>
        """
        
        # Add compliance details if available
        if hasattr(st.session_state, 'schema_analysis') and st.session_state.schema_analysis:
            compliance = st.session_state.schema_analysis.get("ndmo_compliance", {})
            if compliance:
                html_content += """
                    <table>
                        <thead>
                            <tr>
                                <th>Category</th>
                                <th>Score</th>
                                <th>Status</th>
                                <th>Description</th>
                            </tr>
                        </thead>
                        <tbody>
                """
                
                categories = compliance.get("category_scores", {})
                for category, score in categories.items():
                    status_class = "compliant" if score >= 0.8 else "non-compliant" if score < 0.5 else "partially-compliant"
                    status_text = "Compliant" if score >= 0.8 else "Non-Compliant" if score < 0.5 else "Partially Compliant"
                    
                    html_content += f"""
                        <tr>
                            <td>{category}</td>
                            <td>{score:.1%}</td>
                            <td><span class="compliance-badge {status_class}">{status_text}</span></td>
                            <td>NDMO compliance for {category} standards</td>
                        </tr>
                    """
                
                html_content += """
                        </tbody>
                    </table>
                """
        
        # Add improvements section
        if hasattr(st.session_state, 'schema_comparison') and st.session_state.schema_comparison:
            improvements = st.session_state.schema_comparison.get("compliance_improvements", [])
            if improvements:
                html_content += """
                    <div class="section">
                        <h2>🔧 Compliance Improvements</h2>
                        <p>The following improvements were made to achieve NDMO compliance:</p>
                        <table>
                            <thead>
                                <tr>
                                    <th>Improvement</th>
                                    <th>NDMO Standard</th>
                                    <th>Description</th>
                                </tr>
                            </thead>
                            <tbody>
                """
                
                for improvement in improvements:
                    html_content += f"""
                        <tr>
                            <td>{improvement.get('improvement', '')}</td>
                            <td>{improvement.get('ndmo_standard', '')}</td>
                            <td>{improvement.get('description', '')}</td>
                        </tr>
                    """
                
                html_content += """
                            </tbody>
                        </table>
                    </div>
                """
        
        # Add footer
        html_content += """
                <div class="footer">
                    <p>Generated by Professional NDMO Data Quality Dashboard</p>
                    <p>© 2024 - All rights reserved</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html_content
    
    def export_compliant_schema(self):
        """Export compliant schema to Excel file"""
        try:
            if not hasattr(st.session_state, 'compliant_schema') or not st.session_state.compliant_schema:
                st.error("❌ No compliant schema available. Please make schema NDMO compliant first.")
                return
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"compliant_schema_{timestamp}.xlsx"
            filepath = self.get_report_path("export", filename)
            
            # Get compliant schema data
            compliant_schema = st.session_state.compliant_schema
            schema_analysis = compliant_schema.get("schema_analysis", {})
            columns = schema_analysis.get("columns", [])
            
            # Create DataFrame for schema
            schema_data = []
            for col in columns:
                schema_data.append({
                    'COLUMN_NAME': col.get('name', ''),
                    'DATA_TYPE': col.get('data_type', ''),
                    'IS_NULLABLE': 'YES' if col.get('nullable', True) else 'NO',
                    'PRIMARY_KEY': 'YES' if col.get('primary_key', False) else 'NO',
                    'UNIQUE': 'YES' if col.get('unique', False) else 'NO',
                    'MAX_LENGTH': col.get('constraints', {}).get('max_length', ''),
                    'MIN_VALUE': col.get('constraints', {}).get('min_value', ''),
                    'MAX_VALUE': col.get('constraints', {}).get('max_value', ''),
                    'REQUIRED': 'YES' if col.get('constraints', {}).get('required', False) else 'NO',
                    'NDMO_STANDARD': col.get('ndmo_standard', ''),
                    'DESCRIPTION': col.get('description', '')
                })
            
            schema_df = pd.DataFrame(schema_data)
            
            # Export to Excel
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                schema_df.to_excel(writer, sheet_name='Compliant_Schema', index=False)
                
                # Add metadata sheet
                metadata = {
                    'Property': ['Export Date', 'Original Columns', 'Compliant Columns', 'NDMO Compliance Score', 'Status'],
                    'Value': [
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        len(st.session_state.original_schema.get("schema_analysis", {}).get("columns", [])) if hasattr(st.session_state, 'original_schema') else 0,
                        len(columns),
                        f"{compliant_schema.get('ndmo_compliance', {}).get('overall_score', 0):.1%}",
                        'NDMO Compliant'
                    ]
                }
                metadata_df = pd.DataFrame(metadata)
                metadata_df.to_excel(writer, sheet_name='Metadata', index=False)
            
            st.success(f"✅ Compliant schema exported successfully!")
            st.info(f"📄 File saved as: {filename}")
            
            # Store filename for re-analysis
            st.session_state.exported_schema_file = filename
            
        except Exception as e:
            st.error(f"❌ Error exporting compliant schema: {str(e)}")
    
    def export_processed_data(self):
        """Export processed data to Excel file"""
        try:
            # Check if we have processing results or can process data
            if not hasattr(st.session_state, 'processing_results') or not st.session_state.processing_results:
                # Try to process data if we have the required files
                if hasattr(st.session_state, 'data_file') and hasattr(st.session_state, 'schema_file'):
                    st.info("🔄 No processed data found. Processing data first...")
                    try:
                        self.process_data()
                        # Check if processing was successful
                        if hasattr(st.session_state, 'processing_results') and st.session_state.processing_results:
                            st.success("✅ Data processed successfully!")
                        else:
                            st.error("❌ Failed to process data. Please check your files and try again.")
                            return
                    except Exception as e:
                        st.error(f"❌ Error during data processing: {str(e)}")
                        return
                else:
                    st.error("❌ No processed data available and no data/schema files found. Please upload and process data first.")
                    return
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"processed_data_{timestamp}.xlsx"
            filepath = self.get_report_path("export", filename)
            
            # Get processed data
            processing_results = st.session_state.processing_results
            processed_data = processing_results.get('processed_data', {})
            
            if 'dataframe' in processed_data:
                df = processed_data['dataframe']
                
                # Export to Excel
                with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                    df.to_excel(writer, sheet_name='Processed_Data', index=False)
                    
                    # Add quality metrics sheet
                    quality_metrics = processing_results.get('quality_metrics', {})
                    metrics_data = []
                    for metric, value in quality_metrics.items():
                        if isinstance(value, dict):
                            for sub_metric, sub_value in value.items():
                                metrics_data.append({
                                    'Category': metric,
                                    'Metric': sub_metric,
                                    'Value': sub_value
                                })
                        else:
                            metrics_data.append({
                                'Category': 'Overall',
                                'Metric': metric,
                                'Value': value
                            })
                    
                    metrics_df = pd.DataFrame(metrics_data)
                    metrics_df.to_excel(writer, sheet_name='Quality_Metrics', index=False)
                    
                    # Add processing summary
                    summary_data = {
                        'Property': [
                            'Export Date',
                            'Original Rows',
                            'Processed Rows',
                            'Original Columns',
                            'Processed Columns',
                            'Quality Improvement',
                            'NDMO Compliance'
                        ],
                        'Value': [
                            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            processing_results.get('original_data', {}).get('rows', 0),
                            processed_data.get('rows', 0),
                            processing_results.get('original_data', {}).get('columns', 0),
                            processed_data.get('columns', 0),
                            f"{quality_metrics.get('overall_score', 0):.1%}",
                            f"{processing_results.get('ndmo_compliance', {}).get('overall_score', 0):.1%}"
                        ]
                    }
                    summary_df = pd.DataFrame(summary_data)
                    summary_df.to_excel(writer, sheet_name='Processing_Summary', index=False)
                
                st.success(f"✅ Processed data exported successfully!")
                st.info(f"📄 File saved as: {filename}")
                
                # Store filename for re-analysis
                st.session_state.exported_data_file = filename
            else:
                st.error("❌ No processed dataframe found in results")
                
        except Exception as e:
            st.error(f"❌ Error exporting processed data: {str(e)}")
    
    def reanalyze_exported_files(self):
        """Re-analyze exported files to verify compliance"""
        try:
            if not hasattr(st.session_state, 'exported_schema_file') or not st.session_state.exported_schema_file:
                st.error("❌ No exported schema file found. Please export compliant schema first.")
                return
            
            if not hasattr(st.session_state, 'exported_data_file') or not st.session_state.exported_data_file:
                st.error("❌ No exported data file found. Please export processed data first.")
                return
            
            with st.spinner("🔄 Re-analyzing exported files..."):
                # Re-analyze schema
                schema_file = st.session_state.exported_schema_file
                schema_analysis = self.schema_analyzer.analyze_schema_file(schema_file)
                
                if "error" not in schema_analysis:
                    # Re-analyze NDMO compliance
                    ndmo_manager = NDMOStandardsManager()
                    compliance = ndmo_manager.validate_schema_compliance(schema_analysis)
                    schema_analysis["ndmo_compliance"] = compliance
                    
                    # Store re-analyzed results
                    st.session_state.reanalyzed_schema = schema_analysis
                    
                    # Re-analyze data
                    data_file = st.session_state.exported_data_file
                    data_analysis = self.data_processor.process_data_file(data_file, schema_file)
                    
                    if "error" not in data_analysis:
                        st.session_state.reanalyzed_data = data_analysis
                        
                        # Display results
                        st.success("✅ Re-analysis completed successfully!")
                        
                        # Show comparison
                        st.markdown("### 📊 Re-analysis Results")
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric(
                                "Schema Compliance",
                                f"{compliance.get('overall_score', 0):.1%}",
                                delta=f"+{compliance.get('overall_score', 0) - 0.167:.1%}" if compliance.get('overall_score', 0) > 0.167 else None
                            )
                        
                        with col2:
                            st.metric(
                                "Data Quality",
                                f"{data_analysis.get('quality_metrics', {}).get('overall_score', 0):.1%}",
                                delta=None
                            )
                        
                        with col3:
                            st.metric(
                                "Total Columns",
                                len(schema_analysis.get('schema_analysis', {}).get('columns', [])),
                                delta=None
                            )
                        
                        # Show detailed results
                        st.markdown("#### 🛡️ NDMO Compliance Details")
                        compliance_df = pd.DataFrame([
                            {"Category": category, "Score": f"{score:.1%}", "Status": "✅ Compliant" if score >= 0.8 else "⚠️ Partially Compliant" if score >= 0.5 else "❌ Non-Compliant"}
                            for category, score in compliance.get('category_scores', {}).items()
                        ])
                        st.dataframe(compliance_df, use_container_width=True)
                        
                    else:
                        st.error(f"❌ Data re-analysis failed: {data_analysis['error']}")
                else:
                    st.error(f"❌ Schema re-analysis failed: {schema_analysis['error']}")
                    
        except Exception as e:
            st.error(f"❌ Error re-analyzing files: {str(e)}")
    
    def generate_technical_report(self):
        """Generate technical report for developers"""
        try:
            if not hasattr(st.session_state, 'schema_analysis') or not st.session_state.schema_analysis:
                st.error("❌ No schema analysis available. Please analyze schema first.")
                return
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"technical_report_{timestamp}.md"
            filepath = self.get_report_path("technical", filename)
            
            # Generate technical report content
            report_content = self.create_technical_report_content()
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            st.success(f"✅ Technical report generated successfully!")
            st.info(f"📄 Report saved as: {filename}")
            
            # Display report content
            st.markdown("### 📋 Technical Report Preview")
            with st.expander("View Technical Report"):
                st.markdown(report_content)
                
        except Exception as e:
            st.error(f"❌ Error generating technical report: {str(e)}")
    
    def create_technical_report_content(self) -> str:
        """Create comprehensive technical report content"""
        schema_analysis = st.session_state.schema_analysis
        compliance = schema_analysis.get("ndmo_compliance", {})
        schema_info = schema_analysis.get("schema_analysis", {})
        columns = schema_info.get("columns", [])
        
        report = f"""# 🛡️ NDMO Compliance Technical Report

**Generated on:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Project:** Professional NDMO Data Quality Dashboard

## 📊 Executive Summary

- **Current NDMO Compliance:** {compliance.get('overall_score', 0):.1%}
- **Total Columns:** {len(columns)}
- **Compliance Status:** {'✅ Compliant' if compliance.get('overall_score', 0) >= 0.8 else '⚠️ Partially Compliant' if compliance.get('overall_score', 0) >= 0.5 else '❌ Non-Compliant'}

## 🔍 Detailed Analysis

### Schema Structure
- **Table Name:** {schema_info.get('table_name', 'Unknown')}
- **Total Columns:** {len(columns)}
- **Primary Keys:** {sum(1 for col in columns if col.get('primary_key', False))}
- **Required Fields:** {sum(1 for col in columns if col.get('constraints', {}).get('required', False))}

### NDMO Standards Compliance

"""
        
        # Add compliance details
        category_scores = compliance.get('category_scores', {})
        for category, score in category_scores.items():
            status = "✅ Compliant" if score >= 0.8 else "⚠️ Partially Compliant" if score >= 0.5 else "❌ Non-Compliant"
            report += f"- **{category}:** {score:.1%} - {status}\n"
        
        report += f"""

## 🔧 Required Modifications

### 1. Primary Key Implementation
**Issue:** Missing or insufficient primary key constraints
**Solution:**
```sql
-- Add primary key constraint
ALTER TABLE {schema_info.get('table_name', 'your_table')} 
ADD CONSTRAINT pk_{schema_info.get('table_name', 'your_table')} 
PRIMARY KEY (id);
```

### 2. Data Type Standardization
**Issue:** Inconsistent or non-standard data types
**Required Changes:**
"""
        
        # Add data type recommendations
        for col in columns:
            current_type = col.get('data_type', 'Unknown')
            recommended_type = self._get_recommended_data_type(col)
            if current_type != recommended_type:
                report += f"- **{col.get('name', 'Unknown')}:** {current_type} → {recommended_type}\n"
        
        report += f"""

### 3. Constraint Implementation
**Required Constraints:**
"""
        
        # Add constraint recommendations
        for col in columns:
            constraints = col.get('constraints', {})
            if not constraints.get('required', False):
                report += f"- **{col.get('name', 'Unknown')}:** Add NOT NULL constraint\n"
            if not constraints.get('unique', False) and col.get('primary_key', False):
                report += f"- **{col.get('name', 'Unknown')}:** Add UNIQUE constraint\n"
        
        report += f"""

### 4. Audit Trail Fields
**Missing Fields:**
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)
- `created_by` (VARCHAR)
- `updated_by` (VARCHAR)

**Implementation:**
```sql
ALTER TABLE {schema_info.get('table_name', 'your_table')} 
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(100),
ADD COLUMN updated_by VARCHAR(100);
```

### 5. Data Quality Constraints
**Required Validations:**
"""
        
        # Add validation recommendations
        for col in columns:
            constraints = col.get('constraints', {})
            if constraints.get('min_length') or constraints.get('max_length'):
                min_len = constraints.get('min_length', 'N/A')
                max_len = constraints.get('max_length', 'N/A')
                report += f"- **{col.get('name', 'Unknown')}:** Length validation ({min_len}-{max_len} characters)\n"
            if constraints.get('min_value') or constraints.get('max_value'):
                min_val = constraints.get('min_value', 'N/A')
                max_val = constraints.get('max_value', 'N/A')
                report += f"- **{col.get('name', 'Unknown')}:** Range validation ({min_val}-{max_val})\n"
        
        report += f"""

## 🚀 Implementation Priority

### High Priority (Critical)
1. **Primary Key Implementation** - Required for data integrity
2. **Audit Trail Fields** - Required for compliance tracking
3. **Data Type Standardization** - Required for data consistency

### Medium Priority (Important)
1. **Constraint Implementation** - Improves data quality
2. **Validation Rules** - Ensures data accuracy
3. **Index Optimization** - Improves performance

### Low Priority (Enhancement)
1. **Documentation Updates** - Improves maintainability
2. **Performance Monitoring** - Optimizes system performance

## 📝 Code Examples

### Database Migration Script
```sql
-- Migration script for NDMO compliance
BEGIN TRANSACTION;

-- Add primary key
ALTER TABLE {schema_info.get('table_name', 'your_table')} 
ADD CONSTRAINT pk_{schema_info.get('table_name', 'your_table')} 
PRIMARY KEY (id);

-- Add audit fields
ALTER TABLE {schema_info.get('table_name', 'your_table')} 
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(100),
ADD COLUMN updated_by VARCHAR(100);

-- Add constraints
"""
        
        # Add constraint examples
        for col in columns:
            if not col.get('constraints', {}).get('required', False):
                report += f"ALTER TABLE {schema_info.get('table_name', 'your_table')} MODIFY COLUMN {col.get('name', 'Unknown')} NOT NULL;\n"
        
        report += f"""
COMMIT;
```

### Application Code Updates
```python
# Python example for data validation
def validate_data(data):
    errors = []
    
    # Required field validation
    required_fields = {[f"'{col.get('name', 'Unknown')}'" for col in columns if col.get('constraints', {}).get('required', False)]}
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
```

## 🎯 Success Metrics

### Compliance Targets
- **Overall NDMO Compliance:** 95%+
- **Data Quality Score:** 90%+
- **Audit Trail Coverage:** 100%
- **Constraint Coverage:** 95%+

### Performance Targets
- **Query Response Time:** < 100ms
- **Data Validation Time:** < 50ms
- **Audit Log Performance:** < 10ms

## 📚 Additional Resources

### NDMO Standards Documentation
- [Data Governance Standards](https://ndmo.gov.sa/standards/data-governance)
- [Data Quality Guidelines](https://ndmo.gov.sa/standards/data-quality)
- [Security Requirements](https://ndmo.gov.sa/standards/security)

### Implementation Checklist
- [ ] Primary key implementation
- [ ] Audit trail fields added
- [ ] Data type standardization
- [ ] Constraint implementation
- [ ] Validation rules added
- [ ] Performance testing completed
- [ ] Documentation updated
- [ ] Compliance testing passed

---

**Report Generated by:** Professional NDMO Data Quality Dashboard
**Version:** 1.0
**Contact:** Technical Team
"""
        
        return report
    
    def _get_recommended_data_type(self, column: dict) -> str:
        """Get recommended data type for a column"""
        current_type = column.get('data_type', '').upper()
        name = column.get('name', '').lower()
        
        # ID fields
        if 'id' in name and current_type not in ['INTEGER', 'BIGINT']:
            return 'INTEGER'
        
        # Date fields
        if any(keyword in name for keyword in ['date', 'time', 'created', 'updated']):
            return 'TIMESTAMP'
        
        # Text fields
        if current_type in ['TEXT', 'LONGTEXT']:
            return 'VARCHAR(255)'
        
        # Numeric fields
        if current_type in ['FLOAT', 'DOUBLE']:
            return 'DECIMAL(10,2)'
        
        return current_type
    
    def generate_implementation_guide(self):
        """Generate implementation guide for developers"""
        try:
            if not hasattr(st.session_state, 'schema_analysis') or not st.session_state.schema_analysis:
                st.error("❌ No schema analysis available. Please analyze schema first.")
                return
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"implementation_guide_{timestamp}.md"
            filepath = self.get_report_path("technical", filename)
            
            # Generate implementation guide content
            guide_content = self.create_implementation_guide_content()
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(guide_content)
            
            st.success(f"✅ Implementation guide generated successfully!")
            st.info(f"📄 Guide saved as: {filename}")
            
            # Display guide content
            st.markdown("### 🔧 Implementation Guide Preview")
            with st.expander("View Implementation Guide"):
                st.markdown(guide_content)
                
        except Exception as e:
            st.error(f"❌ Error generating implementation guide: {str(e)}")
    
    def create_implementation_guide_content(self) -> str:
        """Create comprehensive implementation guide content"""
        schema_analysis = st.session_state.schema_analysis
        compliance = schema_analysis.get("ndmo_compliance", {})
        schema_info = schema_analysis.get("schema_analysis", {})
        columns = schema_info.get("columns", [])
        
        guide = f"""# 🚀 NDMO Compliance Implementation Guide

**Generated on:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Target Compliance:** 95%+

## 📋 Implementation Checklist

### Phase 1: Critical Compliance (Week 1-2)
- [ ] **Primary Key Implementation**
  - [ ] Identify existing primary key
  - [ ] Add primary key if missing
  - [ ] Test primary key constraints
  
- [ ] **Audit Trail Fields**
  - [ ] Add created_at field
  - [ ] Add updated_at field
  - [ ] Add created_by field
  - [ ] Add updated_by field
  - [ ] Implement audit triggers
  
- [ ] **Data Type Standardization**
  - [ ] Review all column types
  - [ ] Convert to standard types
  - [ ] Test data conversion

### Phase 2: Data Quality (Week 3-4)
- [ ] **Constraint Implementation**
  - [ ] Add NOT NULL constraints
  - [ ] Add UNIQUE constraints
  - [ ] Add CHECK constraints
  - [ ] Test constraint validation
  
- [ ] **Validation Rules**
  - [ ] Implement length validation
  - [ ] Implement range validation
  - [ ] Implement format validation
  - [ ] Test validation rules

### Phase 3: Performance & Security (Week 5-6)
- [ ] **Index Optimization**
  - [ ] Add primary key indexes
  - [ ] Add foreign key indexes
  - [ ] Add query optimization indexes
  
- [ ] **Security Implementation**
  - [ ] Add data encryption
  - [ ] Implement access controls
  - [ ] Add audit logging

## 🔧 Step-by-Step Implementation

### Step 1: Database Schema Updates

#### 1.1 Primary Key Implementation
```sql
-- Check existing primary key
SHOW KEYS FROM {schema_info.get('table_name', 'your_table')} WHERE Key_name = 'PRIMARY';

-- Add primary key if missing
ALTER TABLE {schema_info.get('table_name', 'your_table')} 
ADD CONSTRAINT pk_{schema_info.get('table_name', 'your_table')} 
PRIMARY KEY (id);
```

#### 1.2 Audit Trail Fields
```sql
-- Add audit fields
ALTER TABLE {schema_info.get('table_name', 'your_table')} 
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(100),
ADD COLUMN updated_by VARCHAR(100);

-- Create audit trigger
DELIMITER $$
CREATE TRIGGER {schema_info.get('table_name', 'your_table')}_audit_trigger
BEFORE UPDATE ON {schema_info.get('table_name', 'your_table')}
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
    SET NEW.updated_by = USER();
END$$
DELIMITER ;
```

#### 1.3 Data Type Standardization
```sql
-- Standardize data types
"""
        
        # Add data type conversion examples
        for col in columns:
            current_type = col.get('data_type', 'Unknown')
            recommended_type = self._get_recommended_data_type(col)
            if current_type != recommended_type:
                guide += f"ALTER TABLE {schema_info.get('table_name', 'your_table')} MODIFY COLUMN {col.get('name', 'Unknown')} {recommended_type};\n"
        
        guide += f"""
```

### Step 2: Application Code Updates

#### 2.1 Data Validation Layer
```python
# validation.py
class DataValidator:
    def __init__(self, schema):
        self.schema = schema
    
    def validate(self, data):
        errors = []
        
        # Required field validation
        for field, config in self.schema.items():
            if config.get('required', False) and not data.get(field):
                errors.append(f"{{field}} is required")
        
        # Data type validation
        for field, value in data.items():
            if value is not None:
                field_config = self.schema.get(field, {{}})
                field_type = field_config.get('type', 'string')
                
                if field_type == 'integer' and not isinstance(value, int):
                    errors.append(f"{{field}} must be an integer")
                elif field_type == 'string' and not isinstance(value, str):
                    errors.append(f"{{field}} must be a string")
        
        return errors
```

#### 2.2 Audit Trail Implementation
```python
# audit.py
class AuditTrail:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def log_change(self, table_name, record_id, action, old_data, new_data, user_id):
        audit_record = {{
            'table_name': table_name,
            'record_id': record_id,
            'action': action,
            'old_data': json.dumps(old_data),
            'new_data': json.dumps(new_data),
            'user_id': user_id,
            'timestamp': datetime.now()
        }}
        
        self.db.audit_logs.insert(audit_record)
```

### Step 3: Testing Implementation

#### 3.1 Unit Tests
```python
# test_validation.py
import unittest
from validation import DataValidator

class TestDataValidation(unittest.TestCase):
    def setUp(self):
        self.validator = DataValidator({{
            'id': {{'type': 'integer', 'required': True}},
            'name': {{'type': 'string', 'required': True, 'max_length': 100}},
            'email': {{'type': 'string', 'required': True, 'format': 'email'}}
        }})
    
    def test_required_field_validation(self):
        data = {{'id': 1}}  # Missing required fields
        errors = self.validator.validate(data)
        self.assertIn('name is required', errors)
        self.assertIn('email is required', errors)
    
    def test_data_type_validation(self):
        data = {{'id': 'not_a_number', 'name': 'John', 'email': 'john@example.com'}}
        errors = self.validator.validate(data)
        self.assertIn('id must be an integer', errors)
```

#### 3.2 Integration Tests
```python
# test_integration.py
import unittest
from database import Database
from validation import DataValidator

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.validator = DataValidator(self.db.get_schema())
    
    def test_end_to_end_validation(self):
        # Test complete data flow
        data = {{'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}}
        
        # Validate data
        errors = self.validator.validate(data)
        self.assertEqual(len(errors), 0)
        
        # Insert data
        result = self.db.insert('users', data)
        self.assertTrue(result.success)
        
        # Verify audit trail
        audit_logs = self.db.get_audit_logs('users', 1)
        self.assertGreater(len(audit_logs), 0)
```

## 🎯 Performance Optimization

### Database Optimization
```sql
-- Add indexes for performance
CREATE INDEX idx_{schema_info.get('table_name', 'your_table')}_created_at 
ON {schema_info.get('table_name', 'your_table')} (created_at);

CREATE INDEX idx_{schema_info.get('table_name', 'your_table')}_updated_at 
ON {schema_info.get('table_name', 'your_table')} (updated_at);

-- Optimize queries
EXPLAIN SELECT * FROM {schema_info.get('table_name', 'your_table')} 
WHERE created_at >= '2024-01-01';
```

### Application Optimization
```python
# Use connection pooling
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine(
    'mysql://user:password@localhost/db',
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20
)

# Use prepared statements
def get_user_by_id(user_id):
    stmt = "SELECT * FROM users WHERE id = %s"
    return db.execute(stmt, (user_id,))
```

## 🔒 Security Implementation

### Data Encryption
```python
# encryption.py
from cryptography.fernet import Fernet

class DataEncryption:
    def __init__(self, key):
        self.cipher = Fernet(key)
    
    def encrypt(self, data):
        return self.cipher.encrypt(data.encode())
    
    def decrypt(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()
```

### Access Control
```python
# access_control.py
class AccessControl:
    def __init__(self, db):
        self.db = db
    
    def check_permission(self, user_id, table_name, action):
        permissions = self.db.get_user_permissions(user_id)
        return f"{{table_name}}.{{action}}" in permissions
    
    def audit_access(self, user_id, table_name, action, success):
        self.db.log_access(user_id, table_name, action, success)
```

## 📊 Monitoring & Alerting

### Performance Monitoring
```python
# monitoring.py
import time
from functools import wraps

def monitor_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        # Log performance metrics
        logger.info(f"{{func.__name__}} took {{end_time - start_time:.2f}} seconds")
        
        return result
    return wrapper
```

### Compliance Monitoring
```python
# compliance_monitor.py
class ComplianceMonitor:
    def __init__(self, db):
        self.db = db
    
    def check_compliance(self):
        compliance_score = self.calculate_compliance_score()
        
        if compliance_score < 0.95:
            self.send_alert(f"Compliance score dropped to {{compliance_score:.1%}}")
        
        return compliance_score
    
    def calculate_compliance_score(self):
        # Calculate based on NDMO standards
        total_checks = 10
        passed_checks = 0
        
        # Check primary key
        if self.has_primary_key():
            passed_checks += 1
        
        # Check audit trail
        if self.has_audit_trail():
            passed_checks += 1
        
        # Add more checks...
        
        return passed_checks / total_checks
```

## 🚀 Deployment Checklist

### Pre-Deployment
- [ ] All tests passing
- [ ] Performance benchmarks met
- [ ] Security review completed
- [ ] Documentation updated
- [ ] Backup strategy in place

### Deployment
- [ ] Database migration scripts ready
- [ ] Application deployment plan
- [ ] Rollback plan prepared
- [ ] Monitoring configured
- [ ] Team notified

### Post-Deployment
- [ ] Smoke tests executed
- [ ] Performance monitoring active
- [ ] Compliance monitoring active
- [ ] Team training completed
- [ ] Documentation updated

## 📞 Support & Resources

### Technical Support
- **Database Team:** database@company.com
- **Application Team:** apps@company.com
- **Security Team:** security@company.com

### Documentation
- [NDMO Standards](https://ndmo.gov.sa/standards)
- [Database Best Practices](https://docs.company.com/db)
- [Security Guidelines](https://docs.company.com/security)

### Tools & Libraries
- **Validation:** Cerberus, Marshmallow
- **Database:** SQLAlchemy, Alembic
- **Monitoring:** Prometheus, Grafana
- **Testing:** pytest, unittest

---

**Implementation Guide Generated by:** Professional NDMO Data Quality Dashboard
**Version:** 1.0
**Last Updated:** {datetime.now().strftime("%Y-%m-%d")}
"""
        
        return guide

def main():
    """Main function"""
    dashboard = ProfessionalNDMODashboard()
    dashboard.run_dashboard()

if __name__ == "__main__":
    main()