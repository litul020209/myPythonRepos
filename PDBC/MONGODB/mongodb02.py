import pymongo as mng

client=mng=mng.MongoClient("127.0.0.1:27017")

db=client["employee_fp10"]

col1=db['mycol1']

print(type(col1))
# col1.insert_one({"_id":1,"name":"raj","salary":10000})



# col1.insert_many([{"_id":2,"name":"kiran","salary":20000},
#                   {"_id":3,"name":"karan","salary":30000},
#                   {"_id":4,"name":"kumar","salary":40000},
#                   {"_id":5,"name":"mohan","salary":50000}])

# for d in col1.find():
#     print(d,type(d))

# for d in col1.find({},{"_id:":0,"name":1}):
#     print(d)


# for d in col1.find({},{"_id:":0,"salary":1}).sort({"salary":-1}):
#     print(d["salary"])


res=col1.find({},{"_id:":0,"salary":1}).sort({"salary":-1}).limit(3)

for d in res:
    print(d["salary"])