import asyncio
from client import EnhancedA2AClient
from tools.search import SearchTool
from tools.mcp_bridge import McpBridge

async def test_tools():
    client = EnhancedA2AClient(api_key="test_key")

    # 1. Register Native Tool
    search_tool = SearchTool()
    client.tool_manager.register_tool(search_tool)

    # 2. Register MCP Tool (Mock)
    mcp_tool = McpBridge({
        "name": "gmail_send",
        "description": "Send emails via Gmail",
        "inputSchema": {"properties": {"to": {"type": "string"}, "body": {"type": "string"}}}
    })
    client.tool_manager.register_tool(mcp_tool)

    # 3. List Tools
    tools = client.tool_manager.get_all_definitions()
    print(f"Registered Tools: {[t.name for t in tools]}")
    assert len(tools) == 2

    # 4. Execute Search Tool
    print("Testing Search Tool...")
    result = await client.tool_manager.call_tool("web_search", query="What is A2A protocol?")
    print(f"Search Output: {result.output}")
    assert "Search results for" in result.output

    # 5. Execute MCP Tool
    print("Testing MCP Bridge...")
    mcp_result = await client.tool_manager.call_tool("gmail_send", to="test@example.com", body="Hello")
    print(f"MCP Output: {mcp_result.output}")
    assert "MCP Tool gmail_send execution mock" in mcp_result.output

    print("Phase 2 Verification Successful!")

if __name__ == "__main__":
    asyncio.run(test_tools())
