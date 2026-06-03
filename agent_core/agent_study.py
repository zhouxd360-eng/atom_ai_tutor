class StudyAgent:
    def __init__(self, model_loader):
        self.model_loader = model_loader
    
    def analyze_weakness(self, student_id, subject, history_data):
        prompt = f"""分析学生 {student_id} 在 {subject} 学科的学习情况：
历史数据：{history_data}

请分析该学生的薄弱知识点，并给出针对性建议。
"""
        return self.model_loader.generate(prompt)
    
    def generate_explanation(self, topic, difficulty="中等"):
        prompt = f"""请以{difficulty}难度水平，详细讲解以下知识点：{topic}

要求：
1. 概念清晰
2. 举例说明
3. 重点突出
"""
        return self.model_loader.generate(prompt)