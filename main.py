from fastapi import FastAPI
from board import board_router
from todo.router import todo_router

app = FastAPI()

app.include_router(board_router)
app.include_router(todo_router)