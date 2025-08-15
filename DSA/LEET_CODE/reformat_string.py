from itertools import permutations

s = "a0b1c2"
if s.isalnum():
   if len(s)%2==0:
      l_s=list(s)
      l_s.sort()
      mid=(len(l_s)-1)//2
      if isinstance(l_s[mid],int):
        perms = permutations(s)
        for p in perms:
            w=''.join(p)
            x=list(w)
            p1=0
            p2=len(w)-1
            while p1 <=len(w)//2:
               if (x[p1].isalpha and x[p2].isdigit) or (x[p1].isdigit and x[p2].isalpha):
                  p1=p1+1
                  p2=p2-1

         
             
         
   

      
   
    

