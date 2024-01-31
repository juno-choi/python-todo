from fastapi import APIRouter, Path
from todo.model import TodoItem
todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def postTodo(todo: TodoItem) -> dict:
    todo_list.append(todo)
    return {"message" : "success"}

@todo_router.get("/todo")
async def getTodo() -> dict:
    return {"list" : todo_list}

@todo_router.get("/todo/{id}")
async def getTodoItem(id: int = Path(gt=-1, title="todo id")) -> dict:
    return {"item" : todo_list[id]}

@todo_router.put("/todo/{todo_id}")
async def putTodoItem(todo: TodoItem, todo_id: int = Path(gt=-1, title="todoItem id")) -> dict:
    todo_list[todo_id] = todo
    return {"message" : "update success"}