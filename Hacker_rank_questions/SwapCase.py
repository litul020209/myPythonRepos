
def swap_case(s):
    a="#@$%^&*!.,"
    b=" "
    c=""
    for x in s:
        if x==a:
            c=c+x
        elif x==b:
            c=c+x
            
        else:
            if x.isupper():
                m=x.lower()
                c=c+m
            else:
                n=x.upper()
                c=c+n
        
    return c

s=input("enter the sentence:  ")
print(swap_case(s))