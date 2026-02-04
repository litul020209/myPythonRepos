import csv


hnames =   ["ENO","NAME","SAL"]

records =[
         {"ENO":100 ,"NAME":"RS","SAL":4.5 },
         {"ENO":110 ,"NAME":"TR","SAL":6.5 },
         {"ENO":120 ,"NAME":"DR","SAL":2.5 },
         {"ENO":130 ,"NAME":"KV","SAL":2.6},
        ]
          
          
with open("C:\\Users\\HP\\OneDrive\\Desktop\\PYTHON\\360_PYTHON\\Csv\\sample.csv" ,"w") as fp:
    csvwr = csv.DictWriter(fp,fieldnames=hnames)
    csvwr.writeheader()
    csvwr.writerows(records)
    print("OK")