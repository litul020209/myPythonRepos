import json

try:
   with open("sample.json","w") as fp:
        data={"a":1}  #pickling the data in file
        json.dump(data,fp)  
   with open("sample.json","r") as fp:
        data=json.load(fp)
        print(data)
   
except:
    print("Check the logic")
