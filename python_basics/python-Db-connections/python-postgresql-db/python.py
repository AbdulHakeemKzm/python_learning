import psycopg2


def create_table():
	connect=psycopg2.connect("dbname='database1' user='postgres' password='root' host= 'localhost' port='5432'")
	cursor=connect.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
	connect.commit()
	connect.close()
	

def insert(item, quantity, price):
	connect=psycopg2.connect("dbname='database1' user='postgres' password='root' host= 'localhost' port='5432'")
	cursor=connect.cursor()
	#cursor.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
	cursor.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
	connect.commit()
	connect.close()


def view():
	connect=psycopg2.connect("dbname='database1' user='postgres' password='root' host= 'localhost' port='5432'")
	cursor=connect.cursor()
	cursor.execute("SELECT * FROM store")
	rows=cursor.fetchall()
	connect.close()
	return rows
	
def delete(item):
	connect=psycopg2.connect("dbname='database1' user='postgres' password='root' host= 'localhost' port='5432'")
	cursor=connect.cursor()
	cursor.execute("DELETE FROM store WHERE item=%s",(item,))
	connect.commit()
	connect.close()


def update(quantity, price, item):
	connect=psycopg2.connect("dbname='database1' user='postgres' password='root' host= 'localhost' port='5432'")
	cursor=connect.cursor()
	cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
	connect.commit()
	connect.close()

	
create_table()

#insert("Orange", 15, 10)
#delete("Orange")
update(20,50,"Appple")
print(view())
