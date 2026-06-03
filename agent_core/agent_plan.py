class PlanAgent:
    def __init__(self, model_loader):
        self.model_loader = model_loader
    
    def generate_daily_plan(self, student_id, subjects, duration=60):
        prompt = f"""为学生{student_id}制定一份{duration}分钟的每日学习计划：

学习科目：{subjects}

要求：
1. 合理分配时间
2. 包含复习和练习环节
3. 符合学生认知规律
"""
        return self.model_loader.generate(prompt)
    
    def generate_weekly_plan(self, student_id, subjects, goals):
        prompt = f"""为学生{student_id}制定一份周学习计划：

学习科目：{subjects}
学习目标：{goals}

要求：
1. 合理安排每天的学习内容
2. 包含复习、练习、测试环节
3. 难度循序渐进
"""
        return self.model_loader.generate(prompt)