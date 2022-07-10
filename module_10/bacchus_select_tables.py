#Caleb Rummel, James Bailey, Joel Mardock, Nicholas Werner
#07-10-2022
#Module 10.3 Assignment

'''This script will select all of the data from each table in the "bacchus" database and output it in print lines'''


import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "bacchus_user",
	"password": "bacchus",
	"host": "127.0.0.1",
	"database": "bacchus",
	"raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()


cursor.execute('SELECT * FROM deliveries_log')
cursorVariable = cursor.fetchall()
print("Deliveries_Log" + str(cursor.column_names))
for rows in cursorVariable:
    print(rows[0], rows[1], rows[2], rows[3])

cursor.execute('SELECT * FROM departments')
cursorVariable = cursor.fetchall()
print("Departments"+ str(cursor.column_names))
for rows in cursorVariable:
    print(rows[0], rows[1])

cursor.execute('SELECT * FROM employee')
cursorVariable = cursor.fetchall()
print("Employee"+ str(cursor.column_names))
for rows in cursorVariable:
    print(rows[0], rows[1], rows[2], rows[3])

cursor.execute('SELECT * FROM employee_time')
cursorVariable = cursor.fetchall()
print("Employee_Time"+ str(cursor.column_names))
for rows in cursorVariable:
    print(rows[0], rows[1], rows[2], rows[3])

cursor.execute('SELECT * FROM suppliers')
cursorVariable = cursor.fetchall()
print("Suppliers"+ str(cursor.column_names))
for rows in cursorVariable:
    print(rows[0], rows[1], rows[2], rows[3])

cursor.execute('SELECT * FROM supplies')
cursorVariable = cursor.fetchall()
print("Supplies"+ str(cursor.column_names))
for rows in cursorVariable:
    print(rows[0], rows[1], rows[2])

cursor.execute('SELECT * FROM wine_distribution')
cursorVariable = cursor.fetchall()
print("Wine_Distribution"+ str(cursor.column_names))
for rows in cursorVariable:
    print(rows[0], rows[1], rows[2], rows[3], rows[4])

cursor.close()    
