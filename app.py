#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SANS Data Quality System - Main Application Entry Point
Professional NDMO Compliance Dashboard

This file serves as the main entry point for deployment platforms
that expect an app.py file instead of direct streamlit commands.
"""

import subprocess
import sys
import os

def main():
    """Main application entry point"""
    try:
        # Change to the directory containing the dashboard
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        
        # Run the Streamlit dashboard
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "professional_dashboard.py",
            "--server.port=8502",
            "--server.address=0.0.0.0",
            "--server.headless=true"
        ])
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

