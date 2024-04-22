from fastapi import APIRouter, Request, HTTPException

from app.api.crud.transactions import save_transaction
from app.api.schemas.transactions import StkCallback, CallbackRequest
from app.api.deps import transactions as transactions_collection
callback_router = APIRouter()

@callback_router.post("/")
async def callback(request: CallbackRequest):
    try:
        stk_callback = request.Body.get("stkCallback", {})
        transaction = {
            "MerchantRequestID": stk_callback.get("MerchantRequestID"),
            "CheckoutRequestID": stk_callback.get("CheckoutRequestID"),
            "ResultCode": stk_callback.get("ResultCode"),
            "ResultDesc": stk_callback.get("ResultDesc"),
            "Amount": stk_callback.get("CallbackMetadata", {}).get("Item", [{}])[0].get("Value"),
            "MpesaReceiptNumber": stk_callback.get("CallbackMetadata", {}).get("Item", [{}])[1].get("Value"),
            "Balance": stk_callback.get("CallbackMetadata", {}).get("Item", [{}])[2].get("Value"),
            "TransactionDate": stk_callback.get("CallbackMetadata", {}).get("Item", [{}])[3].get("Value"),
            "PhoneNumber": stk_callback.get("CallbackMetadata", {}).get("Item", [{}])[4].get("Value"),
        }
        
        await save_transaction(transactions_collection, transaction)
        return {"message": "Transaction saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Callback error: {str(e)}")
