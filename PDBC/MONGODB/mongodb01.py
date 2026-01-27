import pymongo as mng

client=mng=mng.MongoClient("127.0.0.1:27017")
print(client.list_database_names())

db=client["employee_fp10"]
print(db.list_collection_names())

