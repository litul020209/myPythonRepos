n = int(input("enter the rows:"))  # You can adjust the number of rows as needed

for i in range(1, n + 1):
    # Inner loop for each row
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print() 