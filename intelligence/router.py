from typing import List, Optional

class ModelRouter:
    """
    Routes tasks to the most appropriate LLM based on complexity or specific requirements.
    """
    def __init__(self):
        self.models = {
            "fast": "google/gemini-1.5-flash",
            "powerful": "google/gemini-1.5-pro",
            "coding": "anthropic/claude-3.5-sonnet"
        }

    def route(self, prompt: str, task_type: Optional[str] = None) -> str:
        # Simple heuristic-based routing
        if task_type == "code" or any(kw in prompt.lower() for kw in ["code", "python", "script"]):
            return self.models["coding"]
        
        if len(prompt) > 500 or "analy" in prompt.lower():
            return self.models["powerful"]
            
        return self.models["fast"]
