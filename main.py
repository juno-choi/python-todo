from fastapi import FastAPI
from board import board_router

app = FastAPI()

app.include_router(board_router)    # ,로 계속해서 추가 가능