
list_01 = [1, [4, [6, 8]], 3, [5]]
num = [1,2,3,4,5,6,7,8,9]

maxV = float('-inf')  # Start with very low number

for x in list_01:
    if isinstance(x, int):
        if x > maxV:
            maxV = x
    elif isinstance(x, list):
        for y in x:
            if isinstance(y, int):
                if y > maxV:
                    maxV = y
            elif isinstance(y, list):  # Nested again
                for z in y:
                    if isinstance(z, int) and z > maxV:
                        maxV = z

print("Maximum value:", maxV)

        

