# read data drom text02.data file
# import os

# print(os.getcwd())


try:
    with open("FileIO/text02.data","r") as fp:

        # var=fp.read()
        # print(var)
        # print("*" * 50)
        # var=fp.readline()
        # print(var,type(var))
        print("*" * 50)
        var=fp.readlines()
        print(var,type(var))
        print("*" * 50)

        # for x in var:
        #     print(x,end=" ")

except FileNotFoundError:
    print("file path issue")

