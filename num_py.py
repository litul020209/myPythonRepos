
# +4.50 ✔

# -1.0  ✔

# .5 ✔

# -.7   ✔

# +.4 ✔

# -+4.5  ✖

# 4.08 ✔

# 4.  ✔

n=int(input("n: "))

while n != 0:
    n-=1
    f=input("f: ")
    if f.count(".")  == 1 :
        if f[0] == "+" or f[0] == "-" or f[0] == "." or f[0].isnumeric():
            if f.count("+") >= 2 or f.count("-") >= 2:
                print(False)
                continue
            if  ("+") in f  and  ("-") in f:
                print(False)
                continue
            for x in f:
                if x.isnumeric() or x == (".") or x == ("+") or x == ("-"):
                    pass
                else:
                    print(False)
                    continue
            else:
                print(True)

        else:
            print(False)
                   
    else:
        print(False)

            



# a="+-.4"


# if ("+") in a  and  ("-") in a:
#     print(False)
# else:
#     print(True)

# print(a.count("."))
# lst=a.split(".")
# print(lst)