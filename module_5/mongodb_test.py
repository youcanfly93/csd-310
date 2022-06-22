#Joel Mardock
#06-19-2022
#Module 5.2 Assignment

import pymongo
import certifi

conn_str = "mongodb+srv://admin:admin@cluster0.uj3965s.mongodb.net/pytech?retryWrites=true&w=majority"

client = pymongo.MongoClient(conn_str, tlsCAFile=certifi.where())

'''try:
    print("SUCESS")
    print(client.server_info())
except Exception:
    print("Unable to connect")    
'''

db = client.pytech

print(db.list_collection_names())
