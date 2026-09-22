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


## Database

This project now uses **SQLite** instead of an in-memory list, so task 
data persists across server restarts.

- **Why SQLite:** Lightweight, file-based, requires no separate server 
  or installation — ideal for a small project like this.
- **Database file location:** `tasks.db` in the project root (created 
  automatically on first run).
- **How to start the project:** Same as before — `uvicorn main:app 
  --reload --port 8000`. The database and `tasks` table are created 
  automatically if they don't exist, and 3 example tasks are inserted 
  only on the very first run.

### Example SQL query

```sql
SELECT * FROM tasks WHERE done = 1;
```
Returns all completed tasks.


## Running with Docker

This project now runs fully containerized — both the API and PostgreSQL 
database start together with a single command.

### Start everything

```bash
docker compose up --build
```

This starts:
- **db**: PostgreSQL 16 in a container, with a named volume (`pgdata`) 
  so data survives container restarts
- **api**: The FastAPI app, built from the Dockerfile, connecting to 
  the `db` service using the `DATABASE_URL` environment variable

The API is available at `http://localhost:8000` — all endpoints and 
behavior are identical to the previous (SQLite) version. Only the 
storage layer changed.

### Environment variables

Copy `.env.example` to `.env` and fill in real values before running 
locally without Docker. When running via `docker compose`, the 
connection variables are already set in `docker-compose.yml`.

### Persistence proof

Created a task, ran `docker compose down` (stopping and removing both 
containers), then `docker compose up --build` again. The task was still 
present afterward — confirming data survives full container restarts, 
not just app restarts, because it's stored in the `pgdata` named volume.

### Stop everything

```bash
docker compose down
```


