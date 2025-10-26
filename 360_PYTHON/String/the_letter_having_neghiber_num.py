s1="1a2b3c4d5ef6g8h"
ans=[]

for i in range(1,len(s1)-1):
    if type(s1[i])==str:
        if s1[i-1].isdigit() and s1[i+1].isdigit():
            ans.append(s1[i])

print(len(ans))