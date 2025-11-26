@echo off
chcp 65001 >nul
echo 📊 داش بورد جودة البيانات NDMO
echo ==========================================
echo.
echo بدء تشغيل الداش بورد التفاعلي...
echo.

REM التحقق من وجود Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python غير مثبت أو غير موجود في PATH
    echo 💡 يرجى تثبيت Python من https://python.org
    pause
    exit /b 1
)

echo ✅ تم العثور على Python
echo.

REM تثبيت المتطلبات
echo 📦 تثبيت المتطلبات...
pip install -r requirements.txt

REM تشغيل الداش بورد
echo.
echo 🚀 تشغيل الداش بورد...
echo 🌐 سيتم فتح الداش بورد في المتصفح
echo 📍 الرابط: http://localhost:8501
echo ⏹️ لإيقاف الداش بورد: اضغط Ctrl+C
echo.

python run_dashboard.py

pause

