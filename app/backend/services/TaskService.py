from app.backend.database.main import DataBasePool
from app.backend.database.query.task import *
from app.backend.schemas import Task
from app.backend.settings.settings import env_settings

class TaskService(DataBasePool):
    def __init__(self, URL: str = env_settings.POSTGRESQL_URL):
        self.__URL = URL
    async def get_all_tasks(self, user_id: int):
        result = await self.operation(task_get_all, 'select', user_id)
        return result 

    async def add_task(self, task_data: dict, user_id: int):
        await self.operation(task_add, 'insert', task_data, user_id)

    async def update_task(self, task_id: int, task_data: dict):
        await self.operation(task_update, 'update', task_data, task_id)
        
    
    async def delete_task(self, task_id: int):
        await self.operation(task_delete, 'delete', task_id)

    