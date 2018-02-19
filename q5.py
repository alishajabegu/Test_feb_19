
#Q5. Define an Student class and initialize it with name and section.
#  Now, make a classmethod that takes in a string parameter "name-A"
# which creates an instance and returns the instance based on parameter. [Hint: use @classmethod decorator]


class Student:


    def __init__(self, student_name, student_sec):
         self.student_name = student_name
         self.student_sec = student_sec


    @classmethod
    def gen_student_from_string(cls, inp):
         student_name, student_sec = inp.split("-")
         return cls(student_name, student_sec)


students = Student.gen_student_from_string("Alisha-A")
print(students.__dict__)