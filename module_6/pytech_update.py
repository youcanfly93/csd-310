#Joel Mardock
#06/24/2022
#Module 6.2 Assignment: Pytech: Updating Documents

'''This program will connect to the pytech database, format and output the records, and then update one of the records and output again'''

import pymongo
import certifi

conn_str = "mongodb+srv://admin:admin@cluster0.uj3965s.mongodb.net/pytech?retryWrites=true&w=majority"

client = pymongo.MongoClient(conn_str, tlsCAFile=certifi.where())

db = client.pytech

students = db['students']

docs = students.find({})

#Print All Records Found
print("")
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print("")

update = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Disney"}})
#Print The Updated Specific Record    
print("-- DISPLAYING UPDATED STUDENT DOCUMENT FROM find_one() QUERY --")

doc = students.find_one({"student_id":"1007"})
print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")

print("")
print("")
print("End of program, press any key to continue...")
print("")
