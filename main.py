from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class InputData(BaseModel):
    data: List[str]

def process_data(data):
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_alphabet = [max(alphabets, key=lambda x: x.lower())] if alphabets else []

    return numbers, alphabets, highest_alphabet

@app.post("/bfhl")
async def process_request(request_data: InputData):
    numbers, alphabets, highest_alphabet = process_data(request_data.data)

    response = {
        "is_success": True,
        "user_id": "saheb_ansari_27072005",
        "email": "2237451.it.cec@cgc.edu.in",
        "roll_number": "2237451",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }
    return response

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}

