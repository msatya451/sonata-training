class Student:
    def __init__(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name
    def display(self):
        print("student_id:",self.student_id)
        print("student_name:",self.student_name)
obj=Student("222222","satya")
obj.display()