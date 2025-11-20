import asyncio

from tools.spark_tools import submit_spark_job, get_job_status, list_spark_jobs
from tools.postgres_tools import execute_query, get_table_schema, list_tables


async def test_spark_tools():
    print("=== Testing Spark tools ===")
    result_submit = await submit_spark_job("print('hello from spark')")
    print("submit_spark_job:", result_submit)

    job_id = result_submit.get("job_id", "job-123")
    result_status = await get_job_status(job_id)
    print("get_job_status:", result_status)

    result_list = await list_spark_jobs()
    print("list_spark_jobs:", result_list)


async def test_postgres_tools():
    print("\n=== Testing Postgres tools ===")
    result_query = await execute_query("SELECT 1;")
    print("execute_query:", result_query)

    result_schema = await get_table_schema("users")
    print("get_table_schema:", result_schema)

    result_tables = await list_tables()
    print("list_tables:", result_tables)


async def main():
    await test_spark_tools()
    await test_postgres_tools()


if __name__ == "__main__":
    asyncio.run(main())
