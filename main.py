from fastapi import FastAPI
from app.routers import task
from app.routers import users

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(users.router)