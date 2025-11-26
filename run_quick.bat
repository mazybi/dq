@echo off
chcp 65001 >nul
echo 🚀 نظام تحليل جودة البيانات NDMO
echo ==========================================
echo.
echo بدء التشغيل السريع...
echo.

REM التحقق من وجود Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python غير مثبت أو غير موجود في PATH
    echo 💡 يرجى تثبيت Python من https://python.org
    pause
    exit /b 1
)

REM التحقق من وجود الملف
if not exist "Billing August + Billing Schema.xlsx" (
    echo ❌ لم يتم العثور على الملف: Billing August + Billing Schema.xlsx
    echo 📁 الملفات الموجودة:
    dir *.xlsx *.xls 2>nul
    echo.
    pause
    exit /b 1
)

echo ✅ تم العثور على الملف
echo.

REM تثبيت المكتبات المطلوبة
echo 📦 تثبيت المكتبات المطلوبة...
pip install -r requirements.txt

REM تشغيل التحليل
echo.
echo 🔍 بدء تحليل جودة البيانات...
python run_analysis.py

echo.
echo ✅ تم إكمال العملية
pause

