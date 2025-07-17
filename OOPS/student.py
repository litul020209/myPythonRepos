class student:
    def __init__(self,name,age,sec,work):
        self.n=name
        self.a=age
        self.s=sec
        self.mark=0
        self.attend=0
        self.w=work

    def attendence(self):
        if self.w>=60:
            self.attend=75
        else:
            self.attend=70
        return self.attend

    def score(self,mark):
        if self.attend >=75:
             self.mark=80
        else:
             self.mark=70
        return self.mark
        
    
       
        


student_01=student("litul" ,21, "A" ,50)
print(student_01.n)
print(student_01.a)
print(student_01.s)
print(student_01.attendence())
print(student_01.score(50))






    

        
