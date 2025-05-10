from fastapi import Request, HTTPException, status
import os
from dotenv import load_dotenv

load_dotenv()


def verify_api_key(request: Request):
    expected_api_key = os.getenv("API_KEY")
    provided_api_key = request.headers.get("x-api-key")
    if not expected_api_key:
        raise RuntimeError("API_KEY non défini dans l'environnement")
    if not provided_api_key or provided_api_key != expected_api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Clé API invalide ou absente.",
        )
