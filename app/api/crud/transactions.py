
async def save_transaction(collection, transaction_data: dict) -> None:
    
    try:
        result = await collection.insert_one(transaction_data)
        print(f"Transaction inserted with id: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred: {e}")