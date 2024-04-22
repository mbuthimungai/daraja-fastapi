from fastapi import APIRouter, HTTPException
import os
from datetime import datetime
import base64
import aiohttp

from app.api.schemas.stk_push import StkPushReq 
from app.api.v1.endpoints.auth import authorize

stk_router = APIRouter()

PASSKEY = os.getenv('PASSKEY')
BUSINESS_SHORT_CODE = int(os.getenv('BUSINESSSHORTCODE'))

payload = {
    "BusinessShortCode": BUSINESS_SHORT_CODE, 
    "TransactionType": "CustomerPayBillOnline",        
    "PartyB": BUSINESS_SHORT_CODE,
    "CallBackURL": "https://afea-102-217-157-178.ngrok-free.app/v1/callback/",
    "AccountReference": "Company LTD",    
}

URL = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

@stk_router.post("/")
async def perform_stk_push(data: StkPushReq):    
    payload["Amount"] = data.amount
    payload["PartyA"] = data.sender_phone_number
    payload["PhoneNumber"] = data.sender_phone_number
    payload["TransactionDesc"] = data.transaction_desc
    
    now = datetime.now()        
    timestamp = now.strftime('%Y%m%d%H%M%S')
    password_string = str(BUSINESS_SHORT_CODE) + PASSKEY + timestamp

    password_encoded = base64.b64encode(password_string.encode('utf-8')).decode('utf-8')
    
    payload["Password"] = password_encoded   
    payload["Timestamp"] = timestamp
    
    try:
        response = await authorize()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {response['access_token']}"
        }
        async with aiohttp.ClientSession() as async_session:
            async with async_session.post(url=URL, headers=headers, json=payload) as response:
                response.raise_for_status()
                return await response.json()
    except aiohttp.ClientError as e:
        raise HTTPException(status_code=500, detail=f"HTTP request failed: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
