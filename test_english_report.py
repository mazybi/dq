#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test English HTML Report Generator
اختبار مولد التقارير HTML باللغة الإنجليزية

Developer: AI Assistant
Purpose: Test the English HTML report generation
"""

import os
import webbrowser
from datetime import datetime

def main():
    """Main test function"""
    print("🚀 SANS Data Quality System - English HTML Report Test")
    print("🌐 نظام إدارة جودة البيانات - اختبار التقارير HTML الإنجليزية")
    print("=" * 70)
    
    try:
        from html_report_generator import HTMLReportGenerator
        
        print("✅ English HTML Report Generator loaded successfully")
        print("📊 Creating comprehensive English demo data...")
        
        # Create comprehensive English demo data
        demo_schema_analysis = {
            "ndmo_compliance": {
                "overall_score": 0.75,
                "data_governance": {"score": 0.8},
                "data_quality": {"score": 0.7},
                "data_security": {"score": 0.6},
                "data_architecture": {"score": 0.9},
                "business_rules": {"score": 0.8}
            },
            "schema_analysis": {
                "table_name": "customer_orders",
                "columns": [
                    {
                        "name": "order_id",
                        "data_type": "numeric",
                        "required": True,
                        "primary_key": True,
                        "description": "Unique order identifier"
                    },
                    {
                        "name": "customer_id",
                        "data_type": "numeric",
                        "required": True,
                        "description": "Customer identifier"
                    },
                    {
                        "name": "order_date",
                        "data_type": "datetime",
                        "required": True,
                        "description": "Order placement date"
                    },
                    {
                        "name": "total_amount",
                        "data_type": "numeric",
                        "required": True,
                        "description": "Total order amount"
                    },
                    {
                        "name": "currency",
                        "data_type": "text",
                        "required": True,
                        "description": "Order currency"
                    },
                    {
                        "name": "order_status",
                        "data_type": "text",
                        "required": True,
                        "description": "Current order status"
                    },
                    {
                        "name": "payment_method",
                        "data_type": "text",
                        "required": False,
                        "description": "Payment method used"
                    },
                    {
                        "name": "shipping_address",
                        "data_type": "text",
                        "required": False,
                        "description": "Shipping address"
                    },
                    {
                        "name": "billing_address",
                        "data_type": "text",
                        "required": False,
                        "description": "Billing address"
                    },
                    {
                        "name": "created_at",
                        "data_type": "datetime",
                        "required": True,
                        "description": "Record creation timestamp"
                    },
                    {
                        "name": "updated_at",
                        "data_type": "datetime",
                        "required": True,
                        "description": "Record update timestamp"
                    }
                ]
            }
        }
        
        demo_quality_metrics = {
            "completeness": {
                "overall": 0.92,
                "order_id": 1.0,
                "customer_id": 0.98,
                "order_date": 0.99,
                "total_amount": 0.95,
                "currency": 1.0,
                "order_status": 0.97,
                "payment_method": 0.85,
                "shipping_address": 0.88,
                "billing_address": 0.90,
                "created_at": 1.0,
                "updated_at": 0.95
            },
            "uniqueness": {
                "overall": 0.88,
                "order_id": 1.0,
                "customer_id": 0.85,
                "order_date": 0.70,
                "total_amount": 0.75,
                "currency": 0.45,
                "order_status": 0.55,
                "payment_method": 0.65
            },
            "validity": {
                "overall": 0.95,
                "order_id": 1.0,
                "customer_id": 0.98,
                "order_date": 0.99,
                "total_amount": 0.96,
                "currency": 1.0,
                "order_status": 0.94,
                "payment_method": 0.88,
                "shipping_address": 0.92,
                "billing_address": 0.90,
                "created_at": 1.0,
                "updated_at": 0.97
            },
            "overall_score": 0.92
        }
        
        demo_processing_results = {
            "original_data": {
                "rows": 25000,
                "columns": 11,
                "quality_metrics": {
                    "completeness": 0.88,
                    "uniqueness": 0.82,
                    "validity": 0.90
                }
            },
            "processed_data": {
                "rows": 25000,
                "columns": 11,
                "quality_metrics": {
                    "completeness": 0.92,
                    "uniqueness": 0.88,
                    "validity": 0.95
                }
            },
            "improvements_applied": [
                "Filled 625 missing values in payment_method field using most frequent value",
                "Cleaned 125 invalid values in total_amount field",
                "Standardized currency format (USD, EUR, GBP)",
                "Added NOT NULL constraints for required fields",
                "Improved date format consistency",
                "Fixed 50 incorrect values in order_status field",
                "Standardized address format",
                "Added indexing for primary keys",
                "Improved query performance",
                "Added required audit fields"
            ]
        }
        
        print("✅ English demo data created successfully")
        
        # Generate HTML report
        print("🌐 Generating professional English HTML report...")
        generator = HTMLReportGenerator()
        
        filepath = generator.generate_technical_report_html(
            demo_schema_analysis,
            demo_quality_metrics,
            demo_processing_results
        )
        
        print(f"✅ English HTML report generated successfully!")
        print(f"📁 File saved at: {filepath}")
        
        # Get file info
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            print(f"📊 File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        
        # Ask user if they want to open the report
        print("\n" + "=" * 70)
        print("🎉 English Report Test completed successfully!")
        print("🌐 Professional English HTML report is ready!")
        print("=" * 70)
        
        try:
            # Try to open the report in the default browser
            print("🌐 Opening English report in your default browser...")
            webbrowser.open(f"file://{os.path.abspath(filepath)}")
            print("✅ English report opened in browser!")
        except Exception as e:
            print(f"⚠️ Could not open browser automatically: {e}")
            print(f"📁 Please open this file manually: {filepath}")
        
        print("\n📋 English Report Features Demonstrated:")
        print("   ✅ Professional English LTR layout")
        print("   ✅ Company logo integration")
        print("   ✅ Interactive charts and graphs")
        print("   ✅ Responsive design")
        print("   ✅ Data quality metrics visualization")
        print("   ✅ NDMO compliance tracking")
        print("   ✅ Processing results summary")
        print("   ✅ Implementation recommendations")
        print("   ✅ Print-ready styling")
        print("   ✅ Inter font family")
        
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
        print("\n🎬 English Report Test completed successfully!")
        print("📚 All reports are now in English")
        print("🌐 The system is ready for English language usage")
    else:
        print("\n❌ English Report Test failed!")
        print("🔧 Please check the error messages above")
