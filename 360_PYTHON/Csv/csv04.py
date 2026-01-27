#create csv using python
import csv

head_name=["empno","name","sal"]
records=[
    [100,"Rossum",4.5],
    [200,"Travis",5.6],
    [300,"Dennis",3.4],
    [400,"Strup",4.5],
    [500,"Ritche",6.7]
]

try:
    with open ("Csv/emp.csv","w") as fp:
        csvr=csv.writer(fp)
        csvr.writerow(head_name)
        csvr.writerows(records)

except FileNotFoundError:
    print("File not found")