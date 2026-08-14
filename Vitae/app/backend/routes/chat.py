from fastapi import FastAPI, routing, APIRouter, Depends
from pathlib import Path
from Vitae.app.backend.schemas.chat import ChatMessage, ChatRequest
from Vitae.app.externalservices.openai.openai_api import (
    send_message,
    OpenAIIntegrationError,
)
import aiofiles

curent_dir = Path(__file__).resolve()
prompt_file_path = curent_dir.parents[2] / "core" / "prompt.txt"

router = APIRouter()


@router.post("/chatsend", response_model=ChatMessage)
async def chatsend(chat_request: ChatRequest):
    async with aiofiles.open(prompt_file_path, mode="r", encoding="utf-8") as f:
        system_prompt = await f.read()
    messages = [{"role": "system", "content": system_prompt}]
    for message in chat_request.messages:
        messages.append({"role": message.role, "content": message.content})
    try:
        bot_reply = await send_message(messages)
        return ChatMessage(role="assistant", content=bot_reply)
    except OpenAIIntegrationError:
        reply = (
            "My connection to the OpenAI servers is currently unstable. 😅"
            " But don't worry! You can always reach out to Volodymyr directly via email at"
            " Vova.Spetcialny@gmail.com."
        )
        return ChatMessage(
            role="assistant",
            content=reply,
        )
