import asyncio
from connections.postgres_client import PostgresClient
from connections.spark_client import SparkClient

async def test_postgres():
    print("Testing PostgreSQL...")
    try:
        result = await PostgresClient.fetch("SELECT 1;")
        print("PostgreSQL OK:", result)
    except Exception as e:
        print("PostgreSQL ERROR:", e)

def test_spark():
    print("Testing Spark...")
    try:
        spark = SparkClient.get_spark()
        df = spark.range(5)
        df.show()
        print("Spark OK")
    except Exception as e:
        print("Spark ERROR:", e)

async def main():
    await test_postgres()
    test_spark()

asyncio.run(main())
