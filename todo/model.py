from pydantic import BaseModel

class TodoItem(BaseModel):
    item : int
    class Config:
        json_schema_extra = {
            "example" : {
                "item" : 1
            }
        }