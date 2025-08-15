s="abcde"
s_list=list(s)
goal = "abced"
g_list=list(goal)
if s==goal:
    print(True)
max_r=len(s)

a=False
for i in range(max_r-1):
    
    s_list.append(s_list[0])
    s_list.pop(0)
    if s_list==g_list:
        a=True
        break
print(a)
    
    