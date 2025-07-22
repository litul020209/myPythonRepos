#access specifier
from abc import ABC,abstractmethod

class employee(ABC):
    
    def add_info(self,name,dept,emp_id,password,salary):
        self.name=name
        self.dept=dept
        self._empid=emp_id
        self.__password=password
        self.__bonus=2000
        self._salary=salary

    
    
    def __securityCheck(self,__password):
          self.ans=True if __password=="admin123" else False
          return self.ans
    
    
    def Salarycheck(self):
        if self.__securityCheck(self,self.__password):
            self._salary=self._salary+self.__bonus
            return self._salary
    

class hr(employee):
     
    def add_info(self,name,dept,emp_id,password,salary):
        employee.add_info(self,name,dept,emp_id,password,salary)


    def Salarycheck(self):
        employee.Salarycheck(self)
        print(f"your salary is {self._salary}")     
        


emp_id=input("enter your emp_id: ")
name=input("enter the name : ")
dept=input("enter the dept: ")
password=input("enter the pass word: ")
salary=int(input("enter your salary: "))

employee_01=hr(emp_id,name,salary,password,dept)
employee_01.add_info(emp_id,name,salary,password,dept)
employee_01.show_info()

#more work way to do in this code ..

