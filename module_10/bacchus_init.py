#Caleb Rummel, James Bailey, Joel Mardock, Nicholas Werner
#7-10-2022
#Module 10.2 Assignment


import mysql.connector
from mysql.connector import errorcode

config = {
	"user":"root",
    "host":"localhost",
    "password":"admin"
}

#Added connection error code - Joel
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {}" .format(config["user"], config["host"]))
    print("")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

initCurs = db.cursor()

initCurs.execute("DROP DATABASE IF EXISTS bacchus")
initCurs.execute("CREATE DATABASE bacchus")
initCurs.execute("DROP USER IF EXISTS 'bacchus_user'@'localhost';")
initCurs.execute("CREATE USER 'bacchus_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'bacchus';")
initCurs.execute("GRANT ALL PRIVILEGES ON bacchus.* TO'bacchus_user'@'localhost';")
initCurs.execute("USE bacchus")
initCurs.execute("DROP TABLE IF EXISTS employees;")
initCurs.execute("DROP TABLE IF EXISTS departments;")
initCurs.execute("DROP TABLE IF EXISTS supplies;")
initCurs.execute("DROP TABLE IF EXISTS suppliers;")
initCurs.execute("DROP TABLE IF EXISTS employee_time;")
initCurs.execute("DROP TABLE IF EXISTS deliveries_log;")
initCurs.execute("DROP TABLE IF EXISTS wine_distribution;")
initCurs.execute("CREATE TABLE departments (\ndepartment_id INT NOT NULL AUTO_INCREMENT, department_name VARCHAR(30) NOT NULL,\nPRIMARY KEY(department_id)\n);")
initCurs.execute("CREATE TABLE employee (\npersonnel_id INT NOT NULL AUTO_INCREMENT,\nf_name    VARCHAR(20) NOT NULL,\nl_name   VARCHAR(20) NOT NULL,\ndepartment_id INT NOT NULL,\n PRIMARY KEY(personnel_id), CONSTRAINT fk_department\nFOREIGN KEY(department_id) REFERENCES departments(department_id)\n);")
initCurs.execute("CREATE TABLE suppliers (\nsupplier_id INT NOT NULL AUTO_INCREMENT,\nsupplier_name VARCHAR(40) NOT NULL,\nsupplier_address VARCHAR(60) NOT NULL,\nsupplier_contact VARCHAR(20) NOT NULL,\nPRIMARY KEY(supplier_id)\n);")
initCurs.execute("CREATE TABLE supplies (\nitem_id INT NOT NULL AUTO_INCREMENT,\nsupply_name VARCHAR(20) NOT NULL,\nsupplier_id INT NOT NULL,\nPRIMARY KEY(item_id),\nCONSTRAINT fk_suppliers\nFOREIGN KEY(supplier_id)\nREFERENCES suppliers(supplier_id)\n);")

#Added these tables - Joel
initCurs.execute("CREATE TABLE employee_time (record_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,personnel_id INT NOT NULL,work_date date,hours INT)")
initCurs.execute("CREATE TABLE deliveries_log (shipment_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,expected_delivery_date date,actual_delivery_date date,supplier_id INT NOT NULL)")
initCurs.execute("CREATE TABLE wine_distribution (order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,order_date date,wine_name VARCHAR(20), order_units INT NOT NULL,distributor_name VARCHAR(100))")


initCurs.close()

