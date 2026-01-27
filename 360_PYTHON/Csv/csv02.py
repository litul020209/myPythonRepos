#reading csv files data using csv module

import csv

try:
    with open("FileIO/student.csv","r") as fp:
        data=csv.reader(fp)
        for record in data:
            for val in record:
                print(val,end=" ")
            print()
except FileNotFoundError:
    print("FIle not found")