# First line: integer
n = int(input())

# Second line: n space-separated integers → convert to list of int
list1 = set(map(int, input().split()))

# Third line: integer
m = int(input())

# Fourth line: m space-separated integers → convert to list of int
list2 = set(map(int, input().split()))

print("n =", n)
print("list1 =", list1)
print("m =", m)
print("list2 =", list2)