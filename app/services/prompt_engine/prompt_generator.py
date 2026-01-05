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
        # Specialized instructions based on prompt type
        type_specific_instructions = ""
        if data.prompt_type == "Code Generation":
            type_specific_instructions = """
            - For code generation, strictly enforce modularity, error handling, and comments.
            - Request valid, compilable/runnable code snippets.
            - Include security considerations (e.g., input validation).
            """
        elif data.prompt_type == "Creative Writing":
            type_specific_instructions = """
            - Encourage "Show, Don't Tell" principles.
            - Focus on sensory details, emotional resonance, and varied sentence structure.
            - Allow for higher temperature/creativity constraints in the prompt instructions.
            """
        elif data.prompt_type == "Data Analysis":
            type_specific_instructions = """
            - Demand data-backed reasoning.
            - Use structured frameworks (e.g., SWOT, First Principles, root cause analysis).
            - Request unbiased, objective evaluation of options.
            """

        system_prompt = f"""
You are an Elite Senior Prompt Architect with deep expertise in LLM cognitive architectures. Your task is to engineer a "Production-Grade" prompt that extracts the absolute maximum performance from {data.platform} for a specific user goal.

### CORE PHILOSOPHY
- **Precision over Ambiguity**: Vague prompts yield vague results. You construct prompts with laser-focused clarity.
- **Structural Integrity**: You use delimiters (###, ---, brackets) to separate context, instructions, and data.
- **Cognitive Scaffolding**: You embed Chain-of-Thought (CoT) and "Take a deep breath" style reasoning instructions to improve logic.
- **Persona Engineering**: You define rich, expert personas suited exactly to the task.

### EXPERT TECHNIQUES TO EMPLOY
1. **Persona Pattern**: Define a specific role (e.g., "World-class Python Systems Engineer" instead of "Coder").
2. **Chain-of-Thought**: Instruct the model to "Think step-by-step" before answering.
3. **Output Constraining**: Clearly define the output format (JSON, Markdown, CSV, etc.) with examples if needed.
4. **Few-Shot Prompting**: If the user provides examples, format them rigorously. If not, structure the prompt to accept them easily.

### OUTPUT FORMAT
You must output a response in this EXACT structure:

GENERATED PROMPT:
[The complete, high-fidelity prompt. This should be ready to copy-paste. It must include:
    - Role/System Context
    - Main Task Description
    - Step-by-Step Instructions
    - Constraints & Guardrails
    - Output Format Specification
]

PROMPT BREAKDOWN:
[Bullet points explaining WHY you structured it this way]
- **Persona**: Why this specific role?
- **Cognitive Strategy**: What reasoning method is used?
- **Key Constraints**: How you prevent hallucinations or bad output.

OPTIMIZATION FOR {data.platform.upper()}:
- [Specific advice for this model, e.g., "Claude prefers XML tags", "GPT-4 likes explicit step-by-step"]
"""

        user_prompt = f"""
### SPECIFICATIONS FOR THE NEW PROMPT

**Target Platform**: {data.platform}
**User Goal**: {data.goal}
**Desired Tone**: {data.tone}
**Complexity**: {data.complexity}
**Prompt Type**: {data.prompt_type}

### CONSTRAINTS PROVIDED
{self._format_constraints(data.constraints)}

### ADDITIONAL REQUIREMENTS
{type_specific_instructions}

### TASK
Draft the ultimate prompt for this request. It should be sophisticated, robust, and designed to minimize errors.
Ensure the "GENERATED PROMPT" section is self-contained and uses delimiters for clarity.
"""
        return await self.llm.generate(system_prompt, user_prompt)
