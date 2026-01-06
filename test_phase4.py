import asyncio
from client import EnhancedA2AClient

async def test_intelligence():
    client = EnhancedA2AClient(api_key="test_key")

    # 1. Test Memory
    print("Testing Memory...")
    await client.memory_manager.memorize("User preferences: Likes dark mode and Python.", agent_id="pref_agent")
    
    recalled = await client.memory_manager.recall("preferences")
    print(f"Recalled Memory: '{recalled}'")
    assert "dark mode" in recalled, f"Memory recall failed. Expected 'dark mode' in '{recalled}'"

    # 2. Test Router
    print("\nTesting Model Router...")
    
    fast_model = client.model_router.route("Hello, how are you?")
    print(f"Simple prompt route: {fast_model}")
    assert "flash" in fast_model, f"Fast route failed. Expected 'flash' in '{fast_model}'"

    coding_model = client.model_router.route("Write a python script to sort a list.")
    print(f"Coding prompt route: {coding_model}")
    assert "sonnet" in coding_model, f"Coding route failed. Expected 'sonnet' in '{coding_model}'"

    complex_model = client.model_router.route("Execute a deep analysis of the following 1000 line log file...")
    print(f"Complex prompt route: {complex_model}")
    assert "pro" in complex_model, f"Complex route failed. Expected 'pro' in '{complex_model}'"

    print("\nPhase 4 Verification Successful!")

if __name__ == "__main__":
    asyncio.run(test_intelligence())
