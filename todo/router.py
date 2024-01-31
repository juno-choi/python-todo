from fastapi import APIRouter, Path, HTTPException, status
from todo.model import TodoItem, TodoResponse
todo_router = APIRouter(
    prefix="/api",
    tags=["todo"]
)

todo_list = []

@todo_router.post("/todo")
async def postTodo(todo: TodoItem) -> dict:
    todo_list.append(todo)
    return {"message" : "success"}

@todo_router.get("/todo", response_model=TodoResponse)
async def getTodo() -> dict:
    size = len(todo_list)
    if size == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="todo list is empty!"
        )
    return {"todos" : todo_list}

@todo_router.get("/todo/{id}")
async def getTodoItem(id: int = Path(gt=-1, title="todo id")) -> dict:
    return {"item" : todo_list[id]}

@todo_router.put("/todo/{todo_id}")
async def putTodoItem(todo: TodoItem, todo_id: int = Path(gt=-1, title="todoItem id")) -> dict:
    todo_list[todo_id] = todo
    return {"message" : "update success"}

@todo_router.delete("/todo")
async def deleteTodo() -> dict:
    todo_list.clear()
    return {"message" : "delete all success"}
