
def n_to_one(n):
    if n==0:
        print(n)
        return
    else:
        print(n)
        n_to_one(n-1)
num=10
n_to_one(num)