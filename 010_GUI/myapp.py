from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


root = Tk()
root.geometry("700x500")
root.title("User Registration")



def conn():
    return mysql.connector.connect(
        host="localhost",
        user = "root",
        password="root",
        port=3306,
        database = "1feb_python"
    )

def delete():
    id  =e1.get()
    mydb  =conn()
    cursor = mydb.cursor()
    cursor.execute(f"delete from user where id={id}")
    mydb.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e1.focus_set()
    messagebox.showinfo("success","User Deleted")
    for i in table.get_children():
        table.delete(i)
    show()


def getdata(self):
    rowid = table.selection()[0]
    rdata = table.set(rowid)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e1.insert(0,rdata['Id'])
    e2.insert(0,rdata['Name'])
    e3.insert(0,rdata['Email'])
    e4.insert(0,rdata['Phone'])

def add():
    mydb  =conn()
    cursor = mydb.cursor()
    qry = "insert into user values(%s,%s,%s,%s)"
    val = (e1.get(),e2.get(),e3.get(),e4.get())
    cursor.execute(qry,val)
    mydb.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e1.focus_set()
    messagebox.showinfo("success","Registration success")
    for i in table.get_children():
        table.delete(i)
    show()

def update():
    mydb  =conn()
    cursor = mydb.cursor()
    qry = "update user set name=%s,email=%s,phone=%s where id=%s"
    val = (e2.get(),e3.get(),e4.get(),e1.get())
    cursor.execute(qry,val)
    mydb.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e1.focus_set()
    messagebox.showinfo("success","Update success")
    for i in table.get_children():
        table.delete(i)
    show()


def show():
    mydb  =conn()
    cursor = mydb.cursor()
    cursor.execute("select * from user")
    data = cursor.fetchall()    
    for i,(id,name,email,phone) in enumerate(data,start=1):
        table.insert("",END,values=(id,name,email,phone))
        cid = id
    e1.insert(0,cid+1)

l1 = Label(root,text="Id").place(x=10, y=10)
l2 = Label(root,text="Name").place(x=10,y=40)
l3 = Label(root,text="Email").place(x=10, y=70)
l4 = Label(root,text="Phone").place(x=10,y=100)


e1 = Entry(root)
e1.place(x=100,y=10)
e2 = Entry(root)
e2.place(x=100,y=40)
e3 = Entry(root)
e3.place(x=100,y=70)
e4= Entry(root)
e4.place(x=100,y=100)


b1 = Button(root,text="Add",command=add, height=2,width=7).place(x = 10, y=130)
b2 = Button(root,text="Update",command=update,  height=2,width=7).place(x = 90, y=130)
b3 = Button(root,text="Delete",command=delete, height=2,width=7).place(x = 170, y=130)

cols = ("Id","Name","Email","Phone")
table = ttk.Treeview(root,columns=cols,show="headings")

for col in cols:
    table.heading(col,text=col)
    table.place(x=10,y=200)


show()
table.bind("<Double-Button-1>",getdata)
root.mainloop()