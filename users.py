from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update, delete
from slugify import slugify
from typing import Annotated

from backend.db import get_db
from sqlalchemy.testing.suite.test_reflection 

from app.models import user
from app.schemas import CreateUser, UpdateUser

router = APIRouter(prefix="/user", tags=["user"])

# Функция для получения всех пользователей
@router.get("/")
def all_users(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(user)).scalars().all() # Получаем и возвращаем всех пользователей
    return result

# Функция для получения пользователя по ID
@router.get("/{user_id}")
def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)], user=None):
    user = db.execute(select(user).where(user.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user

# Функция для создания нового пользователя
@router.post("/create")
def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    new_user = user(**user.dict(), slug=slugify(user.username))
    db.execute(insert(user).values(new_user.__dict__))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

# Функция для обновления пользователя
@router.put("/update/{user_id}")
def update_user(user_id: int, user_data: UpdateUser, db: Annotated[Session, Depends(get_db)], user=None):
    user = db.execute(select(user).where(user.id == user_id)).scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    for key, value in user_data.dict().items():
        setattr(user, key, value)

    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }

# Функция для удаления пользователя
@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)], user=None):
    user = db.execute(select(user).where(user.id == user_id)).scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(delete(user).where(user.id == user_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User deleted successfully!'
    }
