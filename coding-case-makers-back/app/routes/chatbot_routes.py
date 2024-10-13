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
    """Answer the question using a lot of data and a modified prompt. It is slower."""
    try:
        answer = service.get_computer_info(chat_request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/chatbot-rag")
async def chatbot_rag(chat_request: ChatRequest, service: ChatbotService = Depends(get_chatbot_service)):
    """Answer the question using the top 5 data, with a RAG and embeddings which makes it faster"""
    try:
        answer = service.get_computer_info_RAG(chat_request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))