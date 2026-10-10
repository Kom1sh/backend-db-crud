from fastapi import Depends

from repositories.tasks import TaskRepository
from schemas import TaskIn, TaskUpdate
from models.tasks import Task


class TaskService:
    def __init__(self, repository: TaskRepository = Depends()):
        self.repository = repository

    def create_task(self, task: TaskIn) -> Task:
        return self.repository.create(task)

    def get_tasks_collection(self) -> list[Task]:
        return self.repository.get_all()

    def get_task(self, id: int) -> Task | None:
        return self.repository.get_by_id(id)

    def edit_task(self, id: int, upd_data: TaskUpdate) -> Task | None:
        task = self.repository.get_by_id(id)

        if not task:
            return None

        upd_data = upd_data.model_dump(exclude_none=True)
        return self.repository.update(task, upd_data)

    def delete_task(self, id: int) -> bool:
        task = self.repository.get_by_id(id)

        if not task:
            return False

        self.repository.delete(task)
        return True
