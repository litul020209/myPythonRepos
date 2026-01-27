import pymongo as mng

client = mng.MongoClient("mongodb://127.0.0.1:27017")

db = client["employee_fp10"]
col1 = db["mycol1"]

res = col1.update_many({}, {"$inc": {"salary": 10000}})

for d in col1.find({}, {"_id": 0, "salary": 1}):
    print(d["salary"])


# col1.delete_one({" write the id inside here you want to delete"}).

# col1.delete_one({}) #remove all document.

