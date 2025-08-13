arr=[2,1,0,0,5,4,3,4,2,1,2,3,3]
m=max(arr)
freq=[]
finish=[]
for i in range(len(arr)):
    key=arr[i]
    count=1
    for j in range(i+1,len(arr)):

        if key==arr[j]:
            count=count+1    
    if key in finish:
        continue
    else:
       finish.append(key)
       freq.append(count)

print(finish)
print(freq)
