from fastapi import APIRouter
from api.student_info.service import StudentService

router = APIRouter()
service = StudentService()

@router.get("/")
async def get_students():
    return service.get_all_students()

@router.get("/{student_id}")
async def get_student(student_id: int):
    return service.get_student(student_id)

@router.post("/")
async def create_student(student: dict):
    return service.create_student(student)

@router.put("/{student_id}")
async def update_student(student_id: int, student: dict):
    return service.update_student(student_id, student)

@router.delete("/{student_id}")
async def delete_student(student_id: int):
    return service.delete_student(student_id)