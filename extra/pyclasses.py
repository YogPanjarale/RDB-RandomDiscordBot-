class mg():
    name = ''
    age = 17
    grade = 12
    def __init__(self,name):
        self.name = name
student = input("enter your name: \n")
student = mg(student)
print(student.age)
print(student.grade)
print(student.name)