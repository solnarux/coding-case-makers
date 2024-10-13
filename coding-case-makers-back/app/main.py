# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chatbot_routes, computer_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"],  
)

#app.include_router(user_routes.router)
app.include_router(computer_routes.router)
app.include_router(chatbot_routes.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Chatbot!!!"}
