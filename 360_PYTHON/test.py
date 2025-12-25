# import sys
# a=10
# b=20
# c=30
# print(sys.getrefcount(a))
# print(sys.getrefcount(b))
# print(sys.getrefcount(c))
# a1=10
# b1=20
# c1=30
# print(sys.getrefcount(a))
# print(sys.getrefcount(b))
# print(sys.getrefcount(c))

# def print_patient(self):
    #     for o in Hospital.hospital_patient:
    #         print(o.name)
    #         print(o.age)
    #         print(o.gender)
    #         print("-"*7)

# doc={}
# doc["a"]={}
# doc["b"]={}

# print(doc)
# class Hospital:
#     hospital_patient=[]
#     hospital_doctors={
#         "Neurologist":{},
#         "Cardiologist":{},
#         "Medicine":{},
#         "Nephrologist":{},
#         "Oncologist":{},
#         "Hepatologist":{},
#         "Orthologist":{},
#         "Surgeon":{},
#         "Dermatologist":{},
#         "Immunplogist":{},
#         "Gastroenterologist":{},
#         "Ophthalmologist":{},
#         "Endocrinologists":{},
#         "Otolaryngologist":{},
#         "Pulmonologist":{},
#         "Pediatric":{},
#         "Gynecologist":{},
#         "Dentist":{},
#         "Urologist":{}
#     }
    
#     @classmethod
#     def add_doctor(cls,doctor):
#         match doctor.specialisation:
#             case "Neurologist":
#                 Hospital.hospital_doctors["Neurologist"][doctor]=[]
#             case "Cardiologist":
#                 Hospital.hospital_doctors["Cardiologist"][doctor]=[]
#             case "Medicine":
#                 Hospital.hospital_doctors["Medicine"][doctor]=[]
#             case "Oncologist":
#                 Hospital.hospital_doctors["Oncologist"][doctor]=[]
#             case "Hepatologist":
#                 Hospital.hospital_doctors["Hepatologist"][doctor]=[]
#             case "Orthologist":
#                 Hospital.hospital_doctors["Orthologist"][doctor]=[]
#             case "Surgeon":
#                 Hospital.hospital_doctors["Surgeon"][doctor]=[]
#             case "Dermatologist":
#                 Hospital.hospital_doctors["Dermatologist"][doctor]=[]
#             case "Immunplogist":
#                 Hospital.hospital_doctors["Immunplogist"][doctor]=[]
#             case "Gastroenterologist":
#                 Hospital.hospital_doctors["Gastroenterologist"][doctor]=[]
#             case "Ophthalmologist":
#                 Hospital.hospital_doctors["Ophthalmologist"][doctor]=[]
#             case "Endocrinologists":
#                 Hospital.hospital_doctors["Endocrinologists"][doctor]=[]
#             case "Otolaryngologist":
#                 Hospital.hospital_doctors["Otolaryngologist"][doctor]=[]
#             case "Pulmonologist":
#                 Hospital.hospital_doctors["Pulmonologist"][doctor]=[]
#             case "Pediatric":
#                 Hospital.hospital_doctors["Pediatric"][doctor]=[]
#             case "Gynecologist":
#                 Hospital.hospital_doctors["Gynecologist"][doctor]=[]
#             case "Dentist":
#                 Hospital.hospital_doctors["Dentist"][doctor]=[]
#             case "Urologist":
#                 Hospital.hospital_doctors["Urologist"][doctor]=[]
#             case "Nephrologist":
#                 Hospital.hospital_doctors["Nephrologist"][doctor]=[]
#             case _:
#                 print("please check your specialisation")
            
#     @classmethod
#     def add_patient(cls,patient):
#         Hospital.hospital_patient+=[patient]
    
    
#     @classmethod
#     def book_appointment(cls):
#         cls.disease_map = {
#            "Brain"       :      "Neurologist",
#            "Heart"       :      "Cardiologist",
#            "Fever"       :      "Medicine",
#            "Kidney"      :      "Nephrologist",
#            "Cancer"      :      "Oncologist",
#            "Liver"       :      "Hepatologist",
#            "Ortho"       :      "Orthologist" ,
#            "Surgery"     :      "Surgeon",
#            "Skin"        :      "Dermatologist",
#            "Immunity"    :      "Immunplogist",
#            "Stomach"     :      "Gastroenterologist",
#            "Eye"         :      "Ophthalmologist",
#            "Thyroid"     :      "Endocrinologists",
#            "ENT"         :      "Otolaryngologist",
#            "Lungs"       :      "Pulmonologist",
#            "Newborns"    :      "Pediatric",
#            "Pregnancy"   :      "Gynecologist",
#            "Teeth"       :      "Dentist",
#            "Urine"       :      "Urologist"
#         } 
        
#         for  p1 in Hospital.hospital_patient:
#             if p1.doctor_assign==None:
#                 cls.specific_department=p1.disease
#                 while True:
#                     for k in Hospital.hospital_doctors[cls.specific_department]:
#                         if not Hospital.hospital_doctors[cls.specific_department][k]:
#                            Hospital.hospital_doctors[cls.specific_department][k]+=[p1]
                           

                        




        