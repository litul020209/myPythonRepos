s = "abcdefg"
k = 2
tl=k*2
str_box=[]
while True:
    l=s[:tl]
    str_box.append(l)
    s=s[tl:]
    if not s:
        break
ans_list=[]
for w in str_box:
    x=w[:k]
    x=x[::-1]
    ans=w.replace(w[:k],x)
    ans_list.append(ans)
result= "".join(ans_list)
print(result)
    
      

      