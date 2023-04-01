import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

print(mydb.is_connected())

cur=mydb.cursor()
# cur.execute("create database fsds")
cur.execute("use fsds")

# cur.execute('create table fsds1(name varchar(40),roll_no int,mail_id varchar(50))')
cur.execute("insert into fsds1 values('Dinesh',3456,'dinesh1234@gmail.com')")

mydb.commit()