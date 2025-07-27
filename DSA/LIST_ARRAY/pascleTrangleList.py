def pascal_triangle(n):
    ans_list=[]
    for i in range(n):
        num = 1
        list_01=[]
        for j in range(i + 1):
            list_01.append(num)
            num = num * (i - j) // (j + 1)
        ans_list.append(list_01)
    if i==(n-1):
        return ans_list


rows = int(input("Enter number of rows: "))
print(pascal_triangle(rows))

