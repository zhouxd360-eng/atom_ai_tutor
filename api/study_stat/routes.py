from fastapi import APIRouter
from api.study_stat.service import StudyStatService

router = APIRouter()
service = StudyStatService()

@router.get("/")
async def get_stats():
    return service.get_all_stats()

@router.get("/student/{student_id}")
async def get_student_stats(student_id: int):
    return service.get_student_stats(student_id)

@router.get("/student/{student_id}/subject/{subject}")
async def get_subject_stats(student_id: int, subject: str):
    return service.get_subject_stats(student_id, subject)

@router.post("/")
async def add_stat(stat: dict):
    return service.add_stat(stat)