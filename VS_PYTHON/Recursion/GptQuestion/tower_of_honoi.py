def toh(n,a,b,c):
    if n==1:
        print(f"move this 1st from source {a} to destination ------->  {c}")
        return

    toh(n-1,a,c,b)
    print(f"move this {n} from {a} to  ------->  {c} ")
    toh(n-1,b,a,c)
toh(3,"a","b","c")