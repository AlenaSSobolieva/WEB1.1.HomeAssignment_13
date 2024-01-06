# fastapi_contacts/app/crud.py

from sqlalchemy.orm import Session
from fastapi_contacts.app.models import User  # Import the User model
from fastapi_contacts.app import models
from passlib.context import CryptContext
from fastapi_contacts.app.security import get_password_hash


crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: models.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_contact(db: Session, contact: models.Contact):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contact_by_email(db: Session, email: str):
    return db.query(models.Contact).filter(models.Contact.email == email).first()