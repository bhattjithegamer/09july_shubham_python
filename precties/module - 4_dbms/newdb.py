import pymysql

try:
    db = pymysql.connect(host="localhost",user="root",passwd="",database="firstdb")
    print("data connected")
except Exception as e:
    print(e)

cr = db.cursor()

table = "create table student(id integer primary key auto_increment,name text,city text)"

try:
    cr.execute(table)
    print("created")
except Exception as e:
    print(e)

insert = "insert into student(name,city)values('shubham','valasan'),"
('bhatt ji','paneli'),
('jadeja','knoda'),
('veshvi','rjk')
try:
    cr.execute(insert)
    db.commit()
    print("done")
except Exception as e:
    print(e)

# update = "update student set name = 'jadeja',city = 'knoda' where id = 2"

# try:
#     cr.execute(update)
#     db.commit()
#     print("good")
# except Exception as e:
#     print(e)

    # dele = "delete from student where id = 2"
    # try:
    #     cr.execute(dele)
    #     db.commit()
    #     print("good")
    # except Exception as e:
    #     print(e)

# show = "select * from student"
# try:
#     cr.execute(show)
#     data = cr.fetchmany(1)
#     print(data)
# except Exception as e:
#     print(e)