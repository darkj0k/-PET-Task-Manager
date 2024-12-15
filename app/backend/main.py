from fastapi import FastAPI, APIRouter, HTTPException
from app.backend.routes.Task import router as router_task
from app.backend.services.TaskService import TaskService

app = FastAPI()
utils_router = APIRouter(prefix="/utils", tags=['Utilities'])
@utils_router.get('')
async def migration():
    async with TaskService() as conn:
        await conn.migration()
    return HTTPException(status_code=200)

app.include_router(utils_router)
app.include_router(router_task)