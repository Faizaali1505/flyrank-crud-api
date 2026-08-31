# Task CRUD API

A simple REST API to create, read, update, and delete tasks — built with FastAPI. Data is stored in memory (resets on server restart).

## How to run

1. Clone this repo and navigate into it
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Start the server: `uvicorn main:app --reload --port 8000`
6. Visit `http://localhost:8000/docs` for interactive API docs

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | List all tasks |
| GET | /tasks/{id} | Get a single task |
| POST | /tasks | Create a new task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Example

Create a task:
\`\`\`
curl.exe -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{\"title\":\"Buy milk\"}'
\`\`\`

Returns: `{"id": 4, "title": "Buy milk", "done": false}` with status `201`.