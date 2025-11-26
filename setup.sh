#!/bin/bash

# Create necessary directories
mkdir -p reports/technical_reports
mkdir -p reports/compliance_reports
mkdir -p reports/html_reports
mkdir -p reports/exports
mkdir -p assets

# Set permissions
chmod +x run_dashboard.sh
chmod +x run_quick.sh
chmod +x start_dashboard_mac.sh

echo "✅ Project setup completed successfully!"
echo "📁 Created necessary directories"
echo "🔧 Set proper permissions"
echo "🚀 Ready for deployment!"

