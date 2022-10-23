import hashlib

from sqlmodel import Session, select

from app.db.db import engine
from app.models.schemas.user import Users
from app.core.security import verify_password

def authenticate(email: str, password: str):
    encoded_password = hashlib.md5(password.encode()).hexdigest()

    with Session(engine) as session:
        statement = select(Users).where(Users.email == email)
        user = session.exec(statement).first()
    
    if not user:
        return None
    if user.password != encoded_password:
        return None
    
    return user
