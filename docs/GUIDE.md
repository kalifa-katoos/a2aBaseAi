# A2ABase Clone - Documentation

Welcome to the A2ABase Clone documentation. This platform allows you to build, manage, and deploy coordinated AI agents.

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- Node.js 18+
- Docker & Docker Compose

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/your-repo/a2abase-clone.git
cd a2abase-clone

# Setup Python environment
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Setup Dashboard
cd dashboard
npm install
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
A2ABASE_API_KEY=your_key
GEMINI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
```

## 🧠 Core Concepts

### Agents
Agents are defined using the `Agent` class. They have instructions, a model, and a set of tools.

### Tools
Tools can be **Native** (Python functions) or **MCP** (Model Context Protocol) integrations.

### Memory
Agents use a `MemoryManager` to store and recall information across sessions.

## 🛠️ Usage Examples

### Creating a simple agent
```python
from client import EnhancedA2AClient
from models.a2a_schema import AgentCard

client = EnhancedA2AClient(api_key="your_key")
# ... register tools and create agent card
```

## 🚢 Deployment
We provide a production-ready `docker-compose.yml` in the `infrastructure` directory.
