letter=["a","b","c","d","e","f","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

n=int(input("enter the number (0-26): "))
d=1
k=8
for i in range(n):
   mid=(i+d)//2
   m=n-1
   print("-"*k)
   for j in range(i+d):
      
      if j<= mid:

         if j==mid:
            print(letter[m],end="-")
           
         else:
            print(letter[m],end="-")
            m=m-1                           
      else:
         m=m+1        
         print(letter[m],end="-")
   k=k-2    
   d=d+1
   print("")






   
