from pydantic import BaseModel
from typing import Optional


class UserSignupRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class UserSignInRequest(BaseModel):
    email: str
    password: str