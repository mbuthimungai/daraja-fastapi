from fastapi import APIRouter, Request

callback_router = APIRouter()

@callback_router.post("/")
async def callback(request: Request):
    data = await request.json()
    print(data)
    return