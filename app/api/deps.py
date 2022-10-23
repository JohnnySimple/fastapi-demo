from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlmodel import Session, select

from app.core import security
from app.core.config import settings
from app.models.schemas.token import TokenPayload
from app.db.db import engine
from app.resources import strings

from app.models.schemas.user import Users


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/oauth/token"
)

def get_current_user(token: str = Depends(reusable_oauth2)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )

        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    
    with Session(engine) as session:
        statement = select(Users).where(Users.id == token_data.sub)
        user = session.exec(statement).first()
    
    if not user:
        raise HTTPException(status_code=400, detail=strings.USER_NOT_FOUND)

    return user
