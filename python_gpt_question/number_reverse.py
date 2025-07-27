number = 392
count = 0


while True:
    str_number = str(number)
    list_n = list(str_number)
    list_m = list_n.copy()

    list_n.sort()
    list_m.sort(reverse=True)

    m = int("".join(list_n))
    n = int("".join(list_m))

    new_number = n - m
    print(f"Step {count+1}: {n} - {m} = {new_number}")
    count += 1

    if new_number == number: # Stop if it becomes a fixed point
        break
    number = new_number

print("Total steps:", count)

 


