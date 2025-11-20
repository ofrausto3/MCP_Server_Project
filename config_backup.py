import os
from dataclasses import dataclass

@dataclass
class Settings:
    postgres_host: str = os.getenv("POSTGRES_HOST", "localhost")
    postgres_port: int = int(os.getenv("POSTGRES_PORT", "5432"))
    postgres_db: str = os.getenv("POSTGRES_DB", "postgres")
    postgres_user: str = os.getenv("POSTGRES_USER", "postgres")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD", "postgres")

    spark_master: str = os.getenv("SPARK_MASTER", "local[*]")
    spark_app_name: str = os.getenv("SPARK_APP_NAME", "mcp-spark-client")

    mcp_server_host: str = os.getenv("MCP_SERVER_HOST", "0.0.0.0")
    mcp_server_port: int = int(os.getenv("MCP_SERVER_PORT", "8000"))
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
