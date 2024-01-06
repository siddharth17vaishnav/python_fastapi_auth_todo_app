from pydantic import BaseModel

class AddTodoRequest(BaseModel):
    todo: str