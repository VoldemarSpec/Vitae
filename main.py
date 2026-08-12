from fastapi import FastAPI
import uvicorn
from Vitae.app.backend.routes import chat

app = FastAPI()

app.include_router(chat.router, prefix="/api/v1/chat", tags=["chat"])


@app.get("/")
async def root():
    return {"message": "backend is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
