from fastapi import APIRouter, Body, Depends, Response,HTTPException,status
from sqlalchemy.orm import Session

from typing import Annotated

import db.user as user
from config import SessionLocal
from schemas.user import UserSignupRequest,UserSignInRequest
from utils.encryption import verify_password

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create_user(body: Annotated[UserSignupRequest, Body(emed=True)], response: Response,
                      db: Session = Depends(get_db)):
    user_exist = user.get_user_by_email(db,body.email)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already registered")
    else:
        try:
            user.create_user(db,body)
            return {"detail":"success"}
        except ValueError as err:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(err))

@router.get('/get')
async def get_users(db: Session = Depends(get_db)):
    _user = user.get_user(db)
    return {"user": _user}

@router.post('/login')
async def login(body:Annotated[UserSignInRequest,Body(emed =True)],db:Session=Depends(get_db)):
    _user = user.get_user_by_email(db,body.email)
    if not _user:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="No user found!")
    else:
        try:
            is_password_correct = verify_password(body.password,_user.password)
            if is_password_correct:
                return {"user":{"name":_user.name,"email":_user.email}}
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Incorrect email or password!")
        except ValueError as err:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(err))
