from fastapi import APIRouter, Depends, HTTPException
from schemas import TaskIn, TaskOut, TaskUpdate
from services.tasks import TaskService

router = APIRouter(tags=["tasks"])


@router.post("/tasks", status_code=201, response_model=TaskOut)
def create_task(task: TaskIn, service: TaskService = Depends()):
    return service.create_task(task)


@router.get("/tasks", status_code=200, response_model=list[TaskOut])
def get_tasks_collection(service: TaskService = Depends()):
    return service.get_tasks_collection()


@router.get("/tasks/{id}", status_code=200, response_model=TaskOut)
def get_task(id: int, service: TaskService = Depends()):
    task = service.get_task(id)

    if task:
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found.")


@router.patch("/tasks/{id}", status_code=200, response_model=TaskOut)
def edit_task(id: int, upd_data: TaskUpdate, service: TaskService = Depends()):
    task = service.edit_task(id, upd_data)

    if task:
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found.")


@router.delete("/tasks/{id}", status_code=200)
def delete_task(id: int, service: TaskService = Depends()):
    if service.delete_task(id):
        return {"message": "Task was deleted."}
    else:
        raise HTTPException(status_code=404, detail="Task not found.")
