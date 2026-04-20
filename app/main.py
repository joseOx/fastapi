from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

#Instancio la aplicacion con metadatos
app = FastAPI(
    title="Mi portfolio Task Manager API",
    description="API para la gestion de tareas, creada con FastAPI",
    version="1.0.0"
)

#Defino un esquema
class Task(BaseModel):
    id:Optional[int] = None
    title: str
    description: Optional[str] = None
    is_completed: bool = False

#base de datos temporal(de prueba)
tasks_db = ["holi"]

#Mis primeros endpoints

@app.get("/",tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Task Manager API"}

@app.get("/tasks", tags=["Tasks"])
async def get_tasks():
    return {"tasks": tasks_db}

@app.post("/tasks",tags = ["Tasks"])
async def create_task(task:Task):
    tasks_db.append(task)
    return {"message":"Task created successfully"}