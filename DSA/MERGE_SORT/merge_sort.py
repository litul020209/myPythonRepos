# def mergeSort(left,right):
#     ans=[]
#     i=0
#     j=0
#     while i<len(left) and j<len(right):
#           if left[i]<right[j]:
#                ans.append(left[i])
#                i=i+1
#           else:
#                ans.append(left[j])
#                j=j+1
#     ans.extend(left[i:])
#     ans.extend(right[j:])
#     return ans

# def merge(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left_arr=merge(arr[:mid])
#     right_arr=merge(arr[mid:])
    
#     return mergeSort(left_arr,right_arr)
    
# arr=[1,4,5,7,3,9,8]
# print(merge(arr))


def mergeSort(left, right):
    ans = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    ans.extend(left[i:])
    ans.extend(right[j:])
    return ans

def merge(arr):
    if len(arr) <= 1:  # also handle empty array case
        return arr
    mid = len(arr) // 2
    left_arr = merge(arr[:mid])   # store the sorted left half
    right_arr = merge(arr[mid:])  # store the sorted right half
    return mergeSort(left_arr, right_arr)

arr = [1, 4, 5, 7, 3, 9, 8]
print(merge(arr))






