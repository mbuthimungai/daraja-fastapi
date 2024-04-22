import aiohttp
import os
import base64


CONSUMER_KEY = os.getenv('CONSUMER_KEY')

CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')

URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

headers = { 
    'Authorization': f'Bearer {base64.encode(f"{CONSUMER_KEY}:{CONSUMER_SECRET}")}'
}


async def authorize():
    async with aiohttp.ClientSession() as async_session:
        try:
            async with async_session.get(url=URL, headers=headers) as response:
                response.raise_for_status()  
                return await response.json() 
        except aiohttp.ClientError as e:
            print(f"HTTP request failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")