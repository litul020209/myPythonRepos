str_01="qA2"
ans=True if str_01.isalnum() else False
print(ans)
ans1=False
for x in str_01:
    if x.isalpha():
        ans1=True
        break

ans2=False
for x in str_01:
    if x.isdigit():
        ans2=True
        break

ans3=False
for x in str_01:
    if x.isupper():
        ans3=True
        break

ans4=False
for x in str_01:
    if x.lower():
        ans4=True
        break
    
print(ans)
print(ans1)
print(ans2)
print(ans3)
print(ans4)