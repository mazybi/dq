#!/bin/bash
# تشغيل داش بورد جودة البيانات NDMO - macOS

echo "📊 داش بورد جودة البيانات NDMO"
echo "=================================================="
echo "نظام شامل لتحليل جودة البيانات"
echo "وفقاً لمعايير الهيئة الوطنية لإدارة البيانات والذكاء الاصطناعي"
echo "=================================================="

# تنظيف العمليات السابقة
echo "🧹 تنظيف العمليات السابقة..."
pkill -f streamlit 2>/dev/null
sleep 2

# فحص Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 غير مثبت"
    exit 1
fi

# فحص التبعيات
echo "🔍 فحص التبعيات..."
python3 -c "import streamlit, pandas, numpy, plotly, openpyxl" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ جميع التبعيات متوفرة"
else
    echo "❌ بعض التبعيات مفقودة - جاري التثبيت..."
    pip3 install -r requirements.txt
fi

# إعداد متغيرات البيئة
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_SERVER_ENABLE_CORS=false
export STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false

echo "🌐 سيتم فتح الداش بورد في المتصفح..."
echo "📍 الرابط: http://localhost:8501"
echo "⏹️ لإيقاف الداش بورد: اضغط Ctrl+C"
echo "=================================================="

# تشغيل الداش بورد
echo "🚀 تشغيل الداش بورد التفاعلي..."
python3 -m streamlit run dashboard.py \
    --server.port 8501 \
    --server.address localhost \
    --server.headless true \
    --server.enableCORS false \
    --server.enableXsrfProtection false \
    --browser.gatherUsageStats false &

# انتظار بدء التشغيل
sleep 5

# فتح المتصفح
echo "🌐 فتح المتصفح..."
open http://localhost:8501

# انتظار انتهاء العملية
wait











