class StudyStatService:
    def __init__(self):
        self.stats = []
    
    def get_all_stats(self):
        return {"stats": self.stats}
    
    def get_student_stats(self, student_id: int):
        student_stats = [s for s in self.stats if s.get("student_id") == student_id]
        return {"student_id": student_id, "stats": student_stats}
    
    def get_subject_stats(self, student_id: int, subject: str):
        subject_stats = [
            s for s in self.stats 
            if s.get("student_id") == student_id and s.get("subject") == subject
        ]
        return {"student_id": student_id, "subject": subject, "stats": subject_stats}
    
    def add_stat(self, stat: dict):
        self.stats.append(stat)
        return {"message": "Stat added", "stat": stat}