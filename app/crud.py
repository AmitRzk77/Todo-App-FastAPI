# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

def get_task(db: Session, task_id: int) -> Optional[models.Task]:
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[models.Task]:
    return db.query(models.Task).order_by(models.Task.id.desc()).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
    db_task = models.Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, db_task: models.Task, updates: schemas.TaskUpdate) -> models.Task:
    if updates.title is not None:
        db_task.title = updates.title
    if updates.description is not None:
        db_task.description = updates.description
    if updates.completed is not None:
        db_task.completed = updates.completed
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, db_task: models.Task) -> None:
    db.delete(db_task)
    db.commit()
