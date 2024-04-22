from fastapi import APIRouter
import os
from datetime import datetime
import base64
import aiohttp

from schemas.stk_push import StkPushReq
from v1.endpoints.auth import authorize

stk_router = APIRouter()

PASSKEY = os.getenv('PASSKEY')
BUSINESS_SHORT_CODE = os.getenv('BUSINESSSHORTCODE')

payload = {
    "BusinessShortCode": BUSINESS_SHORT_CODE, 
    "Timestamp": "20240422093918",
    "TransactionType": "CustomerPayBillOnline",        
    "PartyB": BUSINESS_SHORT_CODE,
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "CompanyXLTD",    
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer p9e5WJv8JrfyZ6B2ZUCnB3fBeywT'
}    

URL = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

@stk_router.post("/", )
async def perform_stk_push(data: StkPushReq):
    payload["Amount"] = data.amount
    payload["PartyA"] = data.sender_phone_number
    payload["PhoneNumber"] = data.sender_phone_number
    payload["TransactionDesc"] = data.transaction_desc
    
    now = datetime.now()        
    timestamp = now.strftime('%Y%m%d%H%M%S')
    
    # Encoding the password
    password_encoded = base64.b64encode(f'{BUSINESS_SHORT_CODE}{PASSKEY}{timestamp}'.encode()).decode('utf-8')
    
    payload["Password"] = password_encoded   
    payload["Timestamp"] = timestamp
    
    response = await authorize()
    headers["Authorization"] = f"Bearer {response['access_token']}"
    
    async with aiohttp.ClientSession() as async_session:
        try:
            async with async_session.post(url=URL, headers=headers, data=payload) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            print(f"HTTP request failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    return
