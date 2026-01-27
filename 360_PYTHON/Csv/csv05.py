#adding row to a existing csv using python

import csv

record=[600,"KVR",1.5]
try:
    with open ("Csv/emp.csv","a") as fp:
        csvr=csv.writer(fp)
        csvr.writerow(record)

except FileNotFoundError:
    print("File not found")