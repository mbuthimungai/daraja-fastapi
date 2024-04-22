from pydantic import BaseModel

class StkCallback(BaseModel):
    MerchantRequestID: str
    CheckoutRequestID: str
    ResultCode: str
    ResultDesc: str
    Amount: str
    MpesaReceiptNumber: str
    Balance: str
    TransactionDate: str
    PhoneNumber: str

class CallbackRequest(BaseModel):
    Body: dict
