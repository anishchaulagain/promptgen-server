
from app.services.prompt_engine.base import BasePromptGenerator
from app.schemas.prompt import PromptRequest
from app.services.llm.groq_client import GroqClient

class ClaudePromptGenerator(BasePromptGenerator):
    def __init__(self):
        self.llm = GroqClient()

    async def generate(self, data: PromptRequest) -> str:
        system_prompt = """
You are a world-class AI prompt engineer.
Your job is to generate highly advanced, optimized prompts.
"""

        user_prompt = f""" Create an ADVANCED prompt for Claude.

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
- Optimize for best Claude performance
"""

        return await self.llm.generate(system_prompt, user_prompt)









# from app.services.prompt_engine.base import BasePromptGenerator
# from app.schemas.prompt import PromptRequest
# from app.services.llm.groq_client import GroqClient

# class ChatGPTPromptGenerator(BasePromptGenerator):

#     def __init__(self):
#         self.llm = GroqClient()

#     async def generate(self, data: PromptRequest) -> str:
#         system_prompt = """
# You are a world-class AI prompt engineer.
# Your job is to generate highly advanced, optimized prompts.
# """

#         user_prompt = f"""
# Create an ADVANCED prompt for ChatGPT.

# GOAL:
# {data.goal}

# TONE:
# {data.tone}

# COMPLEXITY:
# {data.complexity}

# CONSTRAINTS:
# {', '.join(data.constraints) if data.constraints else 'None'}

# RULES:
# - The prompt must be extremely clear and structured
# - Use role assignment
# - Use step-by-step reasoning instructions
# - Optimize for best ChatGPT performance
# """

#         return await self.llm.generate(system_prompt, user_prompt)
