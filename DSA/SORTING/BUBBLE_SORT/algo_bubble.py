

# numbers = [5, 3, 8, 4, 2, 1, 5, 3]  # Example list


# for i in range(len(numbers) - 1):  
 
#     for j in range(len(numbers) - 1 - i):
       
#         if numbers[j] > numbers[j + 1]:
           
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print("Sorted list:", numbers)
n1=[0,0,0,2,4,5,6]
n2=n1.copy()
for i in range(len(n2)):
    if n2[i]==0:
        n1.remove(0)
    else:
        break
print(n1)