from pydantic import BaseModel, Field
from typing import List


class ChatMessage(BaseModel):
    role: str
    content: str = Field(..., max_length=500, description="Text content of the message")


class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(..., max_length=20, description="Chat history")
