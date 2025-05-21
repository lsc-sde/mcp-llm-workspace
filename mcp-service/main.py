import logging
from mcp.server.fastmcp import FastMCP, Context

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP("LLM MCP Server")

@mcp.tool(name="Echo", description="Repeats the message back to you")
def echo(message: str) -> str:
    return f"You said: {message}"


    
# Commented currently to run in dev inspector
if __name__ == "__main__":
    logger.info("Starting FastMCP server...")
    mcp.run(transport="sse")

