list_01=[5,7,8,9,12,14,16]
target=17
last=len(list_01)-1
# print(list_01[0]+list_01[last])
for i in range(len(list_01)):
    if (list_01[i]+list_01[last]) == target:
        print(i,last)
    last=last-1