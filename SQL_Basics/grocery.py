# Grocery List

import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, aisle INTEGER)')

def data_entry():
	c.execute('INSERT INTO groceries VALUES (1, "Bananas",4, 7)')
	c.execute('INSERT INTO groceries VALUES (2, "Peanut Butter", 1, 2)')
	c.execute('INSERT INTO groceries VALUES (3, "Dark chocolate bars", 2, 2)')
	c.execute('SELECT * FROM groceries')

	conn.commit()
	c.close()
	conn.close()

create_table()
data_entry()
