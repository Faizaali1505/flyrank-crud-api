from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Finish assignment", "done": False},
    {"id": 3, "title": "Read a book", "done": True},
]

class TaskCreate(BaseModel):
    title: str
    
@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks", summary="List all tasks")
@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", summary="Get a single task by ID")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})


@app.post("/tasks", status_code=201, summary="Create a new task")
def create_task(new_task: TaskCreate):
    if not new_task.title or not new_task.title.strip():
        raise HTTPException(status_code=400, detail={"error": "Title is required and cannot be empty"})

    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": next_id, "title": new_task.title, "done": False}
    tasks.append(task)
    return task



class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None

@app.put("/tasks/{task_id}", summary="Update a task's title or done status")
def update_task(task_id: int, updates: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if updates.title is not None:
                if not updates.title.strip():
                    raise HTTPException(status_code=400, detail={"error": "Title cannot be empty"})
                task["title"] = updates.title
            if updates.done is not None:
                task["done"] = updates.done
            return task
    raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})

@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return
    raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})



