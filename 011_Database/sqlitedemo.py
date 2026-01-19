import sqlite3


mydb = sqlite3.connect("data.db")

# mydb.execute("create table student(id int primary key, name varchar(20), email varchar(50))")

# mydb.execute("insert into student values(2,'Sagar','sagar@gmail.com')")

# mydb.execute("update student set email='sagar@yahoo.com' where id=2")

# data = mydb.execute("select * from student")

# for std in data.fetchall():
#     for st in std:
#         print(st,end=" ")
#     print()

# mydb.execute("delete from student where id=2")

mydb.commit()