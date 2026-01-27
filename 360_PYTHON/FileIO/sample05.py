#random access file

with open("FileIO/text04.data","r") as fp:
    print(f"current pointer position {fp.tell()}")
    data=fp.read(3)
    print(f"current pointer position {fp.tell()}")