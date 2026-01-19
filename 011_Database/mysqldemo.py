import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="1feb_python"
)

cursor = mydb.cursor()

# cursor.execute("create database python_sql")

# cursor.execute("create table student(id int primary key, name varchar(20), email varchar(50))")
#cursor.execute("insert into student values(2,'Sagar','sagar@gmail.com')")



cursor.execute("select * from emp")

for std in cursor.fetchall():
    for st in std:
        print(st,end=" ")
    print()

# mydb.execute("delete from student where id=2")

# mydb.commit()