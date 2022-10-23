from sqlmodel import SQLModel, Field

from app.models.schemas.rwschema import RWSchema

class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    password: str
    clearance_level: str
    status: str
    type: str