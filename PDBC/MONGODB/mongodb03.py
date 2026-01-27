import pymongo as mng

client=mng=mng.MongoClient("127.0.0.1:27017")

db=client["employee_fp10"]

col1=db['mycol1']

# for d in col1.find():
#     print(d,type(d))

# for d in col1.find({},{"_id:":0,"name":1}):
#     print(d)


# for d in col1.find({},{"_id:":0,"salary":1}).sort({"salary":-1}):
#     print(d["salary"])


# res=col1.find({},{"_id:":0,"salary":1}).sort({"salary":-1}).limit(3)

# for d in res:
#     print(d["salary"])
        

# res=col1.update_one({"_id":1},{"$set":{"salary":100000}})


res=col1.update_many({},{"$inc":{"salary":10000}})

for d in col1.find({},{"_id:":0,"salary":1}):
    print(d["salary"])