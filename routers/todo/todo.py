from fastapi import APIRouter, Body, Depends, Response,HTTPException,status
from sqlalchemy.orm import Session

from typing import Annotated
from schemas.todo import AddTodoRequest
from config import SessionLocal

import db.todo as todo

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@router.post('/{user_id}/create')
def create_todos(user_id:str,body:Annotated[AddTodoRequest,Body], db: Session = Depends(get_db)):
         if user_id:
             try:
                 todo.create_todo(db,user_id,body)
                 return "success"
             except ValueError as err:
                 raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=str(err))
         else :
             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Session Expired")
         
         
@router.get('/{user_id}')
def get_todos(user_id:str,db:Session=Depends(get_db)):
    todos = todo.get_todos(db,user_id)
    return {"todos":todos}