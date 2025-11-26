"""
SQL Schema Generator for NDMO Data Quality Dashboard
Generates SQL scripts and schema templates for various database systems
"""

import pandas as pd
from typing import Dict, Any, List


class SQLSchemaGenerator:
    """Generate SQL scripts and schema templates"""
    
    def __init__(self):
        self.database_type_mapping = {
            'mysql': {
                'varchar': 'VARCHAR',
                'text': 'TEXT',
                'int': 'INT',
                'bigint': 'BIGINT',
                'decimal': 'DECIMAL',
                'float': 'FLOAT',
                'double': 'DOUBLE',
                'date': 'DATE',
                'datetime': 'DATETIME',
                'timestamp': 'TIMESTAMP',
                'boolean': 'BOOLEAN',
                'json': 'JSON'
            },
            'postgresql': {
                'varchar': 'VARCHAR',
                'text': 'TEXT',
                'int': 'INTEGER',
                'bigint': 'BIGINT',
                'decimal': 'DECIMAL',
                'float': 'REAL',
                'double': 'DOUBLE PRECISION',
                'date': 'DATE',
                'datetime': 'TIMESTAMP',
                'timestamp': 'TIMESTAMP',
                'boolean': 'BOOLEAN',
                'json': 'JSONB'
            },
            'sqlserver': {
                'varchar': 'NVARCHAR',
                'text': 'NTEXT',
                'int': 'INT',
                'bigint': 'BIGINT',
                'decimal': 'DECIMAL',
                'float': 'FLOAT',
                'double': 'FLOAT',
                'date': 'DATE',
                'datetime': 'DATETIME2',
                'timestamp': 'DATETIME2',
                'boolean': 'BIT',
                'json': 'NVARCHAR(MAX)'
            },
            'oracle': {
                'varchar': 'VARCHAR2',
                'text': 'CLOB',
                'int': 'NUMBER',
                'bigint': 'NUMBER',
                'decimal': 'NUMBER',
                'float': 'BINARY_FLOAT',
                'double': 'BINARY_DOUBLE',
                'date': 'DATE',
                'datetime': 'TIMESTAMP',
                'timestamp': 'TIMESTAMP',
                'boolean': 'NUMBER(1)',
                'json': 'CLOB'
            },
            'sqlite': {
                'varchar': 'TEXT',
                'text': 'TEXT',
                'int': 'INTEGER',
                'bigint': 'INTEGER',
                'decimal': 'REAL',
                'float': 'REAL',
                'double': 'REAL',
                'date': 'TEXT',
                'datetime': 'TEXT',
                'timestamp': 'TEXT',
                'boolean': 'INTEGER',
                'json': 'TEXT'
            }
        }
    
    def generate_create_table_sql(self, schema_analysis: Dict[str, Any], table_name: str, database_type: str) -> str:
        """Generate CREATE TABLE SQL script"""
        try:
            schema_info = schema_analysis.get('schema_analysis', {})
            columns = schema_info.get('columns', [])
            
            if not columns:
                return "-- No columns found in schema analysis"
            
            # Start building SQL
            sql_lines = [f"-- CREATE TABLE script for {database_type.upper()}"]
            sql_lines.append(f"-- Generated for table: {table_name}")
            sql_lines.append("")
            sql_lines.append(f"CREATE TABLE {table_name} (")
            
            # Process columns
            column_definitions = []
            primary_keys = []
            
            for col in columns:
                col_name = col.get('name', '')
                data_type = col.get('data_type', 'varchar')
                nullable = col.get('nullable', True)
                is_primary = col.get('primary_key', False)
                is_unique = col.get('unique', False)
                default_value = col.get('constraints', {}).get('default_value')
                max_length = col.get('constraints', {}).get('max_length')
                description = col.get('description', '')
                
                # Map data type
                mapped_type = self._map_data_type(data_type, database_type, max_length)
                
                # Build column definition
                col_def = f"    {col_name} {mapped_type}"
                
                # Add constraints
                if not nullable:
                    col_def += " NOT NULL"
                
                if default_value is not None:
                    if database_type == 'sqlserver' and data_type in ['varchar', 'text']:
                        col_def += f" DEFAULT '{default_value}'"
                    else:
                        col_def += f" DEFAULT '{default_value}'"
                
                if is_unique and not is_primary:
                    col_def += " UNIQUE"
                
                # Add comment if available
                if description and database_type in ['mysql', 'postgresql']:
                    col_def += f" COMMENT '{description}'"
                
                column_definitions.append(col_def)
                
                if is_primary:
                    primary_keys.append(col_name)
            
            # Add column definitions
            sql_lines.extend(column_definitions)
            
            # Add primary key constraint
            if primary_keys:
                if database_type == 'sqlserver':
                    sql_lines.append(f"    CONSTRAINT PK_{table_name} PRIMARY KEY ({', '.join(primary_keys)})")
                else:
                    sql_lines.append(f"    PRIMARY KEY ({', '.join(primary_keys)})")
            
            # Close table definition
            sql_lines.append(");")
            sql_lines.append("")
            
            # Add indexes for unique columns
            for col in columns:
                if col.get('unique', False) and not col.get('primary_key', False):
                    col_name = col.get('name', '')
                    sql_lines.append(f"CREATE INDEX idx_{table_name}_{col_name} ON {table_name} ({col_name});")
            
            # Add table comment
            table_description = schema_info.get('description', f'Table {table_name}')
            if database_type in ['mysql', 'postgresql']:
                sql_lines.append(f"ALTER TABLE {table_name} COMMENT = '{table_description}';")
            
            return "\n".join(sql_lines)
            
        except Exception as e:
            return f"-- Error generating SQL: {str(e)}"
    
    def generate_schema_query(self, table_name: str, database_type: str) -> str:
        """Generate SQL query to retrieve schema information"""
        queries = {
            'mysql': f"""
-- MySQL Schema Query
SELECT 
    COLUMN_NAME as 'Column Name',
    DATA_TYPE as 'Data Type',
    IS_NULLABLE as 'Nullable',
    COLUMN_KEY as 'Key',
    COLUMN_DEFAULT as 'Default',
    EXTRA as 'Extra',
    COLUMN_COMMENT as 'Comment'
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = '{table_name}'
ORDER BY ORDINAL_POSITION;
""",
            'postgresql': f"""
-- PostgreSQL Schema Query
SELECT 
    column_name as "Column Name",
    data_type as "Data Type",
    is_nullable as "Nullable",
    column_default as "Default",
    character_maximum_length as "Max Length"
FROM information_schema.columns 
WHERE table_name = '{table_name}'
ORDER BY ordinal_position;
""",
            'sqlserver': f"""
-- SQL Server Schema Query
SELECT 
    c.COLUMN_NAME as 'Column Name',
    c.DATA_TYPE as 'Data Type',
    c.IS_NULLABLE as 'Nullable',
    c.COLUMN_DEFAULT as 'Default',
    c.CHARACTER_MAXIMUM_LENGTH as 'Max Length',
    CASE WHEN pk.COLUMN_NAME IS NOT NULL THEN 'YES' ELSE 'NO' END as 'Primary Key'
FROM INFORMATION_SCHEMA.COLUMNS c
LEFT JOIN (
    SELECT ku.TABLE_NAME, ku.COLUMN_NAME
    FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
    INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE ku
        ON tc.CONSTRAINT_TYPE = 'PRIMARY KEY' 
        AND tc.CONSTRAINT_NAME = ku.CONSTRAINT_NAME
) pk ON c.TABLE_NAME = pk.TABLE_NAME AND c.COLUMN_NAME = pk.COLUMN_NAME
WHERE c.TABLE_NAME = '{table_name}'
ORDER BY c.ORDINAL_POSITION;
""",
            'oracle': f"""
-- Oracle Schema Query
SELECT 
    column_name as "Column Name",
    data_type as "Data Type",
    nullable as "Nullable",
    data_default as "Default",
    data_length as "Max Length"
FROM user_tab_columns 
WHERE table_name = UPPER('{table_name}')
ORDER BY column_id;
""",
            'sqlite': f"""
-- SQLite Schema Query
PRAGMA table_info({table_name});
"""
        }
        
        return queries.get(database_type, f"-- Schema query for {database_type} not available")
    
    def create_schema_template(self) -> Dict[str, List]:
        """Create a schema template with sample data"""
        return {
            'COLUMN_NAME': [
                'id',
                'name',
                'email',
                'phone',
                'age',
                'salary',
                'hire_date',
                'department',
                'is_active',
                'created_at'
            ],
            'DATA_TYPE': [
                'int',
                'varchar',
                'varchar',
                'varchar',
                'int',
                'decimal',
                'date',
                'varchar',
                'boolean',
                'datetime'
            ],
            'NULLABLE': [
                'NO',
                'NO',
                'NO',
                'YES',
                'YES',
                'YES',
                'NO',
                'NO',
                'NO',
                'NO'
            ],
            'PRIMARY_KEY': [
                'YES',
                'NO',
                'NO',
                'NO',
                'NO',
                'NO',
                'NO',
                'NO',
                'NO',
                'NO'
            ],
            'UNIQUE': [
                'YES',
                'NO',
                'YES',
                'NO',
                'NO',
                'NO',
                'NO',
                'NO',
                'NO',
                'NO'
            ],
            'DEFAULT_VALUE': [
                'AUTO_INCREMENT',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                'TRUE',
                'CURRENT_TIMESTAMP'
            ],
            'DESCRIPTION': [
                'Primary key identifier',
                'Full name of the person',
                'Email address (must be unique)',
                'Phone number (optional)',
                'Age in years (optional)',
                'Monthly salary (optional)',
                'Date of hire',
                'Department name',
                'Active status flag',
                'Record creation timestamp'
            ],
            'MIN_LENGTH': [
                '',
                '2',
                '5',
                '10',
                '',
                '',
                '',
                '2',
                '',
                ''
            ],
            'MAX_LENGTH': [
                '',
                '100',
                '255',
                '20',
                '',
                '',
                '',
                '50',
                '',
                ''
            ],
            'MIN_VALUE': [
                '1',
                '',
                '',
                '',
                '18',
                '0',
                '',
                '',
                '',
                ''
            ],
            'MAX_VALUE': [
                '',
                '',
                '',
                '',
                '100',
                '1000000',
                '',
                '',
                '',
                ''
            ],
            'INDEXED': [
                'YES',
                'NO',
                'YES',
                'NO',
                'NO',
                'NO',
                'YES',
                'YES',
                'NO',
                'NO'
            ]
        }
    
    def _map_data_type(self, data_type: str, database_type: str, max_length: int = None) -> str:
        """Map standard data type to database-specific type"""
        base_type = data_type.lower()
        mapped = self.database_type_mapping.get(database_type, {}).get(base_type, data_type.upper())
        
        # Add length for varchar types
        if base_type in ['varchar', 'text'] and max_length:
            if database_type == 'mysql':
                return f"VARCHAR({max_length})"
            elif database_type == 'postgresql':
                return f"VARCHAR({max_length})"
            elif database_type == 'sqlserver':
                return f"NVARCHAR({max_length})"
            elif database_type == 'oracle':
                return f"VARCHAR2({max_length})"
        
        return mapped