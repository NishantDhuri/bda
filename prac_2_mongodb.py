#conda install -c anaconda pymongo

import pymongo
mongo_uri = "mongodb://localhost:27017/"
client = pymongo.MongoClient(mongo_uri)
print(client.list_database_names())
db = client.my_database
print(db.list_collection_names())
table=db.books
print(table.count_documents({}))
