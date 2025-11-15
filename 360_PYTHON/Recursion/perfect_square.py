def is_perfect_square(n, i=1):

    if i * i == n:
        return True
    if i * i > n:
        return False

    return is_perfect_square(n, i + 1)

n=int(input("n: "))
print(is_perfect_square(n, i=1))