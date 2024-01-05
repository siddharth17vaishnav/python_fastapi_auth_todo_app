from pydantic import BaseModel, Field
from typing import Optional, Generic


class UserSignupRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    class Config:
        from_attributes = True


class UserSignInRequest(BaseModel):
    email: str
    password: str