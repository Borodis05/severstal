from typing import List, Optional

from sqlalchemy.exc import IntegrityError

from app.database.config import SessionLocal
from app.database.models import Task
from app.domain.exceptions import DuplicateTitleError

def create_task(task: Task) -> Task:
    with SessionLocal() as session:
        session.add(task)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            raise DuplicateTitleError
        session.refresh(task)
        return task

def get_tasks(
    limit: Optional[int],
    offset: int
) -> List[Task]:
    with (SessionLocal() as db):
        query =(
            db.query(Task)
            .order_by(Task.created_at.desc())
        )
        if offset:
            query = query.offset(offset)

        if limit is not None:
            query = query.limit(limit)

        return query.all()

def get_task(task_id: int) -> Optional[Task]:
    with SessionLocal() as session:
        return session.query(Task).filter(Task.id == task_id).first()

def delete_task(task_id: int) -> bool:
    with SessionLocal() as session:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            return False
        session.delete(task)
        session.commit()
        return True