class StudentService:
    def __init__(self):
        self.students = []
    
    def get_all_students(self):
        return {"students": self.students}
    
    def get_student(self, student_id: int):
        student = next((s for s in self.students if s.get("id") == student_id), None)
        if student:
            return student
        return {"error": "Student not found", "student_id": student_id}
    
    def create_student(self, student: dict):
        new_id = len(self.students) + 1
        student["id"] = new_id
        self.students.append(student)
        return {"message": "Student created", "student": student}
    
    def update_student(self, student_id: int, student: dict):
        for i, s in enumerate(self.students):
            if s.get("id") == student_id:
                self.students[i].update(student)
                return {"message": "Student updated", "student": self.students[i]}
        return {"error": "Student not found", "student_id": student_id}
    
    def delete_student(self, student_id: int):
        for i, s in enumerate(self.students):
            if s.get("id") == student_id:
                deleted = self.students.pop(i)
                return {"message": "Student deleted", "student": deleted}
        return {"error": "Student not found", "student_id": student_id}