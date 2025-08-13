list_1=[9, 7, 5, 3, 1, 2, 4, 6, 8]

a=True

while a==True:
      k = 5
      swap=False
      for i in range(k):
          if  list_1[i]>=list_1[i+1]:
               temp=list_1[i+1]
               list_1[i+1]=list_1[i]
               list_1[i]=temp
               swap=True
      k=k-1
      if not swap:
           break
      
print(list_1)


