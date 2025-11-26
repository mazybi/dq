#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo Script for HTML Report Generator
سكريبت العرض التوضيحي لمولد التقارير HTML

Developer: AI Assistant
Purpose: Demonstrate the HTML report generation capabilities
"""

import os
import webbrowser
from datetime import datetime

def main():
    """Main demo function"""
    print("🎬 SANS Data Quality System - HTML Report Demo")
    print("🎬 نظام إدارة جودة البيانات - عرض التقارير HTML")
    print("=" * 60)
    
    try:
        from html_report_generator import HTMLReportGenerator
        
        print("✅ HTML Report Generator loaded successfully")
        print("📊 Creating comprehensive demo data...")
        
        # Create comprehensive demo data
        demo_schema_analysis = {
            "ndmo_compliance": {
                "overall_score": 0.68,
                "data_governance": {"score": 0.7},
                "data_quality": {"score": 0.65},
                "data_security": {"score": 0.6},
                "data_architecture": {"score": 0.8},
                "business_rules": {"score": 0.65}
            },
            "schema_analysis": {
                "table_name": "customer_transactions",
                "columns": [
                    {
                        "name": "transaction_id",
                        "data_type": "numeric",
                        "required": True,
                        "primary_key": True,
                        "description": "معرف المعاملة الفريد"
                    },
                    {
                        "name": "customer_id",
                        "data_type": "numeric",
                        "required": True,
                        "description": "معرف العميل"
                    },
                    {
                        "name": "transaction_date",
                        "data_type": "datetime",
                        "required": True,
                        "description": "تاريخ المعاملة"
                    },
                    {
                        "name": "amount",
                        "data_type": "numeric",
                        "required": True,
                        "description": "مبلغ المعاملة"
                    },
                    {
                        "name": "currency",
                        "data_type": "text",
                        "required": True,
                        "description": "العملة"
                    },
                    {
                        "name": "transaction_type",
                        "data_type": "text",
                        "required": True,
                        "description": "نوع المعاملة"
                    },
                    {
                        "name": "payment_method",
                        "data_type": "text",
                        "required": False,
                        "description": "طريقة الدفع"
                    },
                    {
                        "name": "status",
                        "data_type": "text",
                        "required": True,
                        "description": "حالة المعاملة"
                    },
                    {
                        "name": "merchant_name",
                        "data_type": "text",
                        "required": False,
                        "description": "اسم التاجر"
                    },
                    {
                        "name": "location",
                        "data_type": "text",
                        "required": False,
                        "description": "الموقع"
                    },
                    {
                        "name": "created_at",
                        "data_type": "datetime",
                        "required": True,
                        "description": "تاريخ الإنشاء"
                    },
                    {
                        "name": "updated_at",
                        "data_type": "datetime",
                        "required": True,
                        "description": "تاريخ التحديث"
                    }
                ]
            }
        }
        
        demo_quality_metrics = {
            "completeness": {
                "overall": 0.88,
                "transaction_id": 1.0,
                "customer_id": 0.95,
                "transaction_date": 0.98,
                "amount": 0.92,
                "currency": 0.99,
                "transaction_type": 0.85,
                "payment_method": 0.75,
                "status": 0.90,
                "merchant_name": 0.80,
                "location": 0.70,
                "created_at": 1.0,
                "updated_at": 0.95
            },
            "uniqueness": {
                "overall": 0.82,
                "transaction_id": 1.0,
                "customer_id": 0.85,
                "transaction_date": 0.60,
                "amount": 0.70,
                "currency": 0.45,
                "transaction_type": 0.55,
                "payment_method": 0.65,
                "status": 0.50,
                "merchant_name": 0.75
            },
            "validity": {
                "overall": 0.91,
                "transaction_id": 1.0,
                "customer_id": 0.95,
                "transaction_date": 0.98,
                "amount": 0.92,
                "currency": 0.99,
                "transaction_type": 0.88,
                "payment_method": 0.85,
                "status": 0.90,
                "merchant_name": 0.82,
                "location": 0.80,
                "created_at": 1.0,
                "updated_at": 0.95
            },
            "overall_score": 0.87
        }
        
        demo_processing_results = {
            "original_data": {
                "rows": 50000,
                "columns": 12,
                "quality_metrics": {
                    "completeness": 0.82,
                    "uniqueness": 0.75,
                    "validity": 0.85
                }
            },
            "processed_data": {
                "rows": 50000,
                "columns": 12,
                "quality_metrics": {
                    "completeness": 0.88,
                    "uniqueness": 0.82,
                    "validity": 0.91
                }
            },
            "improvements_applied": [
                "تم ملء 1,250 قيمة مفقودة في حقل طريقة الدفع",
                "تم تنظيف 500 قيمة غير صحيحة في حقل المبلغ",
                "تم توحيد تنسيق العملات (SAR, USD, EUR)",
                "تم إضافة قيود NOT NULL للحقول المطلوبة",
                "تم تحسين دقة البيانات الزمنية",
                "تم إصلاح 200 قيمة خاطئة في حقل نوع المعاملة",
                "تم توحيد تنسيق أسماء التجار",
                "تم إضافة فهرسة للمفاتيح الأساسية",
                "تم تحسين أداء الاستعلامات",
                "تم إضافة حقول التدقيق المطلوبة"
            ]
        }
        
        print("✅ Demo data created successfully")
        
        # Generate HTML report
        print("🌐 Generating professional HTML report...")
        generator = HTMLReportGenerator()
        
        filepath = generator.generate_technical_report_html(
            demo_schema_analysis,
            demo_quality_metrics,
            demo_processing_results
        )
        
        print(f"✅ HTML report generated successfully!")
        print(f"📁 File saved at: {filepath}")
        
        # Get file info
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            print(f"📊 File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        
        # Ask user if they want to open the report
        print("\n" + "=" * 60)
        print("🎉 Demo completed successfully!")
        print("🌐 Professional HTML report is ready!")
        print("=" * 60)
        
        try:
            # Try to open the report in the default browser
            print("🌐 Opening report in your default browser...")
            webbrowser.open(f"file://{os.path.abspath(filepath)}")
            print("✅ Report opened in browser!")
        except Exception as e:
            print(f"⚠️ Could not open browser automatically: {e}")
            print(f"📁 Please open this file manually: {filepath}")
        
        print("\n📋 Report Features Demonstrated:")
        print("   ✅ Professional Arabic RTL layout")
        print("   ✅ Company logo integration")
        print("   ✅ Interactive charts and graphs")
        print("   ✅ Responsive design")
        print("   ✅ Data quality metrics visualization")
        print("   ✅ NDMO compliance tracking")
        print("   ✅ Processing results summary")
        print("   ✅ Implementation recommendations")
        print("   ✅ Print-ready styling")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure html_report_generator.py is in the same directory")
        return False
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎬 Demo completed successfully!")
        print("📚 For more information, see HTML_REPORT_GUIDE.md")
    else:
        print("\n❌ Demo failed!")
        print("🔧 Please check the error messages above")

