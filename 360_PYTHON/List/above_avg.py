rain_fall=[12, 15, 8, 20, 18, 25, 10]

avg=sum(rain_fall)/len(rain_fall)

print(avg)

c=0
for num in rain_fall:
    if num>= avg:
        c+=1

print(c)