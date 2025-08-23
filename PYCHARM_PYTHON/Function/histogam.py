def simple_histogram(numbers):

    print("Numbers:", numbers)
    print()


    groups = {}


    for number in numbers:

        group = (number // 10) * 10


        if group not in groups:
            groups[group] = 0


        groups[group] = groups[group] + 1


    print("Histogram:")
    for group in sorted(groups.keys()):
        count = groups[group]
        stars = "*" * count
        print(f"{group}-{group + 9}: {stars} ({count} numbers)")



numbers = [5, 15, 23, 8, 16, 25, 12]
simple_histogram(numbers)

