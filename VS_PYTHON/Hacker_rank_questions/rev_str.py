strs="Hey Litul ARe You Ha$ppY Wi% & This \"Pytho&n\" yuU"
unicode="!@#$%^&*(){}:;," ""
for x in strs:
    if x in unicode:
        print(x,end="")
    elif x.isupper():
        print(x.lower(),end="")
    elif x.islower():
        print(x.upper(),end="")
        
