from typing import List
from pydantic import BaseModel

class TodoItem(BaseModel):
    item : int
    name : str
    class Config:
        json_schema_extra = {
            "example" : {
                "item" : 1,
                "name" : "이름"
            }
        }

class TodoResponse(BaseModel):
    todos : List[TodoItem]
    class Config:
        json_schema_extra = {
            "example" : {
                "todos" : [
                    {
                        "item" : "item1",
                        "name" : "name1"
                    },
                    {
                        "item" : "item2",
                        "name" : "name2"
                    }
                ]
            }
        }