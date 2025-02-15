from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users: List['User'] = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users", response_model=List[User])
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int) -> User:
    if age < 18 or age > 120:
        raise HTTPException(status_code=400, detail="Age must be between 18 and 120")

    user_id = (max([user.id for user in users], default=0) + 1)
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


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