config = {
	"user": "bacchus_user",
	"password": "bacchus",
	"host": "127.0.0.1",
	"database": "bacchus",
	"raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

# INSERT STATEMENTS (added by CRummel)
#Departments
cursor.execute("INSERT INTO departments(department_name) VALUES('Executives');")
cursor.execute("INSERT INTO departments(department_name) VALUES('Finance');")
cursor.execute("INSERT INTO departments(department_name) VALUES('Marketing');")
cursor.execute("INSERT INTO departments(department_name) VALUES('Production');")
cursor.execute("INSERT INTO departments(department_name) VALUES('Distribution');")

#Employees
cursor.execute("INSERT INTO employee(f_name, l_name, department_id) VALUES('Stan', 'Bacchus', 1);")
cursor.execute("INSERT INTO employee(f_name, l_name, department_id) VALUES('Davis', 'Bacchus', 1);")
cursor.execute("INSERT INTO employee(f_name, l_name, department_id) VALUES('Janet', 'Collins', 2);")
cursor.execute("INSERT INTO employee(f_name, l_name, department_id) VALUES('Roz', 'Murphy', 3);")
cursor.execute("INSERT INTO employee(f_name, l_name, department_id) VALUES('Bob', 'Ulrich', 3);")
cursor.execute("INSERT INTO employee(f_name, l_name, department_id) VALUES('Henry', 'Doyle', 4);")
cursor.execute("INSERT INTO employee(f_name, l_name, department_id) VALUES('Maria', 'Costanza', 5);")

#Suppliers
cursor.execute("INSERT INTO suppliers(supplier_name, supplier_address, supplier_contact) VALUES('XYZ Bottling', '123 Seasame Street', 'Jim Morrison');")
cursor.execute("INSERT INTO suppliers(supplier_name, supplier_address, supplier_contact) VALUES('East Coast Paper Products', '1601 Pennsylvania Avenue', 'Burt Macklin');")
cursor.execute("INSERT INTO suppliers(supplier_name, supplier_address, supplier_contact) VALUES('London Flow and Storage Solutions', '221C Baker Street', 'James Potter');")

#Supplies
cursor.execute("INSERT INTO supplies(supply_name, supplier_id) VALUES('Bottles', 1);")
cursor.execute("INSERT INTO supplies(supply_name, supplier_id) VALUES('Corks', 1);")
cursor.execute("INSERT INTO supplies(supply_name, supplier_id) VALUES('Labels', 2);")
cursor.execute("INSERT INTO supplies(supply_name, supplier_id) VALUES('Boxes', 2);")
cursor.execute("INSERT INTO supplies(supply_name, supplier_id) VALUES('Vats', 3);")
cursor.execute("INSERT INTO supplies(supply_name, supplier_id) VALUES('Tubing', 3);")


#Added these inserts - Joel
#Employee_Time
cursor.execute("INSERT INTO employee_time(personnel_id, work_date, hours) VALUES('1', '2022-01-08', '8' );")
cursor.execute("INSERT INTO employee_time(personnel_id, work_date, hours) VALUES('1', '2022-03-09', '8' );")
cursor.execute("INSERT INTO employee_time(personnel_id, work_date, hours) VALUES('2', '2022-06-08', '8' );")
cursor.execute("INSERT INTO employee_time(personnel_id, work_date, hours) VALUES('3', '2022-07-07', '16' );")
cursor.execute("INSERT INTO employee_time(personnel_id, work_date, hours) VALUES('4', '2022-05-08', '4' );")
cursor.execute("INSERT INTO employee_time(personnel_id, work_date, hours) VALUES('3', '2022-01-08', '8' );")

#Deliveries_log
cursor.execute("INSERT INTO deliveries_log(expected_delivery_date, actual_delivery_date, supplier_id) VALUES('2022-01-15', '2022-01-15', '1' );")
cursor.execute("INSERT INTO deliveries_log(expected_delivery_date, actual_delivery_date, supplier_id) VALUES('2022-02-27', '2022-03-10', '3' );")
cursor.execute("INSERT INTO deliveries_log(expected_delivery_date, actual_delivery_date, supplier_id) VALUES('2022-03-19', '2022-03-16', '2' );")
cursor.execute("INSERT INTO deliveries_log(expected_delivery_date, actual_delivery_date, supplier_id) VALUES('2022-04-22', '2022-04-23', '3' );")
cursor.execute("INSERT INTO deliveries_log(expected_delivery_date, actual_delivery_date, supplier_id) VALUES('2022-05-19', '2022-05-19', '2' );")
cursor.execute("INSERT INTO deliveries_log(expected_delivery_date, actual_delivery_date, supplier_id) VALUES('2022-06-18', '2022-06-18', '1' );")

#Wine_Distribution
cursor.execute("INSERT INTO wine_distribution(order_date, wine_name, order_units, distributor_name) VALUES('2022-04-18', 'Cabernet', '445', 'Wine-Not?' );")
cursor.execute("INSERT INTO wine_distribution(order_date, wine_name, order_units, distributor_name) VALUES('2022-03-24', 'Merlot', '245', 'I Heart Wine' );")
cursor.execute("INSERT INTO wine_distribution(order_date, wine_name, order_units, distributor_name) VALUES('2022-02-14', 'Chardonnay', '154', 'Its Wine O Clock Somewhere' );")
cursor.execute("INSERT INTO wine_distribution(order_date, wine_name, order_units, distributor_name) VALUES('2022-07-06', 'Cabernet', '189', 'Wine Time' );")
cursor.execute("INSERT INTO wine_distribution(order_date, wine_name, order_units, distributor_name) VALUES('2022-04-03', 'Merlot', '3000', 'Drunk Inc,' );")
cursor.execute("INSERT INTO wine_distribution(order_date, wine_name, order_units, distributor_name) VALUES('2022-07-28', 'Chardonnay', '254', 'Wine and Dine' );")


db.commit()

cursor.close()