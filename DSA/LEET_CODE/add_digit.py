num=int(input("enter the number: "))
a=True
snum=str(num)
while a==True:
      add=0
      for x in snum:
          n=int(x)
          add=add+n
      snum=str(add)
      if len(snum)==1:
          print(snum)
          break
