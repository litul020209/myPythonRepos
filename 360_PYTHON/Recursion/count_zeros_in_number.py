def count_zero(num,count):
    if num!=0:
        digit=num%10
        if digit==0:
            count+=1
        num=num//10
        count_zero(num,count)
    else:
        print(count)

number=int(input("number: "))
count=0
count_zero(number,count)