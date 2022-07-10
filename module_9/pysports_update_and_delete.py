#Joel Mardock
#07-10-2022
#Module 9.3 Assignment: PySports: Update and Deletes

'''This program will execute a query that inserts a new record, updates it, and deletes it. Each execution will SELECT and display results'''

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



#INSERT Query
cursor.execute("INSERT INTO player(player_id, first_name, last_name, team_id) VALUES('21', 'Smeagol', 'Shire Folk', 1);")



db.commit()


#Display after INSERT
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id")
player = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER INSERT--")
for players in player:
    print("Player ID: {}".format(players[0]))
    print("First Name: {}".format(players[1]))
    print("Last Name: {}".format(players[2]))
    print("Team Name: {}".format(players[3]))
    print("")
print("")
print("Press any key to continue...")  
print("")  





#UPDATE query
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")
db.commit()

#Display after UPDATE
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id")
player = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER UPDATE --")
for players in player:
    print("Player ID: {}".format(players[0]))
    print("First Name: {}".format(players[1]))
    print("Last Name: {}".format(players[2]))
    print("Team Name: {}".format(players[3]))
    print("")
print("")
print("Press any key to continue...")  
print("")  


#DELETE query
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")
db.commit()

#Display after DELETE
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id")
player = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER DELETE --")
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