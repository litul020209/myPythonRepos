list_01=[12,15,23,34,31]
p_s=int(input("enter the pair sum number: "))
a=False
start=1
for x in list_01:
    for y in list_01[start:]:
        if x+y==p_s:
            a=True
        else:
            continue
    start=start+1

if a==True:
    print("pair sum is available")
else:
     print("pair sum is not available")