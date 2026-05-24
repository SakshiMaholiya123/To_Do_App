from pydantic import BaseModel

class Task(BaseModel):
    id:int
    title:str
    description:str

class User(BaseModel):
    name:str
    password:str