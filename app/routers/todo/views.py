from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.schemas.todo_schema import TodoCreate, TodoInDB, TodoUpdate, serialize_todos, serialize_todo
from app.db.db_mongo import get_database

router = APIRouter()
db = get_database()

@router.get("/test")
async def read_todos(): return ("ddd")


@router.get("/")
async def read_todos():
    todos = list(db.todos.find())
    return serialize_todos(todos)


@router.post("/", response_model=TodoInDB)
async def create_todo(todo: TodoCreate):
    todo_id = db.todos.insert_one(todo.dict()).inserted_id
    todo = db.todos.find_one({"_id": todo_id})
    return serialize_todo(todo)


@router.put("/{todo_id}")
async def update_todo(todo_id: str, todo: TodoUpdate):
    todo = dict(todo)
    result = db.todos.update_one({"_id": ObjectId(todo_id)}, {"$set": todo})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail=f"Todo with ID {todo_id} not found")
    return {"message": "Todo updated"}