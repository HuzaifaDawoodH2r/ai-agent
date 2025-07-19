
import os
from dotenv import load_dotenv
from agent.agent import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
import asyncio
from openai import AsyncOpenAI

load_dotenv()

set_tracing_disabled(disabled=True)


client=AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL"),
 
)

agent = Agent(
    name="assistant",
    instructions="You are a helpful assistant.",
    model=OpenAIChatCompletionsModel(
        model=os.getenv("MODEL"),
        openai_client=client
    ),
)


async def main():
    runner = Runner(agent)
    user_input = input("User: ")
    result = await runner.run(user_input)
    print(result.final_output)

asyncio.run(main())
