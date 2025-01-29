from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    password: str
    email: str

class UserLogin(BaseModel):
    email: str
    password: str