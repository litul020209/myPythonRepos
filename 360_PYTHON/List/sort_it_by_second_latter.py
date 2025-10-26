fruits=["apple","banana","orange","kiwi"]



copy_list=[x[1] for x in fruits]

copy_list.sort()

print(copy_list)

ans=[y for x in copy_list for y in fruits if x==y[1]]
print(ans)