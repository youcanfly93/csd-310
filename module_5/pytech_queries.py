#Joel Mardock
#06/19/2022
#Module 5.3 Assignment: PyTech: Collection Queries

'''This code will connect to the MongoDB database and output all of the stored results, and also a specifically requested result'''

import pymongo
import certifi

#Connect to the PyTech Database
conn_str = "mongodb+srv://admin:admin@cluster0.uj3965s.mongodb.net/pytech?retryWrites=true&w=majority"

client = pymongo.MongoClient(conn_str, tlsCAFile=certifi.where())

db = client.pytech

students = db['students']

docs = students.find({})

#Print All Records Found
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print("")

#Print Specific Record    
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

doc = students.find_one({"student_id":"1008"})
print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")

print("")
print("")
print("End of program, press any key to continue...")