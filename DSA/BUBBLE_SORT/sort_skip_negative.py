list_01 = [5, -1, 4, -3, 2]
a = True

while a == True:
    p1 = 0
    swap = False
    n = len(list_01)

    while p1 < n - 1:
        # Skip negative at p1
        if list_01[p1] < 0:
            p1 += 1
            continue

        p2 = p1 + 1

        # Skip to next non-negative p2
        while p2 < n and list_01[p2] < 0:
            p2 += 1

        if p2 >= n:
            break

        if list_01[p1] > list_01[p2]:
            # Swap values
            temp = list_01[p1]
            list_01[p1] = list_01[p2]
            list_01[p2] = temp
            swap = True

        p1 += 1

    if not swap:
        break

print(list_01)
