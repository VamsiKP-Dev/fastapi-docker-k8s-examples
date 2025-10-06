
# app/models_db1.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import BaseDB1

class User(BaseDB1):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
