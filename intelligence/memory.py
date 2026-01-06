from typing import List, Dict, Any, Optional
import json
import os

class MemoryEntry:
    def __init__(self, content: str, metadata: Dict[str, Any] = None):
        self.content = content
        self.metadata = metadata or {}

class BaseMemory:
    async def add(self, content: str, metadata: Dict[str, Any] = None):
        raise NotImplementedError

    async def search(self, query: str, limit: int = 5) -> List[MemoryEntry]:
        raise NotImplementedError

class LocalMemory(BaseMemory):
    """A simple local memory that stores data in a JSON file."""
    def __init__(self, storage_path: str = "memory.json"):
        self.storage_path = storage_path
        self.data: List[Dict[str, Any]] = []
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r") as f:
                self.data = json.load(f)

    async def add(self, content: str, metadata: Dict[str, Any] = None):
        self.data.append({
            "content": content,
            "metadata": metadata or {}
        })
        with open(self.storage_path, "w") as f:
            json.dump(self.data, f)

    async def search(self, query: str, limit: int = 5) -> List[MemoryEntry]:
        # Simple keyword matching for the fallback
        results = []
        for item in self.data:
            if query.lower() in item["content"].lower():
                results.append(MemoryEntry(item["content"], item["metadata"]))
        return results[:limit]

class MemoryManager:
    def __init__(self, mode: str = "local"):
        if mode == "local":
            self.store = LocalMemory()
        else:
            # Placeholder for VectorMemory (pgvector)
            self.store = LocalMemory() 

    async def memorize(self, content: str, agent_id: str):
        await self.store.add(content, {"agent_id": agent_id})

    async def recall(self, query: str) -> str:
        entries = await self.store.search(query)
        if not entries:
            return ""
        return "\n".join([e.content for e in entries])
