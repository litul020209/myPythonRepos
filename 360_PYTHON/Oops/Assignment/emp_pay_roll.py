
class Employee:
    def __init__(self,id,name,salary):
        self.__emp_id=id
        self.__emp_name=name
        self.__base_salary=salary

    @property
    def emp_id(self):
        return self.__emp_id
    @emp_id.setter
    def emp_id(self,id):
        self.__emp_id=id
    
    @property
    def emp_name(self):
        return self.__emp_name
    @emp_name.setter
    def emp_name(self,name):
        self.__emp_name=name

    @property
    def base_salary(self):
        return self.__base_salary
    @base_salary.setter
    def base_salary(self,salary):
       self.__base_salary=salary
        
class FullTimeEmployee(Employee):
    full_time_emp=[]
    def __init__(self, id, name, salary,bonus,hra):
        super().__init__(id, name, salary)
        self.__bonus=bonus
        self.__hra=hra
    @property
    def bonus(self):
        return self.__bonus
    @ bonus.setter
    def bonus(self,bonus):
        self.__bonus=bonus
    
    @property
    def hra(self):
        return self.__hra
    @hra.setter
    def hra(self,hra):
        self.__hra=hra

class PartTimeEmployee(Employee):
    part_time_emp=[]
    def __init__(self, id, name, salary,house_worked,rate_per_hour):
        super().__init__(id, name, salary)
        self.__house_worked=house_worked
        self.__rate_per_hour=rate_per_hour

    @property
    def house_worked(self):
        return self.__house_worked
    @house_worked.setter
    def house_worked(self,hw):
        self.__house_worked=hw
    
    @property
    def rate_per_hour(self):
        return self.__rate_per_hour
    @rate_per_hour.setter
    def rate_per_hour(self,rph):
        self.__rate_per_hour=rph
        
class Office:
    @staticmethod
    def add_employee(emp):        
        if isinstance(emp,FullTimeEmployee):
            FullTimeEmployee.full_time_emp.append(emp)
        else:
            PartTimeEmployee.part_time_emp.append(emp)
    @staticmethod
    def remove_employee(emp):
        if isinstance(emp,FullTimeEmployee):
            FullTimeEmployee.full_time_emp.remove(emp)        
        else:
            PartTimeEmployee.part_time_emp.remove(emp)
    @staticmethod
    def get_salary(emp):
        if isinstance(emp,FullTimeEmployee):
            return emp.base_salary+emp.bonus+emp.hra
        else:
            return emp.base_salary+(emp.house_worked*emp.rate_per_hour*30)
    @staticmethod
    def month_salary_report():
        total_salary_for_full_time=0
        o=Office()
        for x in FullTimeEmployee.full_time_emp:
            total_salary_for_full_time+=o.get_salary(x)
        total_salary_for_part_time=0
        for x in PartTimeEmployee.part_time_emp:
            total_salary_for_part_time+=o.get_salary(x)
        print(f"total salary invest on full time employee {total_salary_for_full_time}")
        print(f"total salary invest on part time employee {total_salary_for_part_time}")

e1=PartTimeEmployee(26001,"Litu",1000,8,50)
e2=FullTimeEmployee(26002,"Virat",12000,4000,4000)
o1=Office()
o1.add_employee(e1)
o1.add_employee(e2)
o1.month_salary_report()
