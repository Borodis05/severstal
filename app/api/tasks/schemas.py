from datetime import datetime
from enum import Enum as PyEnum

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TaskStatus(str, PyEnum):
    active = "active"
    completed = "completed"


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: TaskStatus = TaskStatus.active


class TaskIn(TaskBase):
    pass


class TaskOut(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TaskReplace(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None