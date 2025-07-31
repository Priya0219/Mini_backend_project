from datetime import datetime
from pydantic import BaseModel

class todo_input(BaseModel):
    title : str
    description : str
    is_completed : bool = False
    is_deleted : bool = False
    updated_at: int = int(datetime.timestamp(datetime.now()))
    created_at: int = int(datetime.timestamp(datetime.now()))

