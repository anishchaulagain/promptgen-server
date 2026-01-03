from groq import Groq
from app.services.llm.base import BaseLLMClient
from app.core.config import settings

class GroqClient(BaseLLMClient):

    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)

    async def generate(self, system_prompt: str, user_prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model=settings.GROQ_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.4,
        )

        return completion.choices[0].message.content
