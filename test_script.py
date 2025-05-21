from fastmcp import Client

# The Client automatically uses StreamableHttpTransport for HTTP URLs
client = Client("http://mcp-service:8000/mcp")

async def list_tools():
    async with client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

async def echo():
    async with client:
        response = await client.call_tool("echo",{})
        print(f"Echo: {response}")


await list_tools()
await echo()