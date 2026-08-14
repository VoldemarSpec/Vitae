from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from Vitae.app.backend.routes import chat
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/v1/chat", tags=["chat"])


@app.get("/")
async def root():
    return {"message": "backend is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
