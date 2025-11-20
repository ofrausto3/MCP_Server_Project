from typing import Dict, Any, List
from .base import make_resource


def postgres_schema_info(schema_name: str = "public") -> Dict[str, Any]:
    """
    Resource: postgres://schema/{schema_name} (stub).
    """
    tables: List[str] = ["users", "orders", "products"]
    data = {
        "schema": schema_name,
        "tables": tables,
        "views": [],
        "functions": [],
    }
    return make_resource(f"postgres://schema/{schema_name}", data)


def postgres_table_data(table_name: str, limit: int = 100) -> Dict[str, Any]:
    """
    Resource: postgres://tables/{table_name}/data (stub).
    """
    data = {
        "table": table_name,
        "limit": limit,
        "rows": [],
    }
    return make_resource(f"postgres://tables/{table_name}/data", data)
