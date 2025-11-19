# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input("n: "))
while n != 0:
    n -= 1
    x = input("float: ")
    if "." not in x:
        print(False)
        continue

    dot_index = x.index(".")
    x1 = x[:dot_index]
    x2 = x[dot_index + 1:]
    if x1[0] in ["+", "-"]:
        if not x1[1:].isnumeric():
            print(False)
            continue

    if x1[0].isdigit():
        if not x1[1:].isnumeric() and not []:
            print(False)
            continue
    if not x1[1:].isnumeric():
        if not x1[1:]:
            print(True)
            continue
        else:
            print(False)
            continue

    else:
        print(True)

