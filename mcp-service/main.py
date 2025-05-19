import logging
from mcp.server.fastmcp import FastMCP, Context

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP("LLM MCP Server")

@mcp.tool()
def echo(ctx: Context) -> str:
    return f"You said {ctx.input}"

# Commented currently to run in dev inspector
if __name__ == "__main__":
    logger.info("Starting MCP server...")
    mcp.run()

