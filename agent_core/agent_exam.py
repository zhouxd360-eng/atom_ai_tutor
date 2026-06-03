class ExamAgent:
    def __init__(self, model_loader):
        self.model_loader = model_loader
    
    def generate_questions(self, subject, topic, count=5, difficulty="中等"):
        prompt = f"""请为{subject}学科的{topic}知识点生成{count}道{difficulty}难度的练习题。

要求：
1. 题目类型：选择题、填空题、问答题混合
2. 给出参考答案
3. 难度适中
"""
        return self.model_loader.generate(prompt)
    
    def grade_answer(self, question, student_answer):
        prompt = f"""题目：{question}
学生答案：{student_answer}

请批改学生答案，给出得分和详细评语。
"""
        return self.model_loader.generate(prompt)