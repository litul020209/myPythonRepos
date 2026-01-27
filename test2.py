
m=int(input("enter the row number: "))
n=int(input("enter the column number: "))

total_element=m*n

l=[]
i=1

while total_element != 0:
     l.append(int(input(f"num {i}: "))) 
     i+=1
     total_element -=1
matrix=[]
r=[]
for x in l:
    r.append(x)
    if len(r)==m:
       matrix.append(r)
       r=[]

max_row=sum(matrix[0])
for i in range(1,len(matrix)):
    if max_row < sum(matrix[i]):
        max_row=sum(matrix[i])
max_column=0

for i in range(n):
    s=0
    for j in matrix:
        s=s+j[i]
    if max_column < s:
         max_column=s
print(max_row, max_column)