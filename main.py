from fastapi import FastAPI
from board import board_router
from todo.router import todo_router

app = FastAPI(
    title="concierge api",
    description="청약 api",
    version="0.0.1",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

app.include_router(board_router)
app.include_router(todo_router)