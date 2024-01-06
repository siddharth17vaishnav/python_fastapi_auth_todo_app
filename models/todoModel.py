from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from config import Base
from utils.contants import Status

class Todo(Base):
    __tablename__ = 'todos'
    
    id= Column(Integer,primary_key=True)
    todo= Column(String)
    status= Status
    user_id = Column(Integer, ForeignKey('users.id'))
    user= relationship("User")