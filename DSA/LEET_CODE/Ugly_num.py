num=int(input("enter the number: "))

for i in range(1,num+1):
    if num%i==0:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count=count+1

            if count<2:
                break
            else:
                if count==2:
                    print("the number is not a ugly number")
                else:
                    print("the number is a ugly number")


# class Solution:
#     def isUgly(self, n: int) -> bool:
#         if n<=0:
#             return False
#         multiplier=[]
#         for i in range(1,n+1):
#             if n%i==0:
#                 multiplier.append(i)
#         a=True
#         for x in multiplier:
#             count=0
#             for i in range(1,x+1):
#                 if x%i==0:
#                     count=count+1
#             if count==2:
#                 if x in [2,3,5]:
#                     continue
#                 else:
#                     a=False
#         if a==True:
#             return True
#         else:
#             return False
       
        
        







