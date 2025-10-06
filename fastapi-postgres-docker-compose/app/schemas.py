
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NoteBase(BaseModel):
    title: str
    content: Optional[str] = None

class NoteCreate(NoteBase):
    pass

class NoteRead(NoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
