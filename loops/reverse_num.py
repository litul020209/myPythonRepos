num=int(input("Enter the number : "))
reminder=0
reverse_num_str=""
while num>=1:
    reminder=num%10
    num=num//10
    str_reminder=str(reminder)
    reverse_num_str=reverse_num_str+str_reminder
reverse_num=int(reverse_num_str)
print(reverse_num)