from fastapi import FastAPI
from app.api.v1 import auth, users, chat

app = FastAPI(title="AI DMS Backend")

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(chat.router, prefix="/api/chat", tags=["Chatbot"])

@app.get("/")
def root():
    return {"status": "ok"}
