class clg:
    def __init__(self,Dept):
        self.Dept=Dept
        self.clg_name="VITAM"

class student(clg):
     def __init__(self, Dept,name,roll_num):
         self.name=name
         self.Roll_num=roll_num
         super().__init__(Dept)
     def Student_data(self):
         print(f"college name {self.clg_name}")
         print(f"studenet name is {self.name}")
         print(f"studenet roll number is {self.Roll_num}")
         print(f"studenet branch is {self.Dept}") 

class facualty(clg):
    def __init__(self, Dept,name,id):
        self.name=name
        self.id=id
        super().__init__(Dept)
    def faculty_data(self):
         print(f"college name {self.clg_name}")
         print(f"facualty name is {self.name}")
         print(f"facualty id  name is {self.id}")
         print(f"studenet branch is {self.Dept}") 
        

student_01=student("CSE", "Litul Biswal" ,"21CSE09")
student_01.Student_data()

facualty_01=facualty("MECH" ,"Pranab Das" ,"MECH04")  
facualty_01.faculty_data()
