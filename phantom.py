import asyncio
import random
import json
import os
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.errors import FloodWaitError
from db import log_sent, was_sent
from utils import load_chats, load_messages, sleep_random

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE")

session_path = f"accounts/{phone.replace('+', '')}"
client = TelegramClient(session_path, api_id, api_hash)

async def main():
    await client.start(phone)
    chats = load_chats()
    messages = load_messages()

    for chat in chats:
        if await was_sent(chat):
            print(f"⚠️ Уже отправляли в {chat}")
            continue
        try:
            entity = await client.get_entity(chat)
            msg = random.choice(messages)
            await client.send_message(entity, msg)
            print(f"✅ Отправлено в {chat}")
            await log_sent(chat)
            await sleep_random(15, 60)
        except FloodWaitError as e:
            print(f"🛑 FloodWait: {e.seconds} сек — спим")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"❌ Ошибка для {chat}: {e}")

with client:
    client.loop.run_until_complete(main())
