patient_prioroties=[]
while True:
    n=int(input("Enter the priorities of patient: "))
    patient_prioroties.append(n)
    ans=input("is there any more patient yes/no: ")
    if ans=="no":
        break
res=[]
while True:
    max=0
    for x in patient_prioroties:
        if x>max:
            max=x
    res.append(max)
    patient_prioroties.remove(max)
    if not patient_prioroties:
        break
print(res)


