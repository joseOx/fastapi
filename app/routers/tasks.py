from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

#Creo el rooter
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

class Task(BaseModel):
    id: int
    title:str
    is_completed: bool = False

#Base de datos temporal
tasks_db = ["holi"]

@router.get("/")
async def get_all_tasks():
    return tasks_db

@router.post("/")
async def create_task(task: Task):
    tasks_db.append(task)
    return {"message":"Tarea agregada con router","task":task}