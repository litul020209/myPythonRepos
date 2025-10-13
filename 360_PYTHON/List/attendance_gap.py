attendance= [0]
if 0 not in attendance:
    print([])
else:
    ans=[]
    c=1
    p=0
    q=1
    while q<len(attendance):
        if attendance[p]==0:
            if attendance[q]==0:
                c+=1
                q+=1
            else:
                ans.append(c)
                c=1
                p=q
                q=q+1
        else:
            p=q
            q=q+1
    if attendance[p]==0:       
        ans.append(c)
    print(ans)


