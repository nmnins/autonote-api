from fastapi import Request, HTTPException, status
import os
from dotenv import load_dotenv

load_dotenv()  

API_KEY = os.getenv("API_KEY")

def verify_api_key(request: Request):
    header_key = request.headers.get("x-api-key")
    if header_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Clé API invalide",
        )
