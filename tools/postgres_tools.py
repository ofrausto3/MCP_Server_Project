from typing import Dict, Any, List


def execute_query(sql: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """
    Week 1: Execute a SELECT query (stub).
    """
    return {
        "sql": sql,
        "params": params or {},
        "rows": [],
    }


def get_table_schema(table_name: str) -> Dict[str, Any]:
    """
    Week 1: Get table structure (stub).
    """
    return {
        "table": table_name,
        "columns": [
            {"name": "id", "type": "integer"},
            {"name": "value", "type": "text"},
        ],
    }


def list_tables(schema_name: str | None = None) -> Dict[str, Any]:
    """
    Week 1: List available tables (stub).
    """
    tables: List[str] = ["users", "orders", "products"]
    return {
        "schema": schema_name or "public",
        "tables": tables,
    }


# ---------------------------
# Week 2: Advanced Postgres tools
# ---------------------------

def execute_dml(sql: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """
    Week 2: Execute INSERT/UPDATE/DELETE (stub).
    """
    return {
        "sql": sql,
        "params": params or {},
        "rowcount": 0,
        "status": "ok",
    }


def create_table(table_name: str, columns: Dict[str, str]) -> Dict[str, Any]:
    """
    Week 2: Create a new table (stub).
    columns is a dict like {"id": "integer", "name": "text"}.
    """
    return {
        "table": table_name,
        "columns": columns,
        "status": "created_stub",
    }


def bulk_load_from_spark(dataframe_ref: str, target_table: str) -> Dict[str, Any]:
    """
    Week 2: Transfer data from Spark to PostgreSQL (stub).
    In a real implementation, dataframe_ref would identify a Spark DataFrame.
    """
    return {
        "dataframe_ref": dataframe_ref,
        "target_table": target_table,
        "rows_loaded": 0,
        "status": "bulk_load_stub",
    }
