import asyncio

from mcp_agent.core.fastagent import FastAgent  # type: ignore
from mcp_agent.core.request_params import RequestParams  # type: ignore

# Create the application
fast = FastAgent("FastAgent Client Example")


# Define the agent
@fast.agent(
    name="demo-client",
    instruction="You are a helpful AI assistant.",
    servers=["demo-server"],
    # To change to another ollama hosted model change to generic.modelname
    model="generic.llama3.1:8b",
    request_params=RequestParams(
        parallel_tool_calls=False,
        temperature=0.0,
        maxTokens=128000,
        systemPrompt="You are a helpful AI assistant that answers questions. You must formulate answers based on presented data.",
    ),
    human_input=True,
)
async def main():
    async with fast.run() as agent:
        await agent()


if __name__ == "__main__":
    asyncio.run(main())
