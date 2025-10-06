
# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User schemas (DB1)
class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

# Note schemas (DB2)
class NoteCreate(BaseModel):
    user_id: int
    title: str
    content: Optional[str] = None

class NoteRead(BaseModel):
    id: int
    user_id: int
    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
