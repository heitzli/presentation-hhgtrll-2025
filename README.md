# Hitchhiker's Guide To Running LLMs Locally
![title-image](https://github.com/user-attachments/assets/aeaaf95d-c00e-435c-99d8-fd7fbcdaa599)
Generated with: [ChatGPT Image Generator](https://openai.com/index/introducing-4o-image-generation/)


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
