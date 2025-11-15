def number_of_digit(num,count):
    if num!=0:
       count+=1
       num=num//10
       number_of_digit(num,count)

    else:
        print(count)
num=int(input("num: "))
count=0
number_of_digit(num,count)