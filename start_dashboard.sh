#!/bin/bash

# تشغيل الداشبورد مع الميزات الجديدة
# Start Dashboard with New HTML Features

clear
echo "🚀 SANS Data Quality System"
echo "🌐 نظام إدارة جودة البيانات"
echo "=================================="
echo ""

# التحقق من Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.7+"
    exit 1
fi

# التحقق من Streamlit
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "📦 Installing Streamlit..."
    pip3 install streamlit
fi

# إنشاء المجلدات
mkdir -p reports/html_reports
mkdir -p reports/technical_reports
mkdir -p assets

echo "✅ Environment ready"
echo "✅ البيئة جاهزة"
echo ""

echo "🌐 Starting Dashboard with HTML Reports..."
echo "🌐 بدء تشغيل الداشبورد مع التقارير HTML..."
echo ""
echo "📊 Available Features:"
echo "📊 الميزات المتاحة:"
echo "   ✅ Schema Analysis - تحليل الهيكل"
echo "   ✅ NDMO Compliance - امتثال NDMO"
echo "   ✅ Data Quality Metrics - مقاييس جودة البيانات"
echo "   ✅ HTML Technical Reports - التقارير التقنية HTML"
echo "   ✅ Markdown Reports - التقارير Markdown"
echo "   ✅ Professional Styling - التصميم الاحترافي"
echo ""
echo "🔗 Dashboard URL: http://localhost:8501"
echo "🔗 رابط الداشبورد: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop"
echo "اضغط Ctrl+C للإيقاف"
echo ""

# تشغيل الداشبورد
streamlit run professional_dashboard.py --server.port 8501 --server.address 0.0.0.0

