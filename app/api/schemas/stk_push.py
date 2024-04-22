from pydantic import BaseModel

class StkPushReq(BaseModel):
    amount: int
    sender_phone_number: int
    transaction_desc: str
    
class StkRes(BaseModel):
    error_code: int
    error_description: str
    