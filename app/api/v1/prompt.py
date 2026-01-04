from fastapi import APIRouter, HTTPException
from app.schemas.prompt import PromptRequest, PromptResponse
from app.services.prompt_engine.prompt_generator import PromptGenerator

router = APIRouter()

@router.post("/generate", response_model=PromptResponse)
async def generate_prompt(payload: PromptRequest):

   generator = PromptGenerator()
   prompt = await generator.generate(payload)

   return PromptResponse(
        platform=payload.platform,
        prompt=prompt
    )
