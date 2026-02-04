from typing import Optional

from app.database.models import Task, TaskStatus
from .repository import create_task, get_tasks, get_task, delete_task, replace_task, update_task
from app.domain.exceptions import TaskNotFoundError


def create_task_service(
    *,
    title: str,
    description: Optional[str] = None,
    status: TaskStatus,
) -> Task:
        return create_task(
            Task(
                title=title,
                description=description,
                status=status,
            )
        )

def get_tasks_service(
    *,
    limit: Optional[int],
    offset: int,
):
    return get_tasks(limit,offset)


def get_task_service(task_id: int) -> Task:
    task = get_task(task_id)
    if not task:
        raise TaskNotFoundError
    return task

def delete_task_service(task_id: int) -> None:
    deleted = delete_task(task_id)
    if not deleted:
        raise TaskNotFoundError

def replace_task_service(*, task_id: int, title: str, description: str | None, status: TaskStatus) -> Task:
    task = replace_task(task_id=task_id, title=title, description=description, status=status)
    if not task:
        raise TaskNotFoundError
    return task

def update_task_service(
    *,
    task_id: int,
    title: str | None = None,
    description: str | None = None,
    status: TaskStatus | None = None,
) -> Task:
    task = update_task(
        task_id=task_id,
        title=title,
        description=description,
        status=status,
    )
    if not task:
        raise TaskNotFoundError
    return task