from .llm import LocalLLM


class LeFantome:
    def __init__(self):
        self.llm = LocalLLM()

    def process(self, command: str) -> str:
        prompt = f"""
You are Le-Fantome, a local computer assistant.

The user has given you this command:

{command}

For now, do not execute anything.
Simply explain what actions would be required to complete the command.
"""

        return self.llm.ask(prompt)