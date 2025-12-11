class Bput:
    
    class Department:
        __department_hod={"Cse":"Hari Babu","Eee":"Manas Babu","Etc":"Sekhar Babu","Civil":"Niti Shakti"}

        @classmethod
        def get_dept(cls):
            return cls.__department_hod
        
        @classmethod
        def set_dept(cls,dept_name,dept_hod):
            cls.__department_hod[dept_name]=dept_hod
                  
    def show_department(self):
        return Bput.Department.get_dept()
    
    def add_department(self,dept_name,dept_hod):
        Bput.Department.set_dept(dept_name,dept_hod)
    def search_dept(self,dept_name):
        dept_list=Bput.Department.get_dept()
        if dept_name in dept_list:
            print("dept is present in this university")
        else:
            print("dept is not present in this university")



obj1=Bput()
for k,v in obj1.show_department().items():
    print(f"dept is {k} and hod is {v}")

obj1.add_department("IT","Navya Parbhu")

obj1.search_dept("Auto mobile")



    


            
            

          