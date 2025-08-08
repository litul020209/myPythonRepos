def solve(n):
    if n==0:
        return 
    solve(n-1)
    print(n)
    solve(n-1)

print(solve(n=3))