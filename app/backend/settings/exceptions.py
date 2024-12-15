from datetime import datetime
from fastapi import HTTPException, status

class TaskManagerException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""
    def __init__(self):
        super().__init__(self.status_code, self.detail)

class TaskWithCurrentIDAlreadyExistsException(TaskManagerException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Задача с этим ID уже существует"

class TaskManagerResponse:
    data = {}
    def __init__(self):
        return self.data

class TasksListResponse(TaskManagerResponse):
    def __init__(self, tasks: list):
        self.data = {"Tasks": tasks, "Time": datetime.now(datetime.timezone.utc)}
        super().__init__()