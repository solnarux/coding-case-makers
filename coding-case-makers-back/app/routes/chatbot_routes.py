# app/routes/chatbot_routes.py

from fastapi import APIRouter, HTTPException
from app.services.chatbot_service import ChatbotService
from app.models.chatbot import ChatRequest

router = APIRouter()

@router.post("/chatbot")
async def chatbot(chat_request: ChatRequest):
    try:
        answer = ChatbotService.get_computer_info(chat_request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

