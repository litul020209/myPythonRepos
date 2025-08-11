list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
ans=[]
for i in list_a:
    
    for j in list_b:
        l=[]
        l.append(i)
        l.append(j)      
        tuple_ans=tuple(l)
        ans.append(tuple_ans)
print(ans)