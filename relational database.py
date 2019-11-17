import sqlite3
sql_create_table = """CREATE TABLE IF NOT EXISTS student_name(id INTERGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT);"""
insert_data = """INSERT INTO student_name(name,phone) VALUES(?,?)"""
select_data = """SELECT * FROM student_name"""

con = sqlite3.connect('student.db')
c = con.cursor()
c.exercise(sq1_create_table)

insert = con.cursor()
insert.execute(insert_data,("PhyoeMinThant", "09965152645"))
insert.execute(insert_data,("MinThant", "09794428157"))

select = con.cursor()
all_data = select.execute(select_data)

show = all_data.fetchall()

for x in show:
    print(x)
