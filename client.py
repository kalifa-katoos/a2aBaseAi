from typing import List, Optional, Dict, Any
from models.a2a_schema import AgentCard, Task, Message, Part, TextPart
from tools.base import ToolManager
from intelligence.memory import MemoryManager
from intelligence.router import ModelRouter
import httpx # For calling LLM providers or A2ABase API

class EnhancedA2AClient:
    def __init__(self, api_key: str, base_url: str = "https://api.a2abase.ai/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.agents: Dict[str, AgentCard] = {}
        self.tasks: Dict[str, Task] = {}
        self.tool_manager = ToolManager()
        self.memory_manager = MemoryManager()
        self.model_router = ModelRouter()

    def register_agent(self, card: AgentCard):
        """Registers an agent capability for discovery."""
        self.agents[card.agent_id] = card
        print(f"Agent '{card.name}' registered.")

    def create_task(self, session_id: str, initial_message: str) -> Task:
        """Creates a new A2A Task."""
        task = Task(session_id=session_id)
        msg = Message(role="user", parts=[TextPart(text=initial_message)])
        task.history.append(msg)
        self.tasks[task.id] = task
        return task

    async def run_task_async(self, task_id: str, agent_id: str):
        """Sends the task to a specific agent and waits for completion."""
        task = self.tasks.get(task_id)
        agent = self.agents.get(agent_id)
        
        if not task or not agent:
            raise ValueError("Invalid task_id or agent_id")

        task.status = "working"
        
        # In a real implementation, this would send a JSON-RPC request to the agent's endpoint
        print(f"Sending Task {task_id} to Agent {agent.name} at {agent.endpoint_url}...")
        
        # Mocking the response for now
        # In Phase 2, this will connect to LLMs or Remote Agents
        response_text = f"Hello! I am {agent.name}. I received your task."
        
        task.history.append(Message(role="agent", parts=[TextPart(text=response_text)]))
        task.status = "completed"
        return task

    def get_task_status(self, task_id: str) -> str:
        task = self.tasks.get(task_id)
        return task.status if task else "not_found"
