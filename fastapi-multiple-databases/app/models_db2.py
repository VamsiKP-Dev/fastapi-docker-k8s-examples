
# app/models_db2.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import BaseDB2

class Note(BaseDB2):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)  # logical reference to user.id in DB1
    title = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
