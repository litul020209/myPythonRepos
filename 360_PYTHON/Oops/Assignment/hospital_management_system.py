class Person:
    def __init__(self,name,age,gender):
        self.__name=name
        self.__age=age
        self.__gender=gender

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,n):
        self.__name=n

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,a):
        self.__age=a

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,g):
        self.__gender=g       
class Patienet(Person):
    def __init__(self, name, age, gender,patient_id,disease,doctor_assign):
        super().__init__(name, age, gender)
        self.__patient_id=patient_id
        self.__disease=disease
        self.__doctor_assign=doctor_assign
    
    @property
    def patientid(self):
        return self.__patient_id
    @patientid.setter
    def patientid(self,id):
        self.__patient_id=id
    
    @property
    def patientid(self):
        return self.__patient_id
    @patientid.setter
    def patientid(self,id):
        self.__patient_id=id

    @property
    def disease(self):
        return self.__disease
    @disease.setter
    def disease(self,d):
        self.__disease=d
    
    @property
    def doctor_assign(self):
        return self.__doctor_assign
    @doctor_assign.setter
    def doctor_assign(self,assign):
        self.__doctor_assign=assign

class Doctor(Person):
    def __init__(self, name, age, gender,doctor_id,specialisation):
        super().__init__(name, age, gender)
        self.__doctor_id=doctor_id
        self.__specialisation=specialisation

    @property
    def doctor_id(self):
        return self.__doctor_id
    @doctor_id.setter
    def doctor_id(self,id):
        self.__doctor_id=id
    
    @property
    def specialisation(self):
        return self.__specialisation
    @specialisation.setter
    def doctor_id(self,s):
        self.__specialisation=s

class Hospital:
    patient_details=[]
    doctor_details=[]
    doctor_wise_patient={}
    def add_new_patient(self,p):
        Hospital.patient_details.append(p)
    def add_new_doctor(self,d):
        Hospital.doctor_details.append(d)
    def book_appoinment(self):
        for d in Hospital.doctor_details:
            patient_list=[]
            for p in Hospital.patient_details:
                if p.doctor_assign==d.name:
                   patient_list.append(p)
            Hospital.doctor_wise_patient[d]=patient_list
    
    def display_details(self):
        for d, patients in Hospital.doctor_wise_patient.items():
            for p in patients:
                print(f"{p.name} is assigned with {d.name}")


p1=Patienet("Hari",21,"male","p10012026","fever","Dr Satya")
p2=Patienet("Ram",56,"male","p10022026","mussel pain","Dr BB")
p3=Patienet("Sriya",35,"female","p10032026","pregnent","Dr Neha")

d1=Doctor("Dr Satya",34,"male","d10012026","Medicine")
d2=Doctor("Dr BB",38,"male","d10022026","Orthologist")
d3=Doctor("Dr Neha",42,"female","d10032026","Gynacologist")

h1=Hospital()
h1.add_new_doctor(d1)
h1.add_new_doctor(d2)
h1.add_new_doctor(d3)

h1.add_new_patient(p1)
h1.add_new_patient(p2)
h1.add_new_patient(p3)
h1.book_appoinment()
h1.display_details()