import os
from openai import OpenAI
from abc import ABC, abstractmethod


class LLMClient(ABC):
    @abstractmethod
    def predict(self, input: str, instructions: str) -> dict:
        pass


class OpenAIClient(LLMClient):
    def __init__(self, model: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.model = model

    def predict(self, input: str, instructions: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            instructions=instructions,
            input=input
        )
        return response.output_text
