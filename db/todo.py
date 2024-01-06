from sqlalchemy.orm import Session
from models.todoModel import Todo
from schemas.todo import AddTodoRequest

def get_todos(db:Session , user_id:int):
    return db.query(Todo).filter(Todo.user_id == user_id ).all()

def create_todo(db:Session,user_id:int,todo:AddTodoRequest):
    print(todo.todo)
    db_todo = Todo(user_id = user_id,todo=todo.todo)
    
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
    