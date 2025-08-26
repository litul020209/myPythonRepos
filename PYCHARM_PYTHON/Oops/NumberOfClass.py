
class Student:
    __Total=0
    def __init__(self):
        Student.__Total=Student.__Total+1

obj1=Student()
print(Student._Student__Total)
# obj2=Student()
# obj3=Student()
# print(Student.Total)
# Student.Total=0
# obj4=Student()
# print(Student.Total)