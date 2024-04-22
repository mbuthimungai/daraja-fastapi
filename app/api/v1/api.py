from fastapi import APIRouter


from app.api.v1.endpoints.stk_push import stk_router
from app.api.v1.endpoints.callback import callback_router


api_router = APIRouter()

api_router.include_router(stk_router, prefix="/stkpush", tags=["STK Push"])
api_router.include_router(callback_router, prefix="/callback", tags=["Callback"])