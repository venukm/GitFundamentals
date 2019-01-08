from name import Name

class Student():
    def __init__(self, student_id, first_name, middle_name, last_name):
        self.name = Name(first_name, middle_name, last_name)
        self.student_id = student_id

test_student = Student(1, 'Venu', 'Madhav', 'Kottooru')

print(test_student.name.first_name)

