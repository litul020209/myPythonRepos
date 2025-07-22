n=int(input("enter the total student: "))
student=[]
for i in range(n):
    name=input("enter the student name: ")
    mark=float(input("enter the mark of the given student: "))
    grade=[]
    for j in range(1):
        grade.append(name)
        grade.append(mark)
    student.append(grade)

result=[]
for x in student:
    for y in x:
        if isinstance(y, str) and y.isalpha():
            continue
        else:
            result.append(y)
            

result.sort()

min1=result[0]

for i in range(len(result)):
   if result[0]==min1:
       del result[0]
   else:
       continue
min2=result[0]
  

for x in student:
    for y in x:
        if isinstance(y,float):
            if y==min2:
                for i in x:
                    if isinstance(i,str):
                        print(i)
                    else:
                        continue

            else:
                continue
        else:
            continue
