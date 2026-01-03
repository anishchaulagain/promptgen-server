from fastapi import APIRouter, HTTPException
from app.schemas.prompt import PromptRequest, PromptResponse
from app.services.prompt_engine.chatgpt import ChatGPTPromptGenerator
from app.services.prompt_engine.claude import ClaudePromptGenerator

router = APIRouter()

@router.post("/generate", response_model=PromptResponse)
async def generate_prompt(payload: PromptRequest):

    match payload.platform.lower():
        case "chatgpt":
            generator = ChatGPTPromptGenerator()
            prompt = await generator.generate(payload)
        case "claude":
            generator = ClaudePromptGenerator()
            prompt = await generator.generate(payload)
        case _:
            raise HTTPException(
                status_code=400,
                detail="Platform not supported yet"
            )

    return PromptResponse(
        platform=payload.platform,
        prompt=prompt
    )
