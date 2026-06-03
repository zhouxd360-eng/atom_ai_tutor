from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_students():
    return {"students": []}

@router.get("/{student_id}")
async def get_student(student_id: int):
    return {"student_id": student_id}

@router.post("/")
async def create_student(student: dict):
    return {"message": "Student created", "student": student}

@router.put("/{student_id}")
async def update_student(student_id: int, student: dict):
    return {"message": "Student updated", "student_id": student_id}

@router.delete("/{student_id}")
async def delete_student(student_id: int):
    return {"message": "Student deleted", "student_id": student_id}