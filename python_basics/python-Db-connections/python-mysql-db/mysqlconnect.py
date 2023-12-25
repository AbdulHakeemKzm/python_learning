import mysql.connector

connect=mysql.connector.connect(
	user="root",
	password="9926",
	host= "localhost",
	database="db",
	auth_plugin="mysql_native_password"
)
cursor=connect.cursor()
query=cursor.execute("SELECT * FROM Client_Master")
results=cursor.fetchall()
print(results)
	



	

