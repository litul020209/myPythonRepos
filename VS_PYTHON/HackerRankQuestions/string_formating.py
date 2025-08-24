n=int(input("enter the number : "))

for i in range(1,n+1):
    binary = bin(i)[2:]
    octal = oct(i)[2:]
    hexadecimal = hex(i)[2:]
    print(i,end=" ")
    print(octal,end=" ")
    print(hexadecimal,end=" ")
    print(binary,end="")
    print("\n")