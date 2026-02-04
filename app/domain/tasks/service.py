from typing import Optional

from app.database.models import Task, TaskStatus
from .repository import create_task, get_tasks, get_task
from app.domain.exceptions import TaskNotFoundError

def create_task_service(
    *,
    title: str,
    status: TaskStatus,
) -> Task:
        return create_task(
            Task(
                title=title,
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