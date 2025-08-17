s = "a-bC-dEf-ghIj"

l_s=list(s)
print(l_s)
l_s.reverse()
print(l_s)

s2="".join(l_s)
s3=""
for x in s2:
    if x.isalpha():
        s3=s3+x
s4=list(s3)
print(s4)
for i in range(len(s)):
    if s[i].isalpha():
        continue
    else:
        s4.insert(i,s[i])
print(s4)
ans="".join(s4)
print(ans)