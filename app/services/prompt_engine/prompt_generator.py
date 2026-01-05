from app.services.prompt_engine.base import BasePromptGenerator
from app.schemas.prompt import PromptRequest
from app.services.llm.groq_client import GroqClient

class PromptGenerator(BasePromptGenerator):

    def __init__(self):
        self.llm = GroqClient()

    def _format_constraints(self, constraints: list[str]) -> str:
        if not constraints:
            return "No specific constraints."
        return "\n".join([f"- {c}" for c in constraints])

    async def generate(self, data: PromptRequest) -> str:
        system_prompt = """
You are an expert AI prompt engineer specializing in crafting high-performance prompts for various AI platforms.

Your expertise includes:
- Deep understanding of prompt engineering principles (role assignment, chain-of-thought, few-shot learning, structured outputs)
- Platform-specific optimization (ChatGPT, Claude, Gemini, Midjourney, Stable Diffusion, etc.)
- Balancing clarity, specificity, and token efficiency
- Incorporating constraints and guardrails effectively

OUTPUT STRUCTURE:
You must provide your response in the following structured format:

GENERATED PROMPT:
[The complete, ready-to-use prompt that the user can copy and paste]

PROMPT BREAKDOWN:
Role Assignment: [Explain the role/persona assigned]
Core Instructions: [Key directives and objectives]
Reasoning Approach: [How thinking/reasoning is structured]
Output Format: [Expected response structure]

OPTIMIZATION NOTES:
Platform-Specific: [Why this works well for the target platform]
Key Techniques Used: [List 2-3 prompt engineering techniques applied]
Potential Improvements: [Optional suggestions for iteration]

USAGE TIPS:
[1-2 practical tips for getting the best results with this prompt]
"""

        user_prompt = f"""
Generate an optimized prompt with the following specifications:

TARGET PLATFORM: {data.platform}

OBJECTIVE:
{data.goal}

DESIRED TONE: {data.tone}

COMPLEXITY LEVEL: {data.complexity}
(This should guide how technical/detailed the prompt instructions are)

PROMPT TYPE: {data.prompt_type}
(e.g., conversational, task-based, creative generation, analytical, code generation)

CONSTRAINTS:
{self._format_constraints(data.constraints)}

SPECIAL REQUIREMENTS:
- The prompt should be immediately usable without modification
- Include explicit instructions for step-by-step reasoning when appropriate
- Optimize for {data.platform}'s specific capabilities and token limits
- Balance thoroughness with conciseness
- If relevant, include output formatting instructions (JSON, markdown, etc.)

Generate the structured prompt now.
"""
        return await self.llm.generate(system_prompt, user_prompt)
