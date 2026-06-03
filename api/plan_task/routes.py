from fastapi import APIRouter
from api.plan_task.service import PlanTaskService

router = APIRouter()
service = PlanTaskService()

@router.get("/")
async def get_plans():
    return service.get_all_plans()

@router.get("/student/{student_id}")
async def get_student_plans(student_id: int):
    return service.get_student_plans(student_id)

@router.post("/")
async def create_plan(plan: dict):
    return service.create_plan(plan)

@router.put("/{plan_id}")
async def update_plan(plan_id: str, plan: dict):
    return service.update_plan(plan_id, plan)

@router.delete("/{plan_id}")
async def delete_plan(plan_id: str):
    return service.delete_plan(plan_id)