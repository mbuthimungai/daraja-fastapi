from fastapi import FastAPI
from app.app import app_router

from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="STK push Daraja API")

app.include_router(app_router)