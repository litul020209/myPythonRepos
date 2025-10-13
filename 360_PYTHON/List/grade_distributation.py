nums=[92,84,76,43,59,89]
ans={"A":0,"B":0,"C":0,"D":0}

for n in nums:
    if n >=85:
       ans["A"]+=1
    elif n >= 70 and n < 85:
        ans["B"]+=1
    elif n >= 50 and n < 70:
        ans["C"]+=1
    else:
        ans["D"]+=1
print(ans)


