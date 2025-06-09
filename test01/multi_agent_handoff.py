import os
import asyncio
from dotenv import load_dotenv
from pydantic import BaseModel
from agents import (
    Agent,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunConfig,
    handoff,
    Runner
)

# 1. Load .env
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# 2. Validate API key
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please define it in your .env file.")

# 3. Create OpenAI-compatible Gemini client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 4. Create the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# 5. Create run config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# 6. Define individual agents
football_agent = Agent(
    name="Football Agent",
    instructions="You are a football expert. Answer only football-related questions."
)

cricket_agent = Agent(
    name="Cricket Agent",
    instructions="You are a cricket expert. Answer only cricket-related questions."
)

hockey_agent = Agent(
    name="Hockey Agent",
    instructions="You are a hockey expert. Answer only hockey-related questions."
)

# 7. Define the triage agent that hands off based on topic
triage_agent = Agent(
    name="Triage Agent",
    instructions="""
    You are a triage agent. Route the input to the correct agent:
    - If the question is about football, handoff to Football Agent.
    - If the question is about cricket, handoff to Cricket Agent.
    - If the question is about hockey, handoff to Hockey Agent.
    Do not answer the question yourself.
    """,
    handoffs=[football_agent, cricket_agent, hockey_agent],
)

# 8. Async main function to run the agents
async def main():
    user_input = input("Ask a question about football, cricket, or hockey:\n> ")
    result = await Runner.run(triage_agent, input=user_input, run_config=config)
    print(f"\n🤖 Response:\n{result.final_output}")

# 9. Run the async main function in VS Code
if __name__ == "__main__":
    asyncio.run(main())
