from ollama import chat


class LocalLLM:
    def __init__(self, model="qwen3:4b"):
        self.model = model

    def ask(self, prompt: str) -> str:
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.message.content