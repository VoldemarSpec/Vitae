import os
import asyncio
from openai import DefaultAioHttpClient
from openai import AsyncOpenAI
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)


class OpenAIIntegrationError(Exception):
    pass


async def send_message(messages: list) -> str:
    try:
        async with AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            http_client=DefaultAioHttpClient(),
        ) as client:
            chat_completion = await client.chat.completions.create(
                messages=messages, model="gpt-4o-mini", temperature=0.7
            )
            return chat_completion.choices[0].message.content

    except Exception as e:
        logger.error(f"Failed to connect to OpenAI: {e}")
        raise OpenAIIntegrationError("OpenAI service is unavailable.")
