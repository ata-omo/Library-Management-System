from fastapi import APIRouter, HTTPException

from models.student_model import Student, StudentCreate

from db_config.db_connect import students_collection

from typing import Optional,List

from schema.student_schema import studentEntity ,studentsEntity

std = APIRouter()


@std.post("/students", response_model=Student)
async def create_student(student: StudentCreate):
    result = students_collection.insert_one(student.dict())
    created_student = students_collection.find_one({"_id": result.inserted_id})
    return {**created_student, "id": str(created_student["_id"])}

# API to list students
@std.get("/students", response_model=list[Student])
async def list_students(country: str = None, age: int = None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    students = students_collection.find(query, {"_id": 0})
    return [{**student, "id": str(student["_id"])} for student in students]

# API to fetch a student by ID
@std.get("/students/{id}", response_model=Student)
async def get_student(id: str):
    student = students_collection.find_one({"_id": id})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {**student, "id": str(student["_id"])}

# API to update a student by ID
@std.patch("/students/{id}")
async def update_student(id: str, student: StudentCreate):
    result = students_collection.update_one({"_id": id}, {"$set": student.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student updated successfully"}

# API to delete a student by ID
@std.delete("/students/{id}")
async def delete_student(id: str):
    result = students_collection.delete_one({"_id": id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}