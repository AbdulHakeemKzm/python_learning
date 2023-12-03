import mysql.connector

mysqlconnector = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1databasse"
)

cursor = con.cursor()

query = cursor.execute["SELECT * FROM Dictionary"]
results = cursor.fetchall()

print(results)

