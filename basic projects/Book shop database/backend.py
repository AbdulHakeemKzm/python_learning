import sqlite3

def connect():
	connectdb=sqlite3.connect("books.db")
	curs=connectdb.cursor()
	curs.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
	connectdb.commit()
	connectdb.close()
	
def insert(title, author, year, isbn):
	connectdb=sqlite3.connect("books.db")
	curs=connectdb.cursor()
	curs.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
	connectdb.commit()
	connectdb.close()
	
def view():
	connectdb=sqlite3.connect("books.db")
	curs=connectdb.cursor()
	curs.execute("SELECT * FROM book")
	rows=curs.fetchall()
	connectdb.close()
	return rows

def search(title="", author="", year="", isbn=""):
	connectdb=sqlite3.connect("books.db")
	curs=connectdb.cursor()
	curs.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
	rows=curs.fetchall()
	connectdb.close()
	return rows

def delete(id):	
	connectdb=sqlite3.connect("books.db")
	curs=connectdb.cursor()
	curs.execute("DELETE FROM book WHERE id=?", (id,))
	connectdb.commit()
	connectdb.close()

def update(id, title, author, year, isbn):	
	connectdb=sqlite3.connect("books.db")
	curs=connectdb.cursor()
	curs.execute("UPDATE book SET title= ?,author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
	connectdb.commit()
	connectdb.close()
	
	
connect()

#insert("The sea", "jhon smith", 1918, 913123132)
#delete(3)
#update(2, "The Earth", "jhon Smooth", 1945, 98765432)
print(view())
#print(search(author="jhon smith"))
