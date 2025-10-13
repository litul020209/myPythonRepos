list1 = [10,12,14,17]
list2 = [11,13,18]
ans=[]

for num1 in list1:
    for num2 in list2:
        if num2>num1:
            if num2-num1<=2:
                ans.append((num1,num2))


print(ans)