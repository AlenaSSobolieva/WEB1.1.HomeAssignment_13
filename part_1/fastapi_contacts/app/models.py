# fastapi_contacts/app/models.py

from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)  # Default to False for email verification
    access_token = Column(String, nullable=True)
    refresh_token = Column(String, nullable=True)
    email_verified = Column(Boolean, default=False)  # New field for email verification status

class UserCreate:
    email: str
    password: str
