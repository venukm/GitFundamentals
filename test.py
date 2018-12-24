class name(object):
        def __init__(self, first_name, middle_name, last_name):
                self.FirstName = first_name
                self.MiddleName = middle_name
                self.LastName = last_name
        

class student(name):
        def __init__(self, first_name, middle_name, last_name, student_id):
                name.__init__(self, first_name, middle_name, last_name)
                self.StudentId = student_id

def readStudents():
        with open("student.txt", "r") as f:
                for s in f.readlines():
                        yield s


def writeStudent():
        first_name = input("Input student first name: ")
        middle_name = input("Input student middle name: ")
        last_name = input("Input student last name: ")
        student_id = input("Input student id: ")

        st = student(first_name, middle_name, last_name, student_id)

        with open("student.txt", "a") as f:
                f.write(str(st.__dict__) + "\n")


def main():
        writeStudent()

        for student in readStudents():
                print(student)


if __name__ == "__main__":
    main()