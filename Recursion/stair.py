def possible(number):
    
    if(number==1):return 1
    if(number==2):return 1
    if(number==3):return 1
    possible_ways=possible(number-1)+possible(number-2)+possible(number-3)
    return possible_ways






number=int(input("enter the stair :  "))
print(possible(number))

