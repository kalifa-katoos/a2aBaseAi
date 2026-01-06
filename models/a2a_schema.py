from typing import List, Optional, Union, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime
import uuid

# --- A2A Basic Units ---

class TextPart(BaseModel):
    type: str = "text"
    text: str

class FilePart(BaseModel):
    type: str = "file"
    file_id: str
    filename: str
    mime_type: str

class DataPart(BaseModel):
    type: str = "data"
    data: Dict[str, Any]

Part = Union[TextPart, FilePart, DataPart]

class Message(BaseModel):
    role: str # "user", "agent", "system"
    parts: List[Part]
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class Artifact(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    parts: List[Part]
    created_at: datetime = Field(default_factory=datetime.utcnow)

# --- AgentCard for Discovery ---

class AgentSkill(BaseModel):
    name: str
    description: str
    parameters_schema: Dict[str, Any]

class AgentCard(BaseModel):
    agent_id: str
    name: str
    description: str
    skills: List[AgentSkill]
    endpoint_url: str
    auth_type: str = "none" # "none", "bearer", "api_key"

# --- Task Lifecycle ---

class Task(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    session_id: str
    status: str = "submitted" # "submitted", "working", "completed", "failed"
    history: List[Message] = []
    artifacts: List[Artifact] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

# --- JSON-RPC 2.0 Wrapper ---

class A2ARequest(BaseModel):
    jsonrpc: str = "2.0"
    method: str
    params: Dict[str, Any]
    id: Union[str, int]

class A2AResponse(BaseModel):
    jsonrpc: str = "2.0"
    result: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None
    id: Union[str, int]
