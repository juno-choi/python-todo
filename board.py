from fastapi import APIRouter, Path
from pydantic import BaseModel

board_router = APIRouter(prefix="/api",tags=["board"])

board_list = []

class Member(BaseModel):
    id: int
    name: str

class Board(BaseModel):
    id: int
    subject: str
    content: str
    member: Member

    class Config:
        json_schema_extra = {
            "example" : {
                "id" : 1,
                "subject" : "제목",
                "content" : "내용",
                "member" : {
                    "id" : 1,
                    "name" : "이름"
                }
            }
        }

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

@board_router.get("/board/{id}")
def getDetail2(id: int = Path(gt=0, title="게시판 id")) -> dict:
    return {"board" : board_list[id]}