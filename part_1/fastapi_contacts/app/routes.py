# fastapi_contacts/app/routes.py

from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from fastapi_contacts.app import crud, database, schemas, authentication

router = APIRouter()

@router.post("/register", response_model=schemas.UserResponse)
async def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    existing_user = crud.get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already registered with this email")
    created_user = crud.create_user(db=db, user=user)

    response_model = schemas.UserResponse(id=created_user.id, email=created_user.email,
                                          is_active=created_user.is_active)

    return response_model

@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: schemas.OAuth2PasswordRequestForm = Depends()):
    return authentication.create_access_token(data={"sub": form_data.username})

@router.get("/contacts/{email}", response_model=schemas.Contact)
async def read_contact(email: str, db: Session = Depends(database.get_db)):
    contact = crud.get_contact_by_email(db, email=email)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

