# read data drom text02.data file

try:
    with open("text02.data","r") as fp:
        var=fp.readlines()
        for x in var:
            print(x,sep="\n")

except :
    print("check the logic first")