from fastapi import APIRouter
from app.api.v1.prompt import router as prompt_router

api_router = APIRouter()

api_router.include_router(
    prompt_router,
    prefix="/prompt",
    tags=["Prompt Generator"]
)