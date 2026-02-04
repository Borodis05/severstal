from fastapi import APIRouter, HTTPException, Query, status
from typing import List, Optional

from app.domain.exceptions import DuplicateTitleError, TaskNotFoundError
from app.domain.tasks.service import (create_task_service, get_tasks_service, get_task_service, delete_task_service,
                                      replace_task_service, update_task_service)
from .schemas import TaskOut, TaskIn, TaskReplace, TaskUpdate

router = APIRouter()

@router.post("", response_model=TaskOut)
async def create_task_route(data: TaskIn):
    try:
        return create_task_service(
            title=data.title,
            description=data.description,
            status=data.status,
        )
    except DuplicateTitleError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Task title already exists",
        )

@router.get("", response_model=List[TaskOut])
async def get_tasks_route(
    limit: Optional[int] = Query(
        default=None,
        ge=1,
        le=100,
        description="Количество задач (если не указано — все)",
    ),
    offset: int = Query(
        default=0,
        ge=0,
        description="Смещение",
    ),
):
    return get_tasks_service(limit=limit, offset=offset)


@router.get("/{task_id}", response_model=TaskOut)
async def get_task_route(task_id: int):
    try:
        return get_task_service(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}", status_code=204)
async def delete_task_route(task_id: int):
    try:
        delete_task_service(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")


@router.put("/{task_id}", response_model=TaskOut)
async def replace_task_route(task_id: int, data: TaskReplace):
    try:
        return replace_task_service(
            task_id=task_id,
            title=data.title,
            description=data.description,
            status=data.status,
        )
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")

@router.patch("/{task_id}", response_model=TaskOut)
async def update_task_route(task_id: int, data: TaskUpdate):
    try:
        return update_task_service(
            task_id=task_id,
            title=data.title,
            description=data.description,
            status=data.status,
        )
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")