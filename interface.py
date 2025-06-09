import tkinter as tk
import mysql.connector
import pandas as pd

#Create a local database using mysql
connection = mysql.connector.connect(
    host =  'localhost',
    user = 'root',
    password = 'pass',
    database = 'crud_init'
)

#cursor to interect with the database
#cursor = connection.cursor()

#executing the action to create the table
    #variable sql_table is created to easy the process if we need to call it later
#sql_table = """CREATE TABLE collection (
    #card_collection text,
    #card_number text,
    #card_cost text,
    #card_name text,
    #card_function text,
    #card_color text,
    #card_type1 text,
    #card_type2 text,
    #card_type3 text,
    #card_rarity text
#)"""

#cursor.execute(sql_table) #executing the variable sql_table to create the table "collection"

#commiting the changes to the database
#connection.commit()

#closing connection
#connection.close()

#adding function for the buttons
def add_card():
    #Connect to the local database
    connection = mysql.connector.connect(
        host =  'localhost',
        user = 'root',
        password = 'pass',
        database = 'crud_init'
    )

    #cursor to interect with the database
    cursor = connection.cursor()

    #executing the action to insert information on the table
    cursor.execute("INSERT INTO collection (card_collection, card_number, card_cost, card_name, card_function, card_color, card_type1, card_type2, card_type3, card_rarity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
    (
        entry_collection.get(),
        entry_number.get(), 
        entry_cost.get(),
        entry_name.get(),
        entry_function.get(),
        entry_color.get(),
        entry_type1.get(),
        entry_type2.get(),
        entry_type3.get(),
        entry_rarity.get()
    )
    )

    #commiting the changes to the database
    connection.commit()

    #closing connection
    connection.close()

def export_table():
    #Connect to the local database
    connection = mysql.connector.connect(
        host =  'localhost',
        user = 'root',
        password = 'pass',
        database = 'crud_init'
    )

    #cursor to interect with the database
    cursor = connection.cursor()

    #executing the action to insert information on the table
    cursor.execute("SELECT * FROM collection")
    cards_data = cursor.fetchall() #getting all the data from the database

    #creating a dataframa
    cards_data = pd.DataFrame(cards_data, columns = ['Card Collection', 'Card Number', 'Card Cost', 'Card Name', 'Card Function', 'Card Color', 'First Card Type', 'Second Card Type', 'Third Card Type', 'Card Rarity'])
    cards_data.to_excel('card_collection.xlsx')

    #commiting the changes to the database
    connection.commit()

    #closing connection
    connection.close()

#creating the interface
#window
window = tk.Tk()

#window title
window.title('Card Collection Table')

#labels
label_collection = tk.Label(window, text = 'Card Collection:')
label_collection.grid(row = 0, column = 0, padx = 10, pady = 10)

label_number = tk.Label(window, text = 'Card Number:')
label_number.grid(row = 1, column = 0, padx = 10, pady = 10)

label_cost = tk.Label(window, text = 'Card Cost:')
label_cost.grid(row = 2, column = 0, padx = 10, pady = 10)

label_name = tk.Label(window, text = 'Card Name:')
label_name.grid(row = 3, column = 0, padx = 10, pady = 10)

label_function = tk.Label(window, text = 'Card Function:')
label_function.grid(row = 4, column = 0, padx = 10, pady = 10)

label_color = tk.Label(window, text = 'Card Color:')
label_color.grid(row = 5, column = 0, padx = 10, pady = 10)

label_type1 = tk.Label(window, text = 'First Card Type:')
label_type1.grid(row = 6, column = 0, padx = 10, pady = 10)

label_type2 = tk.Label(window, text = 'Second Card Type:')
label_type2.grid(row = 7, column = 0, padx = 10, pady = 10)

label_type3 = tk.Label(window, text = 'Third Card Type:')
label_type3.grid(row = 8, column = 0, padx = 10, pady = 10)

label_rarity = tk.Label(window, text = 'Card Rarity:')
label_rarity.grid(row = 9, column = 0, padx = 10, pady = 10)

#entries
entry_collection = tk.Entry(window, text = 'Card Collection:', width = 30)
entry_collection.grid(row = 0, column = 1, padx = 10, pady = 10)

entry_number = tk.Entry(window, text = 'Card Number:', width = 30)
entry_number.grid(row = 1, column = 1, padx = 10, pady = 10)

entry_cost = tk.Entry(window, text = 'Card Cost:', width = 30)
entry_cost.grid(row = 2, column = 1, padx = 10, pady = 10)

entry_name = tk.Entry(window, text = 'Card Name:', width = 30)
entry_name.grid(row = 3, column = 1, padx = 10, pady = 10)

entry_function = tk.Entry(window, text = 'Card Function:', width = 30)
entry_function.grid(row = 4, column = 1, padx = 10, pady = 10)

entry_color = tk.Entry(window, text = 'Card Color:', width = 30)
entry_color.grid(row = 5, column = 1, padx = 10, pady = 10)

entry_type1 = tk.Entry(window, text = 'First Card Type:', width = 30)
entry_type1.grid(row = 6, column = 1, padx = 10, pady = 10)

entry_type2 = tk.Entry(window, text = 'Second Card Type:', width = 30)
entry_type2.grid(row = 7, column = 1, padx = 10, pady = 10)

entry_type3 = tk.Entry(window, text = 'Third Card Type:', width = 30)
entry_type3.grid(row = 8, column = 1, padx = 10, pady = 10)

entry_rarity = tk.Entry(window, text = 'Card Rarity:', width = 30)
entry_rarity.grid(row = 9, column = 1, padx = 10, pady = 10)

#buttons
button_add = tk.Button(window, text = 'ADD CARD', command = add_card)
button_add.grid(row = 10, column = 0, padx = 10, pady = 10, columnspan = 2, ipadx = 41)

button_export = tk.Button(window, text = 'EXPORT TABLE', command = export_table)
button_export.grid(row = 11, column = 0, padx = 10, pady = 10, columnspan = 2, ipadx = 30)


window.mainloop()