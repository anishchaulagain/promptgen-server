from app.services.prompt_engine.base import BasePromptGenerator
from app.schemas.prompt import PromptRequest
from app.services.llm.groq_client import GroqClient

class PromptGenerator(BasePromptGenerator):

    def __init__(self):
        self.llm = GroqClient()

    async def generate(self, data: PromptRequest) -> str:
        system_prompt = """
You are a world-class AI prompt engineer.
Your job is to generate highly advanced, optimized prompts.
"""

        user_prompt = f"""
Create an ADVANCED prompt for {data.platform}

GOAL:
{data.goal}

TONE:
{data.tone}

COMPLEXITY:
{data.complexity}

PROMPT TYPE:
{data.prompt_type}

CONSTRAINTS:
{', '.join(data.constraints) if data.constraints else 'None'}

RULES:
- The prompt must be extremely clear and structured
- Use role assignment
- Use step-by-step reasoning instructions
- Optimize for best {data.platform} performance
"""

        return await self.llm.generate(system_prompt, user_prompt)
