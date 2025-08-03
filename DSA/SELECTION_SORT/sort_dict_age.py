list_d=[
    {"name": "A", "age": 24},
    {"name": "B", "age": 20}
     ]
n=len(list_d)


for i in range(n):
    mn_i=i
    
    for j in range(1,n):
        if list_d[j]["age"]<list_d[mn_i]["age"]:
            mn_i=j
    temp=list_d[mn_i]["age"]
    list_d[mn_i]["age"]=list_d[i]["age"]
    list_d[i]["age"]=temp
           

        
print(list_d)      

