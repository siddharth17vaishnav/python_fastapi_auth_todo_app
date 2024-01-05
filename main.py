from fastapi import FastAPI
from models import userModel
from config import engine
from routers.user.auth import router

app = FastAPI()

userModel.Base.metadata.create_all(bind=engine)


@app.get('/') 
async def root():
    return {"message": "Hello World"}


app.include_router(router,prefix="/users",tags=["users"])