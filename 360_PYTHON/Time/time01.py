import time as t
s=t.perf_counter()

s=int(input("s: "))
e=int(input("e: "))

for i in range(s,e+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if i !=1:
           print(i)

e=t.perf_counter()
print(f"{e-s}")

