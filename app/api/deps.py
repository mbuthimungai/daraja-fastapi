from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.getenv("MONGODB_URL_REMOTE"))

db = client.paymentsDB
transactions = db.transactions

