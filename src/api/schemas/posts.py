from pydantic import BaseModel
from datetime import datetime

class PostsCreate(BaseModel):
    title: str
    content: str
    hour: datetime = datetime.now()

class PostsEdit(BaseModel):
    title: str
    content: str