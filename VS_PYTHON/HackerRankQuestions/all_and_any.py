# numbers = list(map(int, input("Enter positive numbers: ").split()))
# print(numbers)

# if "12.23".isnumeric():
#     print(True)

x="4"
if "." in x:
    y=x.split(".")
    print(y[1].isnumeric())
else:
    print("no . in here ")
