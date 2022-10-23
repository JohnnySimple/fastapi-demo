from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.crud.crud_user import authenticate
from app.core import security
from app.core.config import settings

# from app.models.schemas.user import UserResponse
# from app.models.schemas.login import LoginResponse

router = APIRouter()

@router.post("/oauth/token")
async def access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
        get access token for requests
    """

    user = authenticate(
        email=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or passowrd")
    
    if user.status == "inactive":
        raise HTTPException(status_code=403, detail="User is not active")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        "token": {
            "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
            ),
            "token_type": "bearer"
        },
        "response": user
    }

    