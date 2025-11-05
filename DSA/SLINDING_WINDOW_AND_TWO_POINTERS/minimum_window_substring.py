s="ADOBECODEBANC"
t="ABC"
k=len(t)
a=False
while k <= len(s):
    l=0
    r=k
    while r <= len(s):
        s1=s[l:r]
        if all(t.count(c) <= s1.count(c) for c in set(t)):
            print(s1)
            a=True
            break
        l+=1
        r+=1
    if a:
        break
    k+=1