
def sumList(list_01):
    if not list_01:
        return 0
    return list_01[0]+sumList(list_01[1:])

list_01=[2,3,7,5,8,9]
print(sumList(list_01))

