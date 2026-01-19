import mysql.connector
mydb = mysql.connecter.connect(
    host="localhost",
    user="root",
    password="root"
    port=3306,
    database="1_feb_python"
)

cursour = mydb.cursour

que = "insert into student value(%s,%s,%s,%s)"
val = (0,nane,email,)"