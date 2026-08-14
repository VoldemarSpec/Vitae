from pydantic import BaseModel, Field, model_validator
from typing import List


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(..., max_length=20, description="Chat history")


@model_validator(mode="after")
def check_user_messages(self):
    for msg in self.messages:
        if msg.role == "user" and len(msg.content) > 500:
            raise ValueError("User message exceeds maximum length of 500 characters.")
    return self
