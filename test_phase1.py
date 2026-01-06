import asyncio
from client import EnhancedA2AClient
from models.a2a_schema import AgentCard, AgentSkill

async def test_lifecycle():
    client = EnhancedA2AClient(api_key="test_key")

    # 1. Create an AgentCard
    skill = AgentSkill(
        name="weather",
        description="Get weather info",
        parameters_schema={"location": "string"}
    )
    card = AgentCard(
        agent_id="weather_agent_001",
        name="WeatherBot",
        description="I tell the weather.",
        skills=[skill],
        endpoint_url="http://localhost:8000/a2a"
    )

    # 2. Register Agent
    client.register_agent(card)

    # 3. Create a Task
    task = client.create_task(session_id="session_123", initial_message="What is the weather in London?")
    print(f"Task Created: {task.id}, Status: {task.status}")

    # 4. Run Task
    print("Running Task...")
    updated_task = await client.run_task_async(task.id, card.agent_id)
    
    print(f"Task Status: {updated_task.status}")
    print(f"Last Message: {updated_task.history[-1].parts[0].text}")

    assert updated_task.status == "completed"
    print("Phase 1 Verification Successful!")

if __name__ == "__main__":
    asyncio.run(test_lifecycle())
