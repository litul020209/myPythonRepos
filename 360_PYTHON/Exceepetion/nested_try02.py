try:
    a=100
    try:
        if a>=100:
            try:
                b=200
            except:
                
                print("check it")
            else:
                print(a+b)
    except:
        print("check it")
    else:
        print(b)
except:
    print("check it")
else:
    print(b)