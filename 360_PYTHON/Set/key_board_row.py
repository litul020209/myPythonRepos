words =["asdfghjkl","qwertyuiop","zxcvbnm"]
k1={"q","w","e","r","t","y","u","i","o","p"}
k2={"a","s","d","f","g","h","j","k","l"}
k3={"z","x","c","v","b","n","m"}
l1=[k1,k2,k3]
ans=[]
for i in range(len(words)):
    x=words[i]
    x=x.lower()
    x=set(x)
    for k in l1:
        if x < k:
            ans.append(words[i])
            break
print(ans)