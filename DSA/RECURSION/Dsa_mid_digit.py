
def mid_digit(num):
    num=f"{num}"
    length=0
    
    for x in num:
        length+=1
    mid=length//2
    if length ==1:
        return num
    else:
        num=num[:mid]+num[mid+1:]
    return mid_digit(num)
       
     
number=int(input("number: "))
print(mid_digit(number))