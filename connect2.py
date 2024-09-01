import pymysql

conn = pymysql.connect(
    host="AADVIK-PC",
    user="root",
    password="12345",
    database="sih"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM drone_side_table")

for row in cursor.fetchall():
    print(row)

conn.close()
