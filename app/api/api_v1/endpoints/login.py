from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/oauth/token")
async def access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
        get access token for requests
    """

    return "access token"
    