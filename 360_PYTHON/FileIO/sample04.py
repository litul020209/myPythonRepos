#program for counting number of lines, character , words of any file.

try:
    with open ("FileIO/text04.data","r") as fp:
        data=fp.read()
        print(len(data))

        data=fp.readlines()
        print(len(data))

        data=fp.readline()
        print(len(data))
except:
    print("check the logic")