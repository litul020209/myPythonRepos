arr=[1,1,0,0]

# all to one
cost=0
for i in range(len(arr)):
    if arr[i]==0:
        arr[i]=1
        cost=cost+5
    

print(arr)
print(cost)