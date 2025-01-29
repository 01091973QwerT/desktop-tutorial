from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update, delete, delete
from typing import Annotated
from slugify import slugify

from backend.db import get_db
from app.models import task, user
from app.schemas import CreateTask, UpdateTask

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
def all_tasks(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(task)).scalars().all()
    return result

@router.get("/{task_id}")
def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)], task=None):
    task = db.execute(select(task).where(task.id == task_id)).scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task

@router.post("/create")
def create_task(task_data: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)], user=None):
    user = db.execute(select(user).where(user.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    new_task = task(user_id=user_id, **task_data.dict(), slug=slugify(task_data.title))
    db.execute(insert(task).values(new_task.__dict__))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

@router.put("/update/{task_id}")
def update_task(task_id: int, task_data: UpdateTask, db: Annotated[Session, Depends(get_db)], task=None):
    task = db.execute(select(task).where(task.id == task_id)).scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    for key, value in task_data.dict().items():
        setattr(task, key, value)

    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update is successful!'
    }

@router.delete("/delete/{task_id}")
def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)], task=None):
    task = db.execute(select(task).where(task.id == task_id)).scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.execute(delete(task).where(task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task deleted successfully!'
    }


