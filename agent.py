# agents.py

class OpenAIChatCompletionsModel:
    def __init__(self, model, openai_client):
        self.model = model
        self.client = openai_client

    async def complete(self, messages):
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return response.choices[0].message.content


class Agent:
    def __init__(self, name, instructions, model):
        self.name = name
        self.instructions = instructions
        self.model = model

    async def respond(self, prompt):
        messages = [
            {"role": "system", "content": self.instructions},
            {"role": "user", "content": prompt}
        ]
        return await self.model.complete(messages)


class Runner:
    def __init__(self, agent):
        self.agent = agent

    async def run(self, prompt):
        output = await self.agent.respond(prompt)
        return type("Result", (object,), {"final_output": output})()


def set_tracing_disabled(disabled: bool):
    # For now you can just pass; this is placeholder
    pass
