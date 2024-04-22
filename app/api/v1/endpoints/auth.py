import aiohttp
import os
import base64


CONSUMER_KEY = os.getenv('CONSUMER_KEY')

CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')

URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

auth_string = f"{CONSUMER_KEY}:{CONSUMER_SECRET}".encode('utf-8')
encoded_auth_string = base64.b64encode(auth_string).decode('utf-8')
authorization_header = f"Basic {encoded_auth_string}"

headers = { 
           
    'Authorization': f'{authorization_header}'
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