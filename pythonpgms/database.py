import sqlite3
con=sqlite3.connect("mydb")

#print("Database Created Successfully")
# sql_command="""create table employee(id int primary key,
# name varchar(20),
# age int,
# place varchar(20),
# gender varchar(20),
# salary int)"""
#
# con.execute(sql_command)
# print("Table Created successfully")
# sql_command="insert into employee values(100,'Arun',26,'ekm','male',20000)"
# con.execute(sql_command)
# con.execute("insert into employee values(101,'Anu',28,'tvm','female',32000)")
# con.execute("insert into employee values(102,'Kiran',25,'tcr','male',28000)")
# con.execute("insert into employee values(103,'Manu',26,'kannur','male',30000)")
# con.execute("insert into employee values(104,'Meera',24,'tvm','female',22000)")
# con.execute("insert into employee values(105,'Linu',29,'kollam','female',35000)")
# con.commit()
# print("Data Inserted Successfully")
# con.close()
# k=con.execute('select * from employee')
# print(k.fetchall())

#between
k=con.execute('select * from employee where salary between 30000 and 35000')
print(k.fetchall())
k=con.execute('select * from employee where age between 25 and 28')
print(k.fetchall())

#in
k=con.execute('select * from employee where age in (25,26)')
print(k.fetchall())

#like
k=con.execute('select * from employee where name like "m__"')#or "m%" no limit for count of letters m...../ "_"underscore meaning is exactly one
print(k.fetchall())

#and or not
k=con.execute('select * from employee where name "%u" and age=26')
print(k.fetchall())
k=con.execute('select * from employee where name like "m__" or age=26')
print(k.fetchall())
k=con.execute('select * from employee where not (name="arun") ')
print(k.fetchall())

#order by
k=con.execute('select * from employee order by salary desc')
print(k.fetchall())
#distict
k=con.execute('select distict(age) from employee ')#avoid duplicates
print(k.fetchall())
