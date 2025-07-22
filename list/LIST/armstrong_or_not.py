num=int(input("enter the number : "))
num_str=str(num)
pwr=len(num_str)
ans=0
for x in num_str:
    n=int(x)
    p=n**pwr
    ans=ans+p

if ans==num:
    print(f"the {num} is a armstrong number ")
else:
    print(f"the {num} is not a armstrong number ")