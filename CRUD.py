#Algorithm to create a CRUD using python and mysql
#This is not a complete system and will use the prompt as the primary interface

#libraries
import mysql.connector

#Create a local database using mysql
conection = mysql.connector.connect(
    host =  'local',
    user = 'root',
    password = 'pass',
    database = 'table'
)

#cursor to interect with the database
cursor = conection.cursor()

#CRUD start here
#CREATE
#name_cards = "Trafalgar Law"
#numberof_cards = 4
#command = f'INSERT INTO cards (name_cards, numberof_cards) VALUES ("{name_cards}", {numberof_cards})' #use command with '' and no "", this is used for strings
#cursor.execute(command) #execute the command
#conection.commit() #use if you need to edit the database
#result = cursor.fetchall() #use if you need to read the database

#READ
#command = 'SELECT * FROM cards'
#cursor.execute(command) #use if you need to read the database
#result = cursor.fetchall()
#print(result)

#UPDATE
#name_cards = "Monkey D. Luffy"
#command = f'UPDATE cards SET name_cards = "{name_cards}" WHERE name_cards = "Luffy"'
#cursor.execute(command)
#conection.commit()

#DELETE
command = 'DELETE FROM cards WHERE name_cards = "Trafalgar Law"' #set the condition of the deletion
cursor.execute(command)
conection.commit()

#function to sop the program
cursor.close()
conection.close()

