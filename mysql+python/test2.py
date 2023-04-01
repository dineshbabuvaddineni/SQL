import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
cur=mydb.cursor()
cur.execute('select *from fsds.fsds1')

for i in cur:
    print(i)
