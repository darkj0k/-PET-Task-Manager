from typing import Literal
from pydantic import BaseModel, Field, field_validator


class Task(BaseModel):
    title: str = Field(max_length=100)
    description: str

