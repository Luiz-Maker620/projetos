from dao.student_dao import StudentDAO

class StudentService:
    def __init__(self):
        self.dao = StudentDAO()

    def register_student(self, name, age, email):
        return self.dao.create(name, age, email)
        
    def update_student(self, student_id,name,age,email):
        print("atualizei o aluno")

    def remove_student(self, student_id):
        return self.dao.delete(student_id)
    
    def list_students(self):
        print("listei os alunos")

    