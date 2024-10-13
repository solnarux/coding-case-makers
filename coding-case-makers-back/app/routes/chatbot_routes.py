from fastapi import APIRouter, HTTPException, Depends
from app.services.chatbot_service import ChatbotService
from app.models.chatbot import ChatRequest
from app.dependencies import get_computer_service
from app.services.computer_service import ComputerService

router = APIRouter()


def get_chatbot_service(computer_service: ComputerService = Depends(get_computer_service)) -> ChatbotService:
    return ChatbotService(computer_service)


@router.post("/chatbot")
async def chatbot(chat_request: ChatRequest, service: ChatbotService = Depends(get_chatbot_service)):
    try:
        answer = service.get_computer_info(chat_request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
