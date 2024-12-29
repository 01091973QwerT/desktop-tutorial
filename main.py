#uvicorn main:app --reload    Актвация
from fastapi import FastAPI

app = FastAPI()



@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id(user_id: int) -> dict: # user_id автоматически преобразуется в целое число
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def user_info(username: str, age: int) -> dict: #username и age берутся из query params
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}

