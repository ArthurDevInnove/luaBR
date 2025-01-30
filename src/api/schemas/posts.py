from pydantic import BaseModel
from datetime import datetime, time

class PostsCreate(BaseModel):
    title: str
    content: str
    hour: time = datetime.now().time().replace(microsecond=1)

class PostsEdit(BaseModel):
    title: str
    content: str