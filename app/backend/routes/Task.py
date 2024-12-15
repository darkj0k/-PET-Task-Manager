from app.backend.schemas import Task
from fastapi import APIRouter, status, HTTPException
from app.backend.services.TaskService import TaskService
from app.backend.settings.exceptions import TasksListResponse



router = APIRouter(prefix="/task", tags=['task manager'])

@router.post('')
async def add_task(task_data: Task.Task, user_id: int):
    async with TaskService() as Service:
        await Service.add_task(task_data.model_dump(), user_id)
    return {"status": status.HTTP_200_OK}

@router.get('')
async def get_all_task(user_id: int):
    async with TaskService() as Service:
        tasks = await Service.get_all_tasks(user_id)
    return TasksListResponse(tasks)

@router.put('')
async def update_task(task_data: Task.Task, task_id: int):
    async with TaskService() as Service:
        await Service.update_task(task_id, task_data.model_dump())
    return HTTPException(status.HTTP_200_OK)
@router.delete('')
async def delete_task(task_id: int):
    async with TaskService() as Service:
        await Service.delete_task(task_id)
    return HTTPException(status.HTTP_200_OK)