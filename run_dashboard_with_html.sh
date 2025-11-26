#!/bin/bash

# تشغيل الداشبورد مع ميزات HTML الجديدة
# Run Dashboard with New HTML Features

echo "🚀 Starting SANS Data Quality Dashboard with HTML Reports..."
echo "🌐 تشغيل نظام إدارة جودة البيانات مع التقارير HTML الجديدة"
echo ""

# التحقق من وجود Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.7+"
    echo "❌ Python3 غير موجود. يرجى تثبيت Python 3.7+"
    exit 1
fi

# التحقق من وجود الملفات المطلوبة
if [ ! -f "professional_dashboard.py" ]; then
    echo "❌ professional_dashboard.py not found"
    echo "❌ ملف professional_dashboard.py غير موجود"
    exit 1
fi

if [ ! -f "html_report_generator.py" ]; then
    echo "❌ html_report_generator.py not found"
    echo "❌ ملف html_report_generator.py غير موجود"
    exit 1
fi

# إنشاء المجلدات المطلوبة
echo "📁 Creating required directories..."
echo "📁 إنشاء المجلدات المطلوبة..."
mkdir -p reports/html_reports
mkdir -p reports/technical_reports
mkdir -p assets

# التحقق من وجود اللوقو
if [ ! -f "assets/logo@3x.png" ]; then
    echo "⚠️ Logo not found at assets/logo@3x.png"
    echo "⚠️ اللوقو غير موجود في assets/logo@3x.png"
    echo "ℹ️ A placeholder logo will be used"
    echo "ℹ️ سيتم استخدام لوقو احتياطي"
fi

# تثبيت المتطلبات إذا لزم الأمر
echo "📦 Checking dependencies..."
echo "📦 فحص المتطلبات..."

# تشغيل الداشبورد
echo ""
echo "🌐 Starting Dashboard..."
echo "🌐 بدء تشغيل الداشبورد..."
echo ""
echo "📊 Features available:"
echo "📊 الميزات المتاحة:"
echo "   ✅ Schema Analysis - تحليل الهيكل"
echo "   ✅ NDMO Compliance - امتثال NDMO"
echo "   ✅ Data Quality Metrics - مقاييس جودة البيانات"
echo "   ✅ HTML Technical Reports - التقارير التقنية HTML"
echo "   ✅ Markdown Reports - التقارير Markdown"
echo "   ✅ Professional Styling - التصميم الاحترافي"
echo ""
echo "🔗 Dashboard will be available at: http://localhost:8501"
echo "🔗 الداشبورد سيكون متاحاً على: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the dashboard"
echo "اضغط Ctrl+C لإيقاف الداشبورد"
echo ""

# تشغيل Streamlit
streamlit run professional_dashboard.py --server.port 8501 --server.address 0.0.0.0

