import os
from dotenv import load_dotenv
from a2a_sdk import A2AClient, Agent

# Load environment variables
load_dotenv()

def main():
    # Initialize the A2A Client
    # Note: You need a valid A2ABASE_API_KEY in your .env file
    api_key = os.getenv("A2ABASE_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        print("Error: A2ABASE_API_KEY not found in .env file.")
        return

    client = A2AClient(api_key=api_key)

    # Create a simple agent
    agent = client.agents.create(
        name="HelloAgent",
        instructions="You are a helpful assistant. Greet the user and tell them you are an A2A agent.",
        model="google/gemini-1.5-flash" # Example model
    )

    # Create a thread for conversation
    thread = client.threads.create()

    # Create a run
    run = client.runs.create(
        thread_id=thread.id,
        agent_id=agent.id
    )

    # Wait for the run to complete and print the result
    # This is a simplified example; real implementations should handle polling
    print(f"Agent '{agent.name}' initialized successfully.")
    print(f"Run ID: {run.id}")
    print("Proof of Concept setup complete. Add your API key to .env to run.")

if __name__ == "__main__":
    main()
