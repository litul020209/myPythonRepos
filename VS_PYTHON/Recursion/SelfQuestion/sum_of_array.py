# def sumOfArray(arr_01):
#     sum=0
#     for i in arr_01:
#         sum=sum+i           #THIS IS USING FOR LOOP
#     print(sum)

# arr_01=[1,4,7,9,5]
# print(sumOfArray(arr_01))


#USING RESURSION

def sumArr(arr_01,sum):
    i=0
    if not arr_01:
        return sum
    sum=sum+arr_01[i]
    i=i+1
    return sumArr(arr_01[i:],sum)

add=sumArr([1,2,3,4,5,6,7,8,9],0)
print(add)