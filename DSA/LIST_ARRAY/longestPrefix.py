
strs = ["jlower","llow","fvight"]
length=[]
for x in strs:
    length.append(len(x))
    
print(length)
max_v=max(length)
print(max_v)
i=0
prefix=""
while i<=max_v:
    pl1=""
    pl=""
    pl3=""
    j=0
    if i<=length[j]:
        pl1=strs[j][i]
    j=j+1
    if i<length[j]:
        pl2=strs[j][i]
    j=j+1
    if i<length[j]:
        pl3=strs[j][i]
    if pl1==pl2==pl3:
        prefix=prefix+pl1
        
    else:
        print("there is no prefix")
        break
    i=i+1

print(prefix)

