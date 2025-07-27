n = int(input("Enter the given number: "))
a = False

temp = n  

while n % 2 == 0:
    n = n // 2

if n == 1:
    a = True

print(a)

if a:
    print("The number is a power of 2")
else:
    print("The number is not a power of 2")

        


