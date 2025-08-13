marks = {"Math": 75, "English": 85, "Physics": 65}
value=[]
for v in marks.values():
    value.append(v)
n=len(value)

for i in range(n-1):
    m_i=i
    for j in range(1,n):
        if value[m_i]>value[j]:
            m_i=j
    temp=value[m_i]
    value[m_i]=value[i]
    value[i]=temp
dict={}
for x in value:
    for k in marks.keys():
        if marks[k]==x:
            dict[k]=x
            break

print(dict)