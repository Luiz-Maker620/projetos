from models.student import Student

class StudentDAO:
    def create(self,name,age,email):
            return Student.create(name=name,age=age,email=email)
    
    
    def get_by_id(seelf,student_id):
        try:
            return Student.get(Student.id == student_id) 
        except Student.DoesNotExists:
                return None

    def delete(self,student_id):
        student = self.get_by_id(student_id)
        
        if student:
            student.delete_instance()
            return True




        
    


