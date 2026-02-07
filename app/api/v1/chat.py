from fastapi import APIRouter, Depends, HTTPException
from app.schemas.chat import ChatRequest
from app.api.deps import get_current_user
from app.services.rag_client import ask_rag

router = APIRouter()

@router.post("/")
async def chat_ai(payload: ChatRequest, user=Depends(get_current_user)):
    response = await ask_rag(
        question=payload.message,
        division_id=user.division_id,
        role=user.role
    )
    return response
