from fastapi import FastAPI, HTTPException, Query, Body
from typing import Optional, List
from pydantic import BaseModel
from pymongo import MongoClient, IndexModel, ASCENDING
from bson import ObjectId
import pymongo
import uvicorn
from pydantic import validate_call
from pymongo.errors import DuplicateKeyError
import dotenv
import os

dotenv.load_dotenv()

mongodb_uri = os.environ["MONGODB_CONNECTION_STRING"]

client = pymongo.MongoClient(mongodb_uri)

app = FastAPI()
client = MongoClient(mongodb_uri)
db = client["library"]
students_collection = db["students"]

# Create index for uniqueness constraint on 'username'
students_collection.create_indexes([IndexModel([("username", ASCENDING)], unique=True)])

# model for request body
class StudentCreate(BaseModel):
    full_name: str = ...
    username: str = ...
    age: int = ... 
    address: dict = ...
    interests: List[str]

# model for response body
class StudentResponse(BaseModel):
    student_id: str
    full_name: str
    username: str
    age: int
    address: dict
    interests: List[str]

#MongoDB schema for student documents
student_schema = {
    "full_name": {"type": "string"},
    "username": {"type": "string"},
    "age": {"type": "integer", "min": 0},
    "address": {
        "type": "dict",
        "schema": {
            "city": {"type": "string"},
            "country": {"type": "string"}
        }
    },
    "interests": {"type": "array", "items": {"type": "string"}}
}
@validate_call
def validate_student(student: dict):
    StudentCreate(**student)
@app.get("/")
async def root():
    return {"message": "Welcome to the Library Mangament System api"}

@app.post("/api/students", status_code=201, response_model=StudentResponse)
async def create_student(student: StudentCreate = Body(...)):
    if student.age <= 0:
        raise HTTPException(status_code=400, detail="Age must be greater than 0")
    
    validate_student(student.dict())
    
    try:
        result = students_collection.insert_one(student.dict())
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Student with this username already exists")
    
    return {"student_id": str(result.inserted_id), **student.dict()}


@app.get("/api/students", response_model=dict)
async def list_students(country: Optional[str] = Query(None, description="To apply filter of country."),
                        age: Optional[int] = Query(None, description="Only records which have age greater than equal to the provided age should be present in the result."),
                        interests: Optional[List[str]] = Query(None, description="Filter students by interests.")):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    if interests:
        query["interests"] = {"$in": interests}
    
    students = list(students_collection.find(query, {"_id": 0}))
    return {"data": students}

@app.get("/api/students/{id}", response_model=StudentResponse)
async def get_student(id: str):
    student = students_collection.find_one({"_id": ObjectId(id)})
    if student:
        return {"student_id": str(student["_id"]), **student}
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@app.patch("/api/students/{id}", status_code=204)
async def update_student(id: str, student: StudentCreate = Body(...)):
    validate_student(student.dict())
    result = students_collection.update_one({"_id": ObjectId(id)}, {"$set": student.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/api/students/{id}")
async def delete_student(id: str):
    result = students_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
