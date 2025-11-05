y=100

def display():
    x=100
    global y
    y+=500
    print(y)
    def display2():
        def  display3():
            global y
            
            x+=100
            y+=200
            print(y)
            # print(x)
        display3()
        # print(x)
    display2()
display()