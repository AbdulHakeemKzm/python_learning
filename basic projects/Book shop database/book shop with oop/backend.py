import sqlite3

class Database: 

	def __init__(self, db):
		self.connectdb=sqlite3.connect(db)
		self.curs=self.connectdb.cursor()
		self.curs.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
		self.connectdb.commit()
		#connectdb.close()
		
	def insert(self, title, author, year, isbn):
		self.curs.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
		self.connectdb.commit()
		
	def view(self):
		self.curs.execute("SELECT * FROM book")
		rows=self.curs.fetchall()
		return rows

	def search(self, title="", author="", year="", isbn=""):
		self.curs.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
		rows=self.curs.fetchall()
		return rows

	def delete(self, id):	
		self.curs.execute("DELETE FROM book WHERE id=?", (id,))
		self.connectdb.commit()
	
	def update(self, id, title, author, year, isbn):	
		self.curs.execute("UPDATE book SET title= ?,author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
		self.connectdb.commit()
	def __del__(self):
		self.connectdb.close()
		

#insert("The sea", "jhon smith", 1918, 913123132)
#delete(3)
#update(2, "The Earth", "jhon Smooth", 1945, 98765432)
#print(view())
#print(search(author="jhon smith"))
