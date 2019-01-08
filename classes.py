class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


    def __str__(self):
        return f'{self.student_id}, {self.name}'


mark = Student('Mark', 1)
print(mark)
