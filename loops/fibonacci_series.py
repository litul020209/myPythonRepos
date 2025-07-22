num=int(input("enter the number : "))
preveous_01=0
preveous_02=0
fibo_num=1
for i in range(1,num+1):
    if i==1:
        print(0)
        print(fibo_num)
        preveous_01=fibo_num
    elif i==2:
       print(fibo_num)
       preveous_02=fibo_num
       fibo_num=preveous_02+preveous_01
    else:
       print(fibo_num)
       preveous_01=preveous_02
       preveous_02=fibo_num
       fibo_num=preveous_02+preveous_01

        



       

    