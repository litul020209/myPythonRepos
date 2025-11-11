class employee:
    total_emp=0
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
        employee.validDepartment(dept)

    def emp_info(self):
        print(f" employee name is {self.name}")
        print(f" employee department is {self.name}")

    @classmethod
    def total_employees(cls):
        return employee.total_emp

    @staticmethod
    def validDepartment(dept):
        if dept in ["HR", "IT", "Finance", "Admin"]:
            employee.total_emp+=1
        else:
            print("you can't choose for this company")

emp1=employee("Ronal Biswal","BIO")

print(employee.total_emp)
