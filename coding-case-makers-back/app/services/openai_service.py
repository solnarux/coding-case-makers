import os
from typing import List

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
PROJECT_ID = os.getenv("PROJECT_ID")


class OpenAIService:
    client = OpenAI(
        organization=ORGANIZATION_ID,
        api_key=OPENAI_API_KEY,
        project=PROJECT_ID
    )

    @staticmethod
    def generate_response(prompt: str) -> str:
        response = OpenAIService.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    @staticmethod
    def embed_text(text: str) -> list[float]:
        response = OpenAIService.client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
