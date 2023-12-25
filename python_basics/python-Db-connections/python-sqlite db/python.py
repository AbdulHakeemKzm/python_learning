import sqlite3


def create_table():

	connect=sqlite3.connect("lite.db")
	cursor=connect.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
	connect.commit()
	connect.close()
	

def insert(item, quantity, price):
	connect=sqlite3.connect("lite.db")
	cursor=connect.cursor()
	cursor.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
	connect.commit()
	connect.close()


def view():
	connect=sqlite3.connect("lite.db")
	cursor=connect.cursor()
	cursor.execute("SELECT * FROM store")
	rows=cursor.fetchall()
	connect.close()
	return rows
	
def delete(item):
	connect=sqlite3.connect("lite.db")
	cursor=connect.cursor()
	cursor.execute("DELETE FROM store WHERE item=?",(item,))
	connect.commit()
	connect.close()


def update(quantity, price, item):
	connect=sqlite3.connect("lite.db")
	cursor=connect.cursor()
	cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
	connect.commit()
	connect.close()

	

#insert("Coffee Cup", 10, 5)
#delete("Water Glass")
update(11,6,"Coffee Cup")
print(view())
