from fastapi import APIRouter, Path
from todo.model import TodoItem
todo_router = APIRouter()

todo_list = []

