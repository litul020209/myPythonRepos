dict={}
n=int(input("enter the total student number: "))
name_list=[]
for i in range(n):
    name=input("enter the student name: ")
    name_list.append(name)

    marks=[]
    for j in range(3):
        score=float(input("enter the  subjects mark: "))
        marks.append(score)

    for x in range(1):
        dict[name]=marks

name_tuple=tuple(name_list)   
know_result=input(f"enter the name you wants that result {name_tuple} : ")
total_mark=0
for k,v in dict.items():
    if k==know_result:
        for m in v:
            total_mark=total_mark+m
    else:
        continue

avg_mark=total_mark/3
student_mark = round(avg_mark, 2)
print(student_mark)
