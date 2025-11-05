x=100
def check():
    x=10
    print(x)
    def check2():
        global x
        x+=100
        print(x)
    check2()
check()
print(x)