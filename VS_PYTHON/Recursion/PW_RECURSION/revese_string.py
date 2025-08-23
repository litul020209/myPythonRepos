
def rev_str(str_01):
    if not str_01:
        return ""
    return str_01[1:]+str_01[0]



str_01=input("enter the word : ")
print(rev_str(str_01))