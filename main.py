import uvicorn
from fastapi import FastAPI
from config import settings

app = FastAPI(title="MCP Server")

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "postgres": False,
        "spark": False,
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.mcp_server_host,
        port=settings.mcp_server_port,
        reload=True,
    )
