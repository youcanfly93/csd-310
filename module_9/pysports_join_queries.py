#Joel Mardock
#07-10-2022
#Module 9.2 Assignment: PySports: Basic Table Joins

'''This program will execute a query that joins two tables together on the pysports database and output the results'''

import mysql.connector
from mysql.connector import errorcode

#Values for DB connection
config = {
    "user": "pysports_user",
    "password": "seasprite",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#Check Connection
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}" .format(config["user"], config["host"], config["database"]))
    print("")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

cursor = db.cursor()

#Execute Query
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
player = cursor.fetchall()
print("-- DISPLAYING PLAYER RECORDS --")
for players in player:
    print("Player ID: {}".format(players[0]))
    print("First Name: {}".format(players[1]))
    print("Last Name: {}".format(players[2]))
    print("Team Name: {}".format(players[3]))
    print("")
print("")
print("Press any key to continue...")  
print("")  

#Close Connection
db.close()