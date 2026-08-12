import os
import asyncio
from openai import DefaultAioHttpClient
from openai import AsyncOpenAI
from dotenv import load_dotenv
load_dotenv() 

async def send_message(messages:list) -> str:
    async with AsyncOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),  
        http_client=DefaultAioHttpClient(),
    ) as client:
        chat_completion = await client.chat.completions.create(
            messages = messages,
            model="gpt-4o-mini",
            temperature=0.7
        )
        bot_reply = chat_completion.choices[0].message.content
        return bot_reply

