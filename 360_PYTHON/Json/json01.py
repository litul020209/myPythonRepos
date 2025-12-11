import json
try:
    d1={1:"a",2:"2",3:"c"}
    d1=json.dumbs(d1)
    print(d1)
    print(type(d1))

    d1=json.loads(d1)
    print(d1)
    print(type(d1))
except:
    print("check logic")
