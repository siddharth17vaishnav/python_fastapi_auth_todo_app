from fastapi import FastAPI
from models import userModel
from config import engine
from routers.user.auth import router as userRouter
from routers.todo.todo import router as todoRouter

app = FastAPI()

userModel.Base.metadata.create_all(bind=engine)


@app.get('/') 
async def root():
    return {"message": "Hello World"}


app.include_router(userRouter,prefix="/users",tags=["users"])
app.include_router(todoRouter,prefix="/todo",tags=["todos"])
