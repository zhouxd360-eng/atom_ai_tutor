from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_plans():
    return {"plans": []}

@router.get("/student/{student_id}")
async def get_student_plans(student_id: int):
    return {"student_id": student_id, "plans": []}

@router.post("/")
async def create_plan(plan: dict):
    return {"message": "Plan created", "plan": plan}

@router.put("/{plan_id}")
async def update_plan(plan_id: str, plan: dict):
    return {"message": "Plan updated", "plan_id": plan_id}

@router.delete("/{plan_id}")
async def delete_plan(plan_id: str):
    return {"message": "Plan deleted", "plan_id": plan_id}