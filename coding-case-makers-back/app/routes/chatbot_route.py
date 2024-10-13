# app/routes/chatbot_routes.py

from fastapi import APIRouter, HTTPException
from app.services.chatbot_service import ChatbotService

router = APIRouter()

@router.post("/chatbot")
async def chatbot(question: str):
    try:
        answer = ChatbotService.get_computer_info(question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))