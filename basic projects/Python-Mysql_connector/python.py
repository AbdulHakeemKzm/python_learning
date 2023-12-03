import mysql.connector

mysqlconnector = mysql.connector.connect(
user = "uname",
password = "password",
host = "IP",
database = "DBname"
)


cursor = con.cursor()

query = cursor.execute["SELECT * FROM Dictionary"]
results = cursor.fetchall()

print(results)

