from functools import reduce as r
try:
   l1=[1,2,3,4,5]
   print(r(lambda x,y: x<y,l1))

except:
   print("logic")