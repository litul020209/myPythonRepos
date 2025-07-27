
def passwordStrength(password):
    # special_char="@#$%&*!"
    u=0
    l=0
    sc=0
    d=0
    if len(password)<8:
        return "weak"
    else:
        for x in password:
            
            if x.isupper():
                
                u=u+1
            elif x.islower():
                 
                 l=l+1
            elif x.isdigit():
                
                d=d+1
            else:
                
                sc=sc+1 #for special character
    
    if ((u>=1) and (l>=1) and (d>=1) and (sc>=1)):

        return "strong"
    else:
        return "weak"


password=input("enter your password: ")
check=passwordStrength(password)

if check=="strong":
   print("your password is a strong password")
else:
    print("your password is a weak password")