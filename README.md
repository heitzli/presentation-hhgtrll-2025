# MCP Demo Server and Client

## Prerequisites

The following tools need to be installed to run the demo:
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [ollama](https://ollama.com/download)
- [llama3.1:8b](https://ollama.com/library/llama3.1:8b) installed via ollama

## Setup

1. Download / start the model with:
   
   ```bash
   ollama run llama3.1:8b
   ```

2. Start the MCP-Server:

   ```bash
   cd demo-mcp-server
   uv run mcpserver.py 
   ```

3. Start the Client:

   ```bash
   cd demo-client
   uv run agent.py
   ```