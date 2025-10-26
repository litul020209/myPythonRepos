mat=[[7,9,8,6,3],
     [3,9,4,5,2],
     [8,1,10,4,10],
     [9,5,10,9,6],
     [7,2,4,10,8] ]

if len(mat) %2 == 0:
    sum =0
    p=0
    q=len(mat)-1
    for i in range(len(mat)):
        if i < len(mat)//2:
            sum=sum+mat[i][p]+mat[i][q]
            if i==len(mat)//2-1:
                continue
            p=p+1
            q=q-1
        else:
            sum=sum+mat[i][p]+mat[i][q]
            p=p-1
            q=q+1
else:
    sum=0
    p=0
    q=len(mat)-1
    for i in range(len(mat)):
        if i < len(mat)//2:
            sum=sum+mat[i][p]+mat[i][q]
            if i==len(mat)//2-1:
                    continue
            p=p+1
            q=q-1
        elif i == len(mat)//2:
            sum=sum+mat[i][i]
        else:
            sum=sum+mat[i][p]+mat[i][q]
            p=p-1
            q=q+1

print(sum)                