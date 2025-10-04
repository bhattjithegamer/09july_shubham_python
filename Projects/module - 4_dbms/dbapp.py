import sqlite3

try:
    db = sqlite3.connect("first.db")
    print("successfuly conected")
except Exception as e:
    print(e)

table = "create table student (id integer primary key autoincrement,name text,city text)"

try:
    db.execute(table)
    print("done!")
except Exception as e:
    print(e)

#     insert = '''insert into student(name,city)values
# ('shubham','valasan'),
# ('bhatt ji','paneli'),
# ('veshvi','rjk'),
# ('jadeja','knoda')'''
# try:
#     db.execute(insert)
#     db.commit()
#     print("done")
# except Exception as e:
#     print(e)

    update = "update student  set name='ram', city='ayodhya' where id = 2"
try:
    db.execute(update)
    db.commit()
    print("done")
except Exception as e:
    print(e)

dele = "delete from student where id=6"

try:
    db.execute(dele)
    db.commit()
    print("delete done")
except Exception as e:
    print(e)

cur = db.cursor()
show = "select * from student"

try:
    cur.execute(show)
    data = cur.fetchall()
    for i in data:
        print(i)
except Exception as e:
    print(e)

