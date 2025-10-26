arr=[4,2,1,3]
new_arr=arr.copy()
diff=[]
for i in range(len(arr)):
    demo_diff=[]
    for j in range(i+1,len(arr)):
        if max(arr)==arr[i]:
            break
        else:
            if arr[i] < arr[j]:
                d=arr[j] - arr[i]
                demo_diff.append(d)
    if len(demo_diff)>=1:
        min1=min(demo_diff)
    diff.append(min1)
d=min(diff)
    
ans=[]
for x in new_arr:
    for y in new_arr:
        if x != y:
            if y-x==d:
                ans.append([x,y])
                break

f_ans=[]
for x in ans:
    f_ans.append(x[0])
f_ans.sort()
new_ans=[]

for x in f_ans:
    for y in ans:
        if x==y[0]:
            new_ans.append(y)
            break

print(new_ans)


