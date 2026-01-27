#reading csv files data using csv module

import csv

try:
    with open("Csv/student.csv","r") as fp:
        data=csv.DictReader(fp)
        for record in data:
            for k,v in record.items():
                print(f"{k} ---------> {v}")
            print("-"*30)
except FileNotFoundError:
    print("FIle not found")