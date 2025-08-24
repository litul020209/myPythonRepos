
def one_to_n(n):
    if n<0:
        return
    else:
        one_to_n(n-1)
        print(n)

num=10
print(one_to_n(num))