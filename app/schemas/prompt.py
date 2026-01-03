from pydantic import BaseModel
from typing import List, Optional

class PromptRequest(BaseModel):
    platform: str
    goal: str
    tone: Optional[str] = "neutral"
    complexity: Optional[str] = "advanced"
    prompt_type: Optional[str] = "general"
    constraints: Optional[List[str]] = []

class PromptResponse(BaseModel):
    platform: str
    prompt: str