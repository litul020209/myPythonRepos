range_1=int(input("Enter the 1st number: "))
range_2=int(input("Enter the 2nd number: "))

for i in range(range_1,range_2):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count>2:
            continue
    else:
            print(i)
           
        

    