#Joel Mardock
#06/26/2022
#Module 6.3 Assignment: Pytech: Deleting Documents

'''This program will connect to the pytech database, format and output the document, add a new document, display all 
documents, delete that document, and display all documents again'''

import pymongo
import certifi

conn_str = "mongodb+srv://admin:admin@cluster0.uj3965s.mongodb.net/pytech?retryWrites=true&w=majority"

client = pymongo.MongoClient(conn_str, tlsCAFile=certifi.where())

db = client.pytech

students = db['students']

docs = students.find({})

#Print All Documents Found
print("")
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print("")



#Message Variables
first_insert_message = "Inserted student record"
second_insert_message = "into the students collection with document_id"

#Records to insert
student_1 = {
    "student_id": "1010",
    "first_name": "Goofy",
    "last_name": "Goof"
}

#Insert Document And Output Results
print("")
print("-- INSERT STATEMENTS --")

new_student_id = students.insert_one(student_1).inserted_id
print(f"{first_insert_message} {student_1['student_id']} {second_insert_message} {new_student_id}")
print("")

docs = students.find({})
#Print All Documents Found
print("")
print("-- DISPLAYING NEW STUDENT LIST DOC --")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print("")


#Delete Document
students.delete_one({"student_id": "1010"})
docs = students.find({})

#Print All Documents Found
print("")
print("-- DELETED STUDENT ID: 1010 --")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print("")

print("")
print("")
print("End of program, press any key to continue...")
print("Terminated with exit code 0.")
print("")