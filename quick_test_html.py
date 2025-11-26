#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick Test for HTML Report Generator
اختبار سريع لمولد التقارير HTML

Developer: AI Assistant
Purpose: Quick test to demonstrate HTML report generation
"""

import os
import sys
from datetime import datetime

def main():
    """Main test function"""
    print("🚀 SANS Data Quality System - HTML Report Test")
    print("🌐 نظام إدارة جودة البيانات - اختبار التقارير HTML")
    print("=" * 60)
    
    try:
        # Import the HTML report generator
        from html_report_generator import HTMLReportGenerator
        print("✅ HTML Report Generator imported successfully")
        
        # Create sample data
        print("📊 Creating sample data...")
        
        sample_schema_analysis = {
            "ndmo_compliance": {
                "overall_score": 0.75,
                "data_governance": {"score": 0.8},
                "data_quality": {"score": 0.7},
                "data_security": {"score": 0.6},
                "data_architecture": {"score": 0.9},
                "business_rules": {"score": 0.8}
            },
            "schema_analysis": {
                "table_name": "employee_data",
                "columns": [
                    {
                        "name": "employee_id",
                        "data_type": "numeric",
                        "required": True,
                        "primary_key": True,
                        "description": "معرف الموظف الفريد"
                    },
                    {
                        "name": "full_name",
                        "data_type": "text",
                        "required": True,
                        "description": "الاسم الكامل للموظف"
                    },
                    {
                        "name": "department",
                        "data_type": "text",
                        "required": True,
                        "description": "القسم"
                    },
                    {
                        "name": "position",
                        "data_type": "text",
                        "required": False,
                        "description": "المنصب"
                    },
                    {
                        "name": "salary",
                        "data_type": "numeric",
                        "required": False,
                        "description": "الراتب"
                    },
                    {
                        "name": "hire_date",
                        "data_type": "datetime",
                        "required": True,
                        "description": "تاريخ التوظيف"
                    },
                    {
                        "name": "email",
                        "data_type": "text",
                        "required": False,
                        "description": "البريد الإلكتروني"
                    },
                    {
                        "name": "phone",
                        "data_type": "text",
                        "required": False,
                        "description": "رقم الهاتف"
                    }
                ]
            }
        }
        
        sample_quality_metrics = {
            "completeness": {
                "overall": 0.92,
                "employee_id": 1.0,
                "full_name": 0.98,
                "department": 0.95,
                "position": 0.85,
                "salary": 0.90,
                "hire_date": 1.0,
                "email": 0.80,
                "phone": 0.75
            },
            "uniqueness": {
                "overall": 0.88,
                "employee_id": 1.0,
                "full_name": 0.95,
                "department": 0.70,
                "email": 0.85
            },
            "validity": {
                "overall": 0.95,
                "employee_id": 1.0,
                "full_name": 0.98,
                "department": 0.92,
                "position": 0.90,
                "salary": 0.88,
                "hire_date": 0.99,
                "email": 0.85,
                "phone": 0.80
            },
            "overall_score": 0.92
        }
        
        sample_processing_results = {
            "original_data": {
                "rows": 1000,
                "columns": 8,
                "quality_metrics": {
                    "completeness": 0.85,
                    "uniqueness": 0.80,
                    "validity": 0.88
                }
            },
            "processed_data": {
                "rows": 1000,
                "columns": 8,
                "quality_metrics": {
                    "completeness": 0.92,
                    "uniqueness": 0.88,
                    "validity": 0.95
                }
            },
            "improvements_applied": [
                "تم ملء 50 قيمة مفقودة في حقل البريد الإلكتروني",
                "تم تنظيف 25 قيمة غير صحيحة في حقل الراتب",
                "تم توحيد تنسيق أرقام الهواتف",
                "تم إضافة قيود NOT NULL للحقول المطلوبة",
                "تم تحسين دقة بيانات التوظيف",
                "تم إصلاح 15 قيمة خاطئة في حقل القسم",
                "تم توحيد تنسيق الأسماء",
                "تم إضافة فهرسة للمفاتيح الأساسية"
            ]
        }
        
        print("✅ Sample data created successfully")
        
        # Generate HTML report
        print("🌐 Generating HTML report...")
        generator = HTMLReportGenerator()
        
        filepath = generator.generate_technical_report_html(
            sample_schema_analysis,
            sample_quality_metrics,
            sample_processing_results
        )
        
        print(f"✅ HTML report generated successfully!")
        print(f"📁 File saved at: {filepath}")
        
        # Check if file exists and get size
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            print(f"📊 File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        
        print("\n" + "=" * 60)
        print("🎉 Test completed successfully!")
        print("🌐 HTML report is ready for viewing")
        print("📱 Open the file in your browser to see the professional report")
        print("🖨️ The report is also print-ready")
        print("=" * 60)
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure all required files are in the same directory")
        return False
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

