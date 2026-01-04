from fastapi import FastAPI
from app.api.v1.router import api_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Prompt Generator",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",   
        "http://localhost:5173",  
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")