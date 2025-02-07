# import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine, text


def connect_postgres():
    """Create and return a PostgreSQL connection using SQLAlchemy"""
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    
    return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')


def write_df_to_postgres(
        table_name: str, 
        df: pd.DataFrame, 
        if_exists: str = 'replace'
    ):
    """
    Write pandas DataFrame to PostgreSQL table with schema support
    
    Args:
        table_name: Name of the target table (format: 'schema.table_name')
        df: pandas DataFrame to write
        if_exists: How to behave if table exists ('replace' or 'append')
    """
    try:
        engine = connect_postgres()
        
        # Split schema and table name
        parts = table_name.split('.')
        if len(parts) == 2:
            schema, table = parts
            # Create schema if it doesn't exist
            with engine.connect() as conn:
                conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS {schema}'))
                conn.commit()
            
            # Write DataFrame with explicit schema and table separation
            df.to_sql(
                name=table,  # just the table name
                schema=schema,  # schema as separate parameter
                con=engine,
                if_exists=if_exists,
                index=False,
                method='multi'
            )
        else:
            # For tables without schema specification
            df.to_sql(
                name=table_name,
                con=engine,
                if_exists=if_exists,
                index=False,
                method='multi'
            )
        
    except Exception as e:
        raise Exception(f"Error writing to database: {str(e)}")



def read_sql_from_postgres(
        conn, 
        query: str
    ) -> pd.DataFrame:
    """
    Read data from PostgreSQL using SQL query
    
    Args:
        conn: PostgreSQL connection object
        query: SQL query to execute
    
    Returns:
        pandas DataFrame with query results
    """
    try:
        return pd.read_sql_query(query, conn)
    except Exception as e:
        raise Exception(f"Error executing query: {str(e)}")
