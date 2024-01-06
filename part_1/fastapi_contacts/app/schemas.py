# fastapi_contacts/app/schemas.py

from pydantic import BaseModel, Field

class OAuth2PasswordRequestForm(BaseModel):
    username: str = Field(..., alias="email")
    password: str
    scope: str = ""
    client_id: str = ""
    client_secret: str = ""
    grant_type: str = "password"

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool

class Contact(BaseModel):
    name: str
    email: str
    password: str  # Adjust the data type if necessary

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):  # Add this class
    id: int
    email: str
    is_active: bool

