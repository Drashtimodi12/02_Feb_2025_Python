from tkinter import *
import mysql.connector

root = Tk()
root.geometry("500x500")

# b1 = Button(text="Add").pack(side=LEFT)
# b2 = Button(text="Sub").pack(side=RIGHT)
# b3 = Button(text="Mul").pack(side=TOP)
# b4 = Button(text="Div").pack(side=BOTTOM)


# l1 = Label(text="Username").grid(row=1,column=1)
# l2 = Label(text="Email").grid(row=2,column=1)
# l3 = Label(text="Password").grid(row=3,column=1)

# e1 = Entry()
# e1.grid(row=1,column=2)
# e2 = Entry()
# e2.grid(row=2,column=2)
# e3 = Entry()
# e3.grid(row=3,column=2)

# Button(text="submit").grid(row=4,column=2)


def adddata():
    name = e1.get()
    email = e2.get()
    password = e3.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        database="1feb_python"
    )
    cursor = mydb.cursor()

    # cursor.execute(f"insert into student values(0,'{name}','{email}','{password}')")
    qry = "insert into student values(%s,%s,%s,%s)"
    val = (0,name,email,password)
    cursor.execute(qry,val)
    mydb.commit()

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)


l1 = Label(text="Username").place(x=100,y=100)
l2 = Label(text="Email").place(x=100,y=150)
l3 = Label(text="Password").place(x=100,y=200)

e1 = Entry()
e1.place(x=200,y=100)
e2 = Entry()
e2.place(x=200,y=150)
e3 = Entry()
e3.place(x=200,y=200)

Button(text="submit",command=adddata,width=15).place(x=200,y=250)

root.mainloop()

