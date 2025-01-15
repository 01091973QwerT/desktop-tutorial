# uvicorn module.16_5:app --reload
from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users: List['User'] = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> User:
    if age < 18 or age > 120:
        raise HTTPException(status_code=400, detail="Age must be between 18 and 120")

    user_id = (max([user.id for user in users], default=0) + 1)
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, username: str, age: int) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return f"User {user_id} has been deleted"
    raise HTTPException(status_code=404, detail="User was not found")