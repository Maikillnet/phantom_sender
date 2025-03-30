from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(mongo_url)
db = client.phantom_sender
collection = db.sent_logs

async def was_sent(chat_id):
    return await collection.find_one({"chat_id": chat_id}) is not None

async def log_sent(chat_id):
    await collection.insert_one({"chat_id": chat_id})
