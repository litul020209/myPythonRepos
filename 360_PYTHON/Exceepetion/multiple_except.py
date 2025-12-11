try:
    a=int(input("a: "))
    b=int(input("b: "))
    res=a/b
    l1=[1,2,3,4]
    print(l1[9])
    d={1:2,3:4,5:6}
    print(d[10])
    
    
except ValueError:
    print("give the intger value for a and b!")
except ZeroDivisionError:
    print("b never be zero!")
except IndexError:
    print("The index is not found in the l1 list!")
except KeyError:
    print("Check the key ")
except:
    print("check the code properly")

else:
    print(res)