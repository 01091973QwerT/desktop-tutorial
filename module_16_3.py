from fastapi import FastAPI, Path
from typing import Dict, Optional, Tuple, Annotated

app = FastAPI()

users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> Dict[str, str]:
    return users

@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]
) -> str:
    user_id = str(max(map(int, users.keys()), default=0) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[str, Path(..., description='Enter user ID')],
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]
) -> str:
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} has been updated"
    return "User not found"

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path(..., description='Enter user ID')]) -> str:
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    return "User not found"