from collections import defaultdict

# Input first line: n (size of group A), m (size of group B)
n, m = map(int, input().split())

# create a defaultdict with list
groupA = defaultdict(list)

# read group A words and store their positions
for i in range(1, n+1):
    word = input().strip()
    groupA[word].append(i)

# read group B words and check in group A
for _ in range(m):
    word = input().strip()
    if word in groupA:
        print(" ".join(map(str, groupA[word])))
    else:
        print(-1)




