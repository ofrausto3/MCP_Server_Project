from typing import Any, Dict, List, Optional
from connections.postgres_client import get_pool

async def execute_query(sql: str, params: Optional[List[Any]] = None) -> List[Dict[str, Any]]:
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch(sql, *(params or []))
        return [dict(r) for r in rows]

async def list_tables(schema: str = "public") -> List[Dict[str, Any]]:
    sql = '''
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 
    ORDER BY table_name;
    '''
    return await execute_query(sql, [schema])

async def get_table_schema(table: str, schema: str = "public") -> List[Dict[str, Any]]:
    sql = '''
    SELECT column_name, data_type, is_nullable
    FROM information_schema.columns
    WHERE table_schema =  AND table_name = 
    ORDER BY ordinal_position;
    '''
    return await execute_query(sql, [schema, table])
