#reading csv files data

try:
    with open("FileIO/student.csv","r") as fp:
        data=fp.read()
        print(data)
except FileNotFoundError:
    print("FIle not found")