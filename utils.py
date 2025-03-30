import json
import asyncio
import random

def load_chats():
    with open("data/chat_list.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_messages():
    return [
        "Привет! Ищу работу в Москве. Готов к выходу сразу.",
        "Ищу подработку: склад, курьер, погрузка.",
        "Кто знает вакансии без опыта? Пишите в ЛС.",
        "Telegram: @your_username — открыт к предложениям."
    ]

async def sleep_random(min_s, max_s):
    delay = random.randint(min_s, max_s)
    print(f"🕒 Спим {delay} сек...")
    await asyncio.sleep(delay)
