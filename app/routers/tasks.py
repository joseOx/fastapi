from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

#Creo el router
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

class Task(BaseModel):
    id: int
    title:str
    is_completed: bool = False

@router.get("/")
async def read_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

@router.post("/")
async def create_task(title: str , description: str, db: Session = Depends(get_db)):
    new_task = models.Task(title=title, description=description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message":"Tarea agregada con router","task": new_task}