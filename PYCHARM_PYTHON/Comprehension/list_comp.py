
list_1=[1,2,3,4,5]
list_2=[6,7,8,9]

result={i:x+y for i in range(len(list_1)) for x in list_1 for y in list_2}
print(result)