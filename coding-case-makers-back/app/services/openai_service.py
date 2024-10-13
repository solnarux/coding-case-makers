# app/services/openai_service.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIService:
    @staticmethod
    def generate_response(prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change the model as needed
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']