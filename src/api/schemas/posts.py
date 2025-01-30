from pydantic import BaseModel
from datetime import time

class PostsCreate(BaseModel):
    title: str
    content: str
    hour: time
