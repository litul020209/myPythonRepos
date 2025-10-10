list1=["abc","abcd",""," ","   "]
list2=[]
list3=list1
for x in list3:
    if not x:
        continue
    else:
        list2+=[x]
print(list2)

