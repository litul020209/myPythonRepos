from functools import lru_cache

times=0

@lru_cache
def fibbonacii(n):
    global times
    times+=1
    if n==0 or n==1:
        return 1
    return fibbonacii(n-1)+fibbonacii(n-2)

print(fibbonacii(10))
print(times)