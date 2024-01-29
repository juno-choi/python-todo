from fastapi import APIRouter
from pydantic import BaseModel

board_router = APIRouter()

board_list = []

class Board(BaseModel) :
    id: int
    subject: str
    content: str

@board_router.get("/board")
def get() -> dict:
    return {"list" : board_list}

@board_router.post("/board")
def post(board: dict) -> dict:
    board_list.append(board)
    return {"message" : "success"}

@board_router.post("/v2/board")
def post(board: Board) -> dict:
    board_list.append(board)
    return {"message" : "success"}