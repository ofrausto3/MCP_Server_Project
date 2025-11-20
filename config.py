from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # MCP server
    mcp_server_host: str = "0.0.0.0"
    mcp_server_port: int = 8000

    # Postgres
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "postgres"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"

    # Spark
    spark_master: str = "local[*]"
    spark_app_name: str = "mcp-server"

    # Allow extra values in .env
    model_config = SettingsConfigDict(extra="allow", env_file=".env")

settings = Settings()
