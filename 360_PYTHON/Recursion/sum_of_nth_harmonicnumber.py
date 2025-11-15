def sum_of_harmonicnumber(num,sum):
    if num!=0:
        snum=1/num
        sum=sum+snum
        print(f"1/{num}")
        sum_of_harmonicnumber(num-1,sum)
    else:
        print(sum)

num=int(input("num: "))
sum=0
sum_of_harmonicnumber(num,sum)