from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_stats():
    return {"stats": []}

@router.get("/student/{student_id}")
async def get_student_stats(student_id: int):
    return {"student_id": student_id, "stats": []}

@router.get("/student/{student_id}/subject/{subject}")
async def get_subject_stats(student_id: int, subject: str):
    return {"student_id": student_id, "subject": subject, "stats": []}

@router.post("/")
async def add_stat(stat: dict):
    return {"message": "Stat added", "stat": stat}