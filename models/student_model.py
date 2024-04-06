from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age : int
    address : dict

class Student(BaseModel):
    id: str
    name : str
    age: int
    address: dict

