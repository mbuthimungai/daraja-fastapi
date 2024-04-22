from fastapi import APIRouter

# from api.v1.api import api_router
from app.api.v1.api import api_router

app_router = APIRouter()

app_router.include_router(api_router, prefix="/v1")
