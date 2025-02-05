n=int(input("entr the number: "))
if n%5==0 or n%3==0:
   if n%15==0:
      print("the number is divisible by 15")
   else:
      if n%5==0:
       print("the number is divisible by 5 ")
      else:
         print("the number is div by 3 ")
else:
   print("the number neither div by 5  nor div by  3 ")  
