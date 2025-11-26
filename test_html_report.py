#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test HTML Report Generator
Quick test script for the HTML report generator

Developer: AI Assistant
Purpose: Test the HTML report generator with sample data
"""

from html_report_generator import HTMLReportGenerator
import json

def test_html_report_generator():
    """Test the HTML report generator with sample data"""
    
    print("🧪 Testing HTML Report Generator...")
    
    # Initialize generator
    generator = HTMLReportGenerator()
    
    # Sample schema analysis data
    sample_schema_analysis = {
        "ndmo_compliance": {
            "overall_score": 0.167,
            "data_governance": {"score": 0.0},
            "data_quality": {"score": 0.0},
            "data_security": {"score": 0.0},
            "data_architecture": {"score": 0.0},
            "business_rules": {"score": 0.2}
        },
        "schema_analysis": {
            "table_name": "flight_tracking_data",
            "columns": [
                {
                    "name": "id",
                    "data_type": "numeric",
                    "required": True,
                    "primary_key": True,
                    "description": "معرف فريد للطائرة"
                },
                {
                    "name": "timestamp",
                    "data_type": "datetime",
                    "required": True,
                    "description": "وقت تسجيل البيانات"
                },
                {
                    "name": "src_system",
                    "data_type": "text",
                    "required": True,
                    "description": "نظام المصدر"
                },
                {
                    "name": "track_number",
                    "data_type": "numeric",
                    "required": True,
                    "description": "رقم المسار"
                },
                {
                    "name": "icao24",
                    "data_type": "numeric",
                    "required": True,
                    "description": "رمز ICAO للطائرة"
                },
                {
                    "name": "callsign",
                    "data_type": "text",
                    "required": True,
                    "description": "رمز النداء"
                },
                {
                    "name": "ssr_code",
                    "data_type": "numeric",
                    "required": True,
                    "description": "رمز SSR"
                },
                {
                    "name": "latitude",
                    "data_type": "numeric",
                    "required": True,
                    "description": "خط العرض"
                },
                {
                    "name": "longitude",
                    "data_type": "numeric",
                    "required": True,
                    "description": "خط الطول"
                },
                {
                    "name": "altitude",
                    "data_type": "numeric",
                    "required": False,
                    "description": "الارتفاع"
                },
                {
                    "name": "speed",
                    "data_type": "numeric",
                    "required": False,
                    "description": "السرعة"
                },
                {
                    "name": "heading",
                    "data_type": "numeric",
                    "required": False,
                    "description": "الاتجاه"
                },
                {
                    "name": "flight_plan_callsign",
                    "data_type": "text",
                    "required": False,
                    "description": "رمز خطة الطيران"
                },
                {
                    "name": "aircraft_type",
                    "data_type": "text",
                    "required": False,
                    "description": "نوع الطائرة"
                },
                {
                    "name": "departure_airport",
                    "data_type": "text",
                    "required": False,
                    "description": "مطار المغادرة"
                },
                {
                    "name": "arrival_airport",
                    "data_type": "text",
                    "required": False,
                    "description": "مطار الوصول"
                },
                {
                    "name": "on_ground",
                    "data_type": "boolean",
                    "required": False,
                    "description": "على الأرض"
                },
                {
                    "name": "registration_number",
                    "data_type": "text",
                    "required": False,
                    "description": "رقم التسجيل"
                },
                {
                    "name": "created_date",
                    "data_type": "datetime",
                    "required": True,
                    "description": "تاريخ الإنشاء"
                },
                {
                    "name": "modified_date",
                    "data_type": "datetime",
                    "required": True,
                    "description": "تاريخ التعديل"
                }
            ]
        }
    }
    
    # Sample data quality metrics
    sample_quality_metrics = {
        "completeness": {
            "overall": 0.85,
            "id": 1.0,
            "timestamp": 1.0,
            "src_system": 0.95,
            "track_number": 0.90,
            "icao24": 0.88,
            "callsign": 0.82,
            "latitude": 0.85,
            "longitude": 0.85,
            "altitude": 0.75,
            "speed": 0.70,
            "heading": 0.72
        },
        "uniqueness": {
            "overall": 0.78,
            "id": 1.0,
            "timestamp": 0.65,
            "src_system": 0.45,
            "track_number": 0.85,
            "icao24": 0.90,
            "callsign": 0.70
        },
        "validity": {
            "overall": 0.92,
            "id": 1.0,
            "timestamp": 0.98,
            "src_system": 0.95,
            "track_number": 0.90,
            "icao24": 0.88,
            "callsign": 0.85,
            "latitude": 0.95,
            "longitude": 0.95,
            "altitude": 0.90,
            "speed": 0.88,
            "heading": 0.85
        },
        "overall_score": 0.85
    }
    
    # Sample processing results
    sample_processing_results = {
        "original_data": {
            "rows": 15000,
            "columns": 20,
            "quality_metrics": {
                "completeness": 0.75,
                "uniqueness": 0.70,
                "validity": 0.80
            }
        },
        "processed_data": {
            "rows": 15000,
            "columns": 20,
            "quality_metrics": {
                "completeness": 0.85,
                "uniqueness": 0.78,
                "validity": 0.92
            }
        },
        "improvements_applied": [
            "تم ملء 150 قيمة مفقودة في حقل الارتفاع باستخدام القيمة المتوسطة",
            "تم تنظيف 25 قيمة غير صحيحة في حقل السرعة",
            "تم توحيد تنسيق رموز النداء",
            "تم إضافة قيود NOT NULL للحقول المطلوبة",
            "تم تحسين دقة البيانات الجغرافية",
            "تم إصلاح 10 قيم خاطئة في حقل الاتجاه",
            "تم توحيد تنسيق أرقام التسجيل",
            "تم إضافة فهرسة للمفاتيح الأساسية"
        ]
    }
    
    try:
        # Generate HTML report
        print("📊 Generating HTML report...")
        filepath = generator.generate_technical_report_html(
            sample_schema_analysis,
            sample_quality_metrics,
            sample_processing_results
        )
        
        print(f"✅ HTML report generated successfully!")
        print(f"📁 File saved at: {filepath}")
        
        # Test logo encoding
        print("🖼️ Testing logo encoding...")
        logo_data = generator.encode_logo()
        if logo_data:
            print("✅ Logo encoded successfully")
        else:
            print("⚠️ Logo encoding failed, using placeholder")
        
        return filepath
        
    except Exception as e:
        print(f"❌ Error generating HTML report: {str(e)}")
        return None

def main():
    """Main test function"""
    print("🚀 Starting HTML Report Generator Test")
    print("=" * 50)
    
    filepath = test_html_report_generator()
    
    if filepath:
        print("\n" + "=" * 50)
        print("✅ Test completed successfully!")
        print(f"📄 HTML report available at: {filepath}")
        print("🌐 Open the file in your browser to view the report")
    else:
        print("\n" + "=" * 50)
        print("❌ Test failed!")
    
    print("=" * 50)

if __name__ == "__main__":
    main()

