FROM python:3.11-slim

# Install basic tools
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install standard agent libraries
RUN pip install pandas requests beautifulsoup4 playwright

# Set up a non-root user for security
RUN useradd -m agentuser
USER agentuser

CMD ["python3"]
