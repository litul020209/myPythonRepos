# def replace(line):
    
#     ans=line.replace(" ","-")
#     return ans


def  split_and_join(line):
     x=line.split(" ")
     
     y="-".join(x)
     
     return y


    
line ="this is a string"
result =split_and_join(line)
print(result)