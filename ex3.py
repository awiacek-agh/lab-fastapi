from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str


class Student(BaseModel):
    id: int
    first_name: str
    last_name: str



STUDENTS = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/students")
async def students():
    return STUDENTS


@app.post("/students")
async def create_student(student: StudentCreateSchema):
    # id = len(STUDENTS) + 1
    # new_student = Student(**student.dict(), id=id) 
    # STUDENTS[id] = new_student 
    return student

