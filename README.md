# Mini_backend_project
Combination on Python,FastAPI,MongoDB

This is a simple **Todo App API** built using FastAPI and MongoDB. The API provides CRUD operations for managing tasks with soft-delete functionality, along with user deletion functionality.

## Features

- Create new todo tasks
- View all tasks (excluding soft-deleted ones)
- Update existing tasks
- Soft-delete tasks
- Delete users (from external route)

## Project Structure

├── main.py
├── configrations.py
├── database
│ ├── models.py
│ └── schemas.py
├── router
│ └── delete_user.py



