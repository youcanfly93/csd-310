#Joel Mardock
#06/19/2022
#Module 5.3 Assignment: PyTech: Collection Queries

'''This code will connect to the MongoDB database, and insert three records. It will output each record into the terminal as it inserts them in a required format'''


import pymongo
import certifi

#Connect to the PyTech Database
conn_str = "mongodb+srv://admin:admin@cluster0.uj3965s.mongodb.net/pytech?retryWrites=true&w=majority"

client = pymongo.MongoClient(conn_str, tlsCAFile=certifi.where())

db = client.pytech

students = db['students']

#Message Variables
first_insert_message = "Inserted student record"
second_insert_message = "into the students collection with document_id"

#Records to insert
student_1 = {
    "student_id": "1007",
    "first_name": "Mickey",
    "last_name": "Mouse"
}

student_2 = {
   "student_id": "1008",
    "first_name": "Minnie",
    "last_name": "Mouse"
}

student_3 = {
    "student_id": "1009",
    "first_name": "Donald",
    "last_name": "Duck"
}


#Insert Records And Output Results
print("-- INSERT STATEMENTS --")

new_student_id = students.insert_one(student_1).inserted_id
print(f"{first_insert_message} {student_1['first_name']} {student_1['last_name']} {second_insert_message} {new_student_id}")

new_student_id = students.insert_one(student_2).inserted_id
print(f"{first_insert_message} {student_2['first_name']} {student_2['last_name']} {second_insert_message} {new_student_id}")

new_student_id = students.insert_one(student_3).inserted_id
print(f"{first_insert_message} {student_3['first_name']} {student_3['last_name']} {second_insert_message} {new_student_id}")

print("")
print("")
print("End of program, press any key to continue...")
