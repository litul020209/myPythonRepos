from itertools import cycle

c=0

for i in cycle(range(1,10)):
    if c==5:
        break
    print(i)
    c+=1