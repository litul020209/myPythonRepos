def err():
    try:
        print("no error")
        
        return "ok"
        
    except:
        print("error")
        return "not ok"
    finally:
        print("i am run before return")


print(err())