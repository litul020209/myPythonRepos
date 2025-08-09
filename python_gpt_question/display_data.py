s1 = [("John", 85), ("Alice", 92), ("Bob", 85), ("Daisy", 100),("Alice", 92)]
s2=[]
for x in s1:
    y=list(x)
    s2.append(y)


s3=[]
for x in s2:
    for y in x:
        if isinstance(y,(int)):
           s3.append(y)
            

s4=set(s3)
s3=list(s4)
s3.sort(reverse=True)

for w in s3:
    ans=[]
    for i in range(len(s1)):
        
        if s1[i][1]==w:
            ans.append(s1[i][0])
    print(f"{w} --> {ans}")        



