# app/main.py

from fastapi import FastAPI

from app.routes import chatbot_routes, product_routes

app = FastAPI()

#app.include_router(user_routes.router)
app.include_router(product_routes.router)
app.include_router(chatbot_routes.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Chatbot!!!"}
