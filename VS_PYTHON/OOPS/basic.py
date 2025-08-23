class demo:
    def __init__(self,name,age):
        self.n1=name
        self.a1=age

    def methd(self,subject_name):
        sub=subject_name
        print(f"Hi i am {self.n1}")
        print(f"And my age is {self.a1}")
        print(f"i teach {sub}")



student_01=demo("litul",22)
# print(student_01.n1)
# print(student_01.a1)

student_01.methd("python")