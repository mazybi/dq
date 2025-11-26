#!/bin/bash

# نظام تحليل جودة البيانات NDMO
# NDMO Data Quality Analysis System

echo "🚀 نظام تحليل جودة البيانات NDMO"
echo "=========================================="
echo ""
echo "بدء التشغيل السريع..."
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

# التحقق من وجود الملف
if [ ! -f "Billing August + Billing Schema.xlsx" ]; then
    echo "❌ لم يتم العثور على الملف: Billing August + Billing Schema.xlsx"
    echo "📁 الملفات الموجودة:"
    ls -la *.xlsx *.xls 2>/dev/null || echo "لا توجد ملفات Excel"
    echo ""
    exit 1
fi

echo "✅ تم العثور على الملف"
echo ""

# تثبيت المكتبات المطلوبة
echo "📦 تثبيت المكتبات المطلوبة..."
$PYTHON_CMD -m pip install -r requirements.txt

# تشغيل التحليل
echo ""
echo "🔍 بدء تحليل جودة البيانات..."
$PYTHON_CMD run_analysis.py

echo ""
echo "✅ تم إكمال العملية"

