nums = [0,1,0,1,0,1,1,0,1]
if len(nums)==0:
    print( 0 )
if len(nums)==1:
    if nums[0]==1:
        print( 1 )
    else:
        print( 0 )
        
p1=0
p2=1
ans=[]
count=0
while True:
    if nums[p1]==1:
        count=count+1
        if nums[p1]==nums[p2]==1:
            
            p1=p2
            p2=p2+1
        else:
            ans.append(count)
            p1=p2
            p2=p2+1
            count=0
    else:
        ans.append(count)
        p1=p2
        p2=p2+1
        count=0
    if p2>=len(nums):
        if nums[p1]==0:
            ans.append(count)
        else:
           ans.append(count+1)
        break    
print(ans)



