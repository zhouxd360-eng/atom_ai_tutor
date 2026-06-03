class PlanTaskService:
    def __init__(self):
        self.plans = []
    
    def get_all_plans(self):
        return {"plans": self.plans}
    
    def get_student_plans(self, student_id: int):
        student_plans = [p for p in self.plans if p.get("student_id") == student_id]
        return {"student_id": student_id, "plans": student_plans}
    
    def create_plan(self, plan: dict):
        plan_id = f"plan_{len(self.plans) + 1}"
        plan["id"] = plan_id
        self.plans.append(plan)
        return {"message": "Plan created", "plan": plan}
    
    def update_plan(self, plan_id: str, plan: dict):
        for i, p in enumerate(self.plans):
            if p.get("id") == plan_id:
                self.plans[i].update(plan)
                return {"message": "Plan updated", "plan": self.plans[i]}
        return {"error": "Plan not found", "plan_id": plan_id}
    
    def delete_plan(self, plan_id: str):
        for i, p in enumerate(self.plans):
            if p.get("id") == plan_id:
                deleted = self.plans.pop(i)
                return {"message": "Plan deleted", "plan": deleted}
        return {"error": "Plan not found", "plan_id": plan_id}