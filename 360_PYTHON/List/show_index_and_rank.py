ranks= [90, 70, 80, 60]         # Output: [(0,1),(2,2),(1,3),(3,4)] 
copy_rank=ranks.copy()            
ranks.sort(reverse=True)
ans=[]
rank=1
for num in ranks:
    ans.append((copy_rank.index(num),rank))
    rank+=1
print(ans)


    

