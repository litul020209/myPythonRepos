
class Student:
    __student_id=1
    def __init__(self,marks,age):
        self.__mark=marks
        self.__age=age
        self.__studentID=Student.__student_id
        self.validity_marks()

    def validity_marks(self):
        if 0 <= self.__mark <= 100:
            print("your mark is eligible for apply")
            self.validity_age()
        else:
            print("your mark is not eligible for this time")
            return "thanks"
    def validity_age(self):
        if self.__age>=20:
            print("your age also verified for apply ")
            self.check_qualification()

        else:
            print("your age is not eligible for this time")
            return "thanks"
    def check_qualification(self):
        if self.__mark>=65:
            Student.__student_id += 1
            print(f"congratulation your are qualified for this college and your student id is {self.__studentID}")
            return "thanks"

        else:
            print("ohh you have not enough mark to study in here")
            return "thanks"

    def get_marks(self):
        return self.__mark
    def set_marks(self,value):
        self.__mark=value
        return self.__mark

    def get_age(self):
        return self.__age
    def set_age(self,value):
        self.__age=value
        return self.__age

    def get_student_id(self):
        return self.__studentID

student1=Student(100,21)
print(student1.get_age())
print(student1.set_age(22))