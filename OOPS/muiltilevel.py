class student:
    def show(self,num1):
        self.n1=num1
        print(f"total number of students {self.n1}")
class graduate(student):
    def show(self,num1,num2):
        self.n2=num2
        super().show(num1)
        print(f"the {self.n2} students are graduate")
        
    
class employee(graduate):
      def show(self,num1,num2,num3):
          self.n3=num3
          super().show(num1,num2)
          print(f"the {self.n3} students are get job")


clg_01=employee()
print(clg_01.show(100,70,50))