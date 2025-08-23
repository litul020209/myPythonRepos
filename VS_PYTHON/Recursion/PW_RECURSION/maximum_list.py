
def maximum_list(list_01,max):
    if not list_01:
        return max
    if list_01[0]>=max:
        max=list_01[0]
    return maximum_list(list_01[1:],max)

list_01=[4,5,8,12,6,9]
max=0
print(maximum_list(list_01,max))

