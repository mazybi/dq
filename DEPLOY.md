# 🚀 SANS Data Quality System - Deployment Guide

## 📋 Project Overview
Professional NDMO Compliance Dashboard for data quality management and analysis.

## 🛠️ Local Development Setup

### Prerequisites
- Python 3.11+
- pip

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd dataquality

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run setup script
chmod +x setup.sh
./setup.sh

# Start the application
streamlit run professional_dashboard.py
```

## 🌐 Deployment Options

### 1. Heroku Deployment

#### Prerequisites
- Heroku CLI installed
- Git repository

#### Steps
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Set environment variables (optional)
heroku config:set STREAMLIT_SERVER_HEADLESS=true

# Deploy
git add .
git commit -m "Initial deployment"
git push heroku main

# Open the app
heroku open
```

### 2. Railway Deployment

#### Steps
1. Connect your GitHub repository to Railway
2. Railway will automatically detect the `Procfile`
3. Deploy with one click

### 3. Streamlit Cloud Deployment

#### Steps
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select the main file: `professional_dashboard.py`
5. Deploy

### 4. Docker Deployment

#### Create Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "professional_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Build and Run
```bash
docker build -t sans-data-quality .
docker run -p 8501:8501 sans-data-quality
```

## 📁 Project Structure
```
dataquality/
├── assets/                 # Static assets (logos, images)
├── .streamlit/            # Streamlit configuration
├── professional_dashboard.py  # Main application
├── ndmo_standards.py      # NDMO compliance standards
├── smart_schema_analyzer.py   # Schema analysis logic
├── smart_data_processor.py    # Data processing logic
├── schema_problem_analyzer.py # Problem analysis logic
├── sql_schema_generator.py    # SQL generation logic
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── runtime.txt           # Python version
├── setup.sh             # Setup script
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

## 🔧 Configuration

### Environment Variables
- `STREAMLIT_SERVER_HEADLESS=true` - Run in headless mode
- `STREAMLIT_SERVER_PORT=8501` - Set port (default: 8501)

### Customization
- Update logo in `assets/logo@3x.png`
- Modify company branding in `professional_dashboard.py`
- Adjust NDMO standards in `ndmo_standards.py`

## 📊 Features
- ✅ Schema Analysis & Validation
- ✅ Data Quality Assessment
- ✅ NDMO Compliance Monitoring
- ✅ Professional Reporting
- ✅ SQL Script Generation
- ✅ Interactive Dashboard
- ✅ Export Capabilities

## 🛡️ Security Notes
- The application runs in headless mode for production
- CORS and XSRF protection can be configured
- No sensitive data is stored permanently

## 📞 Support
For technical support or questions, please refer to the project documentation or contact the development team.

---
**SANS Data Quality System** - Professional NDMO Compliance Dashboard

