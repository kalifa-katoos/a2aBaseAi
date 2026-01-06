from typing import Any, Dict, List
from pydantic import BaseModel

class ToolDefinition(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Any]

class ToolResult(BaseModel):
    tool_name: str
    output: Any
    is_error: bool = False

class BaseTool:
    def __init__(self):
        self.definition = self.get_definition()

    def get_definition(self) -> ToolDefinition:
        raise NotImplementedError

    async def execute(self, **kwargs) -> ToolResult:
        raise NotImplementedError

class ToolManager:
    def __init__(self):
        self.tools: Dict[str, BaseTool] = {}

    def register_tool(self, tool: BaseTool):
        self.tools[tool.definition.name] = tool

    async def call_tool(self, name: str, **kwargs) -> ToolResult:
        if name not in self.tools:
            return ToolResult(tool_name=name, output=f"Tool {name} not found", is_error=True)
        return await self.tools[name].execute(**kwargs)

    def get_all_definitions(self) -> List[ToolDefinition]:
        return [t.definition for t in self.tools.values()]
