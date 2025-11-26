#!/bin/bash

# داش بورد جودة البيانات NDMO
# NDMO Data Quality Dashboard

echo "📊 داش بورد جودة البيانات NDMO"
echo "=========================================="
echo ""
echo "بدء تشغيل الداش بورد التفاعلي..."
echo ""

# التحقق من وجود Python
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Python غير مثبت أو غير موجود في PATH"
        echo "💡 يرجى تثبيت Python من https://python.org"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "✅ تم العثور على Python: $($PYTHON_CMD --version)"

# تثبيت المتطلبات
echo ""
echo "📦 تثبيت المتطلبات..."
$PYTHON_CMD -m pip install -r requirements.txt

# تشغيل الداش بورد
echo ""
echo "🚀 تشغيل الداش بورد..."
echo "🌐 سيتم فتح الداش بورد في المتصفح"
echo "📍 الرابط: http://localhost:8501"
echo "⏹️ لإيقاف الداش بورد: اضغط Ctrl+C"
echo ""

$PYTHON_CMD run_dashboard.py

