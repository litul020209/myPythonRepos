def pascal_triangle(n):
    for i in range(n):
        # Print spaces for formatting (optional for pyramid shape)
        print(" " * (n - i), end="")

        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            # Update number using formula: nCr = nC(r-1) * (n - r + 1) // r
            num = num * (i - j) // (j + 1)
        print()

# Example usage:
rows = int(input("Enter number of rows: "))
pascal_triangle(rows)
