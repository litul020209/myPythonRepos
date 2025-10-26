list1=[12,14,16,18,15,19]
list2=[14,12,16,13,23,25]

ans=[x  for x in list1 for y in list2 if x==y]

print(ans)