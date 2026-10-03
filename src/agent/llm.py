import time
from ollama import chat


class LocalLLM:

    def __init__(self, model="qwen3:4b"):
        self.model = model

    def ask(self, command: str) -> str:

        start = time.time()

        prompt = f"""
You are Le-Fantome, a local computer agent running on macOS.

Convert the user's request into an action when possible.

User request:
{command}

Available tool:

open_application
- Opens a macOS application.
- Argument: app_name

If the user wants to open an application, respond ONLY with:

{{
    "tool": "open_application",
    "arguments": {{
        "app_name": "Google Chrome"
    }}
}}

If the request does not require a tool, respond normally.

Do not use markdown.
Do not explain JSON.
"""

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0,
                "num_ctx": 2048
            }
        )

        elapsed = time.time() - start

        print(f"[LLM took {elapsed:.2f}s]")

        return response.message.content.strip()