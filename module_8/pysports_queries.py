#Joel Mardock
#07-03-2022
#Module 8.3 Assignment: PySports: Table Queries

'''This program will connect to a localhost MySQL database, and run two queries with a formatted output'''


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
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

cursor = db.cursor()

#Execute First Query
cursor.execute("SELECT team_id, team_name, mascot FROM Team")
team = cursor.fetchall()
print("-- DISPLAYING TEAM RECORDS --")
for teams in team:
    print("Team ID: {}".format(teams[0]))
    print("Team Name: {}".format(teams[1]))
    print("Mascot: {}".format(teams[2]))
    print("")


#Execute Second Query
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM Player")
player = cursor.fetchall()
print("-- DISPLAYING PLAYER RECORDS --")
for players in player:
    print("Player ID: {}".format(players[0]))
    print("First Name: {}".format(players[1]))
    print("Last Name: {}".format(players[2]))
    print("Team ID: {}".format(players[3]))
    print("")
print("")
print("Press any key to continue...")  
print("")  

#Close Connection
db.close()