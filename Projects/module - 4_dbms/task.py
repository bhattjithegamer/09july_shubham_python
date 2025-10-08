import tkinter
import pymysql

try:
    db = pymysql.connect(host="localhost",user="root",passwd="",database="task")
    print("db conected ")
except Exception as e:
    print(e)

cr = db.cursor()

table = "create table student(id integer primary key auto_increment,name text,city text)"

try:
    cr.execute(table)
    db.commit()
    print("created")
except Exception as e:
    print(e)

screen=tkinter.Tk()
screen.title("Myapp")
screen.geometry("400x400")
screen.config(background="light blue")

tkinter.Label(text = "name",bg="light blue",fg="red",font="bold").place(x=100,y=100)
dname = tkinter.Entry()
dname.place(x=180,y=105)

tkinter.Label(text = "city",bg="light blue",fg="red",font="bold").place(x=100,y=120)
dcity = tkinter.Entry()
dcity.place(x=180,y=125)

def btn():
    name = dname.get()
    city = dcity.get()
    try:
        insert = f"insert into student(name,city) values(%s,%s)"
        cr.execute(insert,(name,city))
        db.commit()
        print("data saved in database!")
    except Exception as e:
        print(e)

tkinter.Button(text="save",fg="red",font="Ebrima 15 bold",command=btn).place(x=200,y=200)
screen.mainloop()

btn()
