# 🛡️ SANS Data Quality System

**Professional NDMO Compliance Dashboard with Advanced Pipeline Processing**

A comprehensive enterprise-grade data quality management system that analyzes schemas, processes data, and ensures NDMO (National Data Management Office) compliance. Features advanced pipeline processing with real-time progress tracking, professional reporting, and seamless deployment capabilities.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Deploy](https://img.shields.io/badge/Deploy-Heroku-purple.svg)](https://heroku.com)
[![Pipeline](https://img.shields.io/badge/Pipeline-Advanced-orange.svg)](#-advanced-pipeline-processing)
[![Reports](https://img.shields.io/badge/Reports-Professional-green.svg)](#-professional-reporting)

## ✨ Key Features

### 🌐 NEW: Professional HTML Reports - التقارير HTML الاحترافية
- **Beautiful HTML Reports** with company logo and professional styling
- **Arabic Language Support** with RTL layout and Cairo fonts  
- **Interactive Charts** using Chart.js for data visualization
- **Responsive Design** that works on all devices
- **Print-Ready** reports with optimized styling
- **Enhanced Data Visualization** with progress bars and summary cards
- **Professional Styling** with gradient backgrounds and animations

### 🚀 Advanced Pipeline Processing
- **Real-Time Progress Tracking**: Visual progress bars with detailed step-by-step status
- **Comprehensive Pipeline**: 6-step complete analysis pipeline with automated execution
- **Enhanced Data Processing**: 7-step data processing pipeline with quality improvements
- **NDMO Compliance Pipeline**: 7-step compliance enhancement with detailed tracking
- **Interactive Status Updates**: Real-time status messages with loading animations
- **Error Handling**: Comprehensive error handling with detailed error messages

### 🔍 Smart Schema Analysis
- **Intelligent Schema Detection**: Automatically identifies schema files and analyzes structure
- **Data Type Inference**: Automatically detects data types (numeric, datetime, text, email, phone, etc.)
- **Constraint Analysis**: Identifies primary keys, foreign keys, and business rules
- **NDMO Compliance Check**: Validates schema against NDMO quality standards
- **Auto-Correction**: Automatically fixes common schema issues
- **Enhanced Progress Tracking**: Real-time analysis progress with detailed status updates

### ⚙️ Smart Data Processing
- **Schema-Based Processing**: Processes data according to schema requirements
- **Quality Improvement**: Automatically improves data quality (completeness, validity, consistency)
- **Data Type Conversion**: Converts data to appropriate types based on schema
- **Constraint Enforcement**: Applies schema constraints to data
- **Business Rule Validation**: Validates data against business rules
- **Pipeline Processing**: Step-by-step processing with visual progress tracking

### 📊 Professional Dashboard
- **Interactive Interface**: Modern, responsive dashboard with real-time updates
- **Quality Metrics**: Comprehensive quality assessment with visual charts
- **NDMO Compliance**: Real-time compliance monitoring and reporting
- **Export Capabilities**: Export analysis results and processed data
- **Multi-Tab Interface**: Organized workflow with dedicated tabs for each function
- **Enhanced UI**: Professional styling with gradients, shadows, and animations

### 🛡️ NDMO Standards Compliance
- **Comprehensive Standards**: 20+ NDMO quality standards across 5 categories
- **Real-Time Assessment**: Continuous compliance monitoring
- **Critical Standards**: Identifies and prioritizes critical compliance issues
- **Recommendations**: Provides actionable recommendations for improvement
- **Compliance Scoring**: Weighted scoring system for accurate assessment
- **Enhanced Compliance Pipeline**: Step-by-step compliance enhancement process

### 📋 Professional Reporting
- **HTML Reports**: Interactive HTML reports with embedded data and styling
- **Technical Reports**: Detailed technical documentation with implementation guides
- **Compliance Reports**: Comprehensive NDMO compliance assessment reports
- **Export Management**: Organized file management with categorized exports
- **Report Viewer**: Built-in report viewer with filtering and download capabilities

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd dataquality
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**:
   ```bash
   streamlit run professional_dashboard.py
   ```

## 🚀 Quick Deployment

### Heroku (Recommended)
```bash
# Install Heroku CLI and login
heroku login

# Create and deploy
heroku create your-app-name
git push heroku main
heroku open
```

### Streamlit Cloud
1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repository and deploy

### Railway
1. Connect GitHub repository
2. Auto-deploy with one click

### Docker Deployment
```bash
# Build and run with Docker
docker build -t sans-data-quality .
docker run -p 8501:8501 sans-data-quality

# Or use Docker Compose
docker-compose up
```

For detailed deployment instructions, see [DEPLOY.md](DEPLOY.md)

## 📖 Usage Guide

### 🚀 Quick Start - Complete Analysis Pipeline
1. **Upload Files**: Upload your schema and data files
2. **Run Complete Analysis**: Click "🚀 Complete Analysis" button
3. **Watch Pipeline**: Monitor the 6-step automated pipeline with real-time progress
4. **Review Results**: Access comprehensive reports and exports
5. **Generate HTML Reports**: Choose between Markdown or Professional HTML reports

### 🌐 NEW: HTML Report Generation
1. **Complete Analysis**: Run the complete analysis pipeline first
2. **Choose Report Format**: Select between Markdown or HTML format
3. **Generate HTML Report**: Click "🌐 Generate HTML Report" for professional output
4. **Download & View**: Download the HTML file and open in your browser
5. **Print Ready**: Use the print-friendly styling for physical reports

### 📋 Step-by-Step Usage

#### 1. Upload Files
- **Schema File**: Upload your schema definition file (Excel format)
- **Data File**: Upload your data file for processing (Excel format)

#### 2. Individual Analysis Steps
- **Schema Analysis**: Click "🔍 Analyze Schema" with enhanced progress tracking
- **Problem Analysis**: Click "🔧 Analyze Problems" to identify issues
- **NDMO Compliance**: Click "🛡️ Make NDMO Compliant" with 7-step pipeline
- **Data Processing**: Click "⚙️ Process Data" with 7-step processing pipeline

#### 3. Review Results
- **🏠 Overview Tab**: Key metrics and summary charts
- **🔍 Schema Tab**: Detailed schema analysis results
- **🔧 Problems Tab**: Problem analysis and recommendations
- **⚙️ Processing Tab**: Processing results and improvements
- **📈 Quality Tab**: Comprehensive quality assessment
- **🔄 Compare Tab**: Before/after comparison analysis
- **📋 Reports Tab**: Export analysis results and reports
- **📁 Files Tab**: View and manage saved reports
- **🗄️ SQL Tab**: Generate SQL scripts and schema templates

### 🎯 Advanced Features
- **Pipeline Processing**: Automated multi-step analysis with progress tracking
- **Real-Time Updates**: Live status updates and progress indicators
- **Professional Reports**: HTML, technical, and compliance reports
- **Export Management**: Organized file exports with categorization
- **SQL Generation**: Create database scripts from analyzed schemas

## 🚀 Advanced Pipeline Processing

### Complete Analysis Pipeline (6 Steps)
1. **📋 Schema Analysis**: Analyzing schema structure and validation rules
2. **🔧 Problem Analysis**: Identifying schema problems and compliance issues
3. **🛡️ NDMO Compliance**: Making schema NDMO compliant
4. **⚙️ Data Processing**: Processing data according to compliant schema
5. **📊 Quality Assessment**: Generating comprehensive quality reports
6. **✅ Pipeline Complete**: All analysis steps completed successfully

### Data Processing Pipeline (7 Steps)
1. **📁 Loading Data File**: Reading and validating data file structure
2. **🔍 Schema Validation**: Validating data against schema requirements
3. **🔧 Data Type Conversion**: Converting data types according to schema
4. **📊 Quality Analysis**: Analyzing data quality metrics
5. **🛠️ Quality Improvements**: Applying data quality enhancements
6. **🛡️ NDMO Compliance Check**: Validating NDMO compliance standards
7. **✅ Finalizing Results**: Preparing processing results and reports

### NDMO Compliance Pipeline (7 Steps)
1. **📋 Schema Backup**: Creating backup of original schema
2. **🔍 Compliance Analysis**: Analyzing current compliance status
3. **🔧 Primary Key Enhancement**: Adding and validating primary keys
4. **📊 Audit Trail Fields**: Adding audit trail and metadata fields
5. **🛠️ Data Type Optimization**: Optimizing data types for NDMO standards
6. **🛡️ Security & Constraints**: Adding security fields and constraints
7. **✅ Compliance Validation**: Validating final NDMO compliance

## 📋 Professional Reporting

### Interactive HTML Reports
- **Embedded Styling**: Professional CSS with gradients and animations
- **Company Branding**: SANS Data Quality System logo and branding
- **Dynamic Content**: Real-time data integration with charts and metrics
- **Responsive Design**: Optimized for desktop, tablet, and mobile viewing
- **Interactive Elements**: Hover effects, animations, and visual feedback

### Technical Documentation
- **Implementation Guides**: Step-by-step implementation instructions
- **Code Examples**: SQL and Python code snippets for integration
- **Architecture Diagrams**: System architecture and data flow diagrams
- **Best Practices**: NDMO compliance recommendations and guidelines
- **Troubleshooting**: Common issues and solutions

### Compliance Reports
- **NDMO Assessment**: Comprehensive compliance scoring and analysis
- **Before/After Comparison**: Detailed comparison of original vs compliant schemas
- **Improvement Tracking**: Progress tracking and compliance improvements
- **Recommendations**: Actionable recommendations for compliance enhancement
- **Audit Trail**: Complete audit trail of all compliance changes

## NDMO Standards

The system implements comprehensive NDMO standards across five categories:

### Data Governance (DG)
- **DG001**: Unique Identifiers
- **DG002**: Data Lineage
- **DG003**: Data Ownership

### Data Quality (DQ)
- **DQ001**: Data Completeness
- **DQ002**: Data Accuracy
- **DQ003**: Data Consistency
- **DQ004**: Data Uniqueness
- **DQ005**: Data Validity
- **DQ006**: Data Timeliness

### Data Security (DS)
- **DS001**: Data Encryption
- **DS002**: Access Control
- **DS003**: Data Masking
- **DS004**: Audit Trail

### Data Architecture (DA)
- **DA001**: Data Modeling
- **DA002**: Data Integration
- **DA003**: Data Storage

### Business Rules (BR)
- **BR001**: Business Rule Validation
- **BR002**: Data Relationships
- **BR003**: Calculated Fields

## 📁 Project Structure

```
dataquality/
├── professional_dashboard.py      # Main dashboard application with enhanced UI
├── ndmo_standards.py             # NDMO standards definitions
├── smart_schema_analyzer.py      # Schema analysis engine
├── smart_data_processor.py       # Data processing engine
├── schema_problem_analyzer.py    # Schema problem analysis and NDMO compliance
├── sql_schema_generator.py       # SQL script generation and schema templates
├── requirements.txt              # Python dependencies
├── Procfile                      # Heroku deployment configuration
├── Dockerfile                    # Docker container configuration
├── docker-compose.yml            # Docker Compose configuration
├── runtime.txt                   # Python version specification
├── setup.sh                      # Project setup script
├── .gitignore                    # Git ignore rules
├── .dockerignore                 # Docker ignore rules
├── LICENSE                       # MIT License
├── DEPLOY.md                     # Detailed deployment guide
├── assets/                       # Static assets
│   └── logo@3x.png              # Company logo
├── reports/                      # Generated reports (auto-created)
│   ├── technical_reports/        # Technical documentation
│   ├── compliance_reports/       # NDMO compliance reports
│   ├── html_reports/            # Interactive HTML reports
│   └── exports/                 # Data and schema exports
└── README.md                    # This file
```

## 🔧 Key Components

### NDMOStandardsManager
- Manages NDMO quality standards
- Calculates compliance scores
- Generates recommendations
- Validates schema compliance

### SmartSchemaAnalyzer
- Analyzes Excel schema files
- Detects data types and constraints
- Validates against NDMO standards
- Auto-corrects schema issues
- Enhanced progress tracking

### SmartDataProcessor
- Processes data according to schema
- Improves data quality
- Enforces constraints and business rules
- Calculates quality metrics
- Pipeline-based processing

### SchemaNDMOComplianceProcessor
- Analyzes schema problems
- Makes schemas NDMO compliant
- Adds audit trails and security fields
- Enhances data types and constraints
- Generates compliance reports

### SQLSchemaGenerator
- Generates CREATE TABLE SQL scripts
- Creates schema query scripts
- Supports multiple database types
- Provides schema templates
- Downloads Excel templates

### ProfessionalNDMODashboard
- Interactive Streamlit dashboard with enhanced UI
- Real-time analysis and processing with progress tracking
- Comprehensive reporting with professional styling
- Export capabilities with organized file management
- Advanced pipeline processing with visual feedback

## Quality Metrics

The system calculates comprehensive quality metrics:

- **Completeness**: Percentage of non-null values
- **Accuracy**: Data accuracy validation
- **Consistency**: Data consistency across records
- **Uniqueness**: Duplicate record detection
- **Validity**: Data format and range validation
- **Overall Score**: Weighted average of all metrics

## Compliance Assessment

NDMO compliance is assessed using:

- **Weighted Scoring**: Each standard has a specific weight
- **Critical Standards**: Some standards are marked as critical
- **Category Scoring**: Scores calculated per category
- **Overall Compliance**: Comprehensive compliance score
- **Status Determination**: Compliant/Non-Compliant/Partially Compliant

## 📤 Export Features

The system provides comprehensive export capabilities with organized file management:

### 📋 Analysis Exports
- **Schema Analysis**: JSON export of schema analysis results
- **Problem Analysis**: JSON export of problem analysis results
- **Processing Results**: JSON export of data processing results
- **Quality Reports**: Comprehensive quality assessment reports

### 📊 Data Exports
- **Processed Data**: Excel export of cleaned and processed data
- **Compliant Schema**: Excel export of NDMO-compliant schema
- **Schema Templates**: Downloadable Excel templates for schema definition

### 📄 Professional Reports
- **HTML Reports**: Interactive HTML reports with embedded styling
- **Technical Reports**: Detailed technical documentation with implementation guides
- **Compliance Reports**: Comprehensive NDMO compliance assessment reports
- **Implementation Guides**: Step-by-step implementation documentation

### 🗄️ SQL Generation
- **CREATE TABLE Scripts**: SQL scripts for various database types
- **Schema Queries**: Database schema query scripts
- **Template Downloads**: Excel schema templates for user customization

### 📁 File Management
- **Organized Storage**: Reports saved in categorized directories
- **Report Viewer**: Built-in viewer with filtering and download capabilities
- **File Management**: Clear, refresh, and manage generated reports

## 🎯 Best Practices

1. **Schema Design**: Ensure your schema follows NDMO standards
2. **Data Quality**: Clean your data before processing
3. **Pipeline Processing**: Use the complete analysis pipeline for comprehensive results
4. **Regular Monitoring**: Use the dashboard for continuous monitoring
5. **Compliance Review**: Regularly review NDMO compliance status
6. **Report Management**: Organize and archive generated reports
7. **SQL Integration**: Use generated SQL scripts for database implementation
8. **Documentation**: Keep track of processing results and improvements

## 🆘 Support

For support and questions:
- Review the dashboard interface for guidance
- Check the analysis results for recommendations
- Export reports for detailed analysis
- Monitor compliance status regularly
- Use the built-in report viewer for file management
- Refer to technical reports for implementation guidance

## 📊 System Requirements

- **Python**: 3.11+
- **Memory**: 4GB RAM minimum, 8GB recommended
- **Storage**: 1GB free space for reports and exports
- **Browser**: Modern browser with JavaScript enabled
- **Network**: Internet connection for deployment and updates

## 🔄 Version Information

**Version**: 3.0 Professional Enhanced  
**Last Updated**: September 2025  
**NDMO Standards**: 20+ Standards  
**Compliance Categories**: 5 Categories  
**Pipeline Steps**: 6-step complete analysis pipeline  
**Processing Steps**: 7-step data processing pipeline  
**Compliance Steps**: 7-step NDMO compliance pipeline  
**Export Formats**: JSON, Excel, HTML, Markdown  
**Deployment Options**: Heroku, Streamlit Cloud, Railway, Docker

## 🆕 What's New in Version 3.0

### 🚀 Enhanced Pipeline Processing
- **Real-Time Progress Tracking**: Visual progress bars with step-by-step status updates
- **Automated Pipeline Execution**: One-click complete analysis with 6-step pipeline
- **Enhanced Error Handling**: Comprehensive error handling with detailed messages
- **Interactive Status Updates**: Live status messages with loading animations

### 🎨 Professional UI Enhancements
- **Modern Design**: Enhanced styling with gradients, shadows, and animations
- **Responsive Layout**: Optimized for all screen sizes and devices
- **Company Branding**: SANS Data Quality System logo and professional branding
- **Fixed Header**: Sticky header with company logo and navigation

### 📊 Advanced Reporting
- **HTML Reports**: Interactive HTML reports with embedded styling and data
- **Technical Documentation**: Comprehensive technical reports with implementation guides
- **Report Management**: Organized file management with categorized exports
- **Built-in Viewer**: Report viewer with filtering and download capabilities

### 🗄️ SQL Generation
- **Database Scripts**: Generate CREATE TABLE scripts for multiple database types
- **Schema Templates**: Downloadable Excel templates for schema definition
- **Query Generation**: Database schema query scripts
- **Template Management**: Built-in template viewer and download system

### 📁 File Organization
- **Structured Directories**: Organized report storage in categorized folders
- **Export Management**: Enhanced export capabilities with file size tracking
- **Clean Project Structure**: Streamlined project organization for deployment
- **Docker Support**: Full Docker containerization with docker-compose support