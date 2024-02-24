import mysql.connector

# con=mysql.connector.connect(host="localhost",username="root",password="root")
#
# c=con.cursor()   #cursor object
#
# c.execute("create database company")
con = mysql.connector.connect(host="localhost",username="root",password="root",database="mydb")

c=con.cursor()

#c.execute("create table employee(id int primary key,name varchar(20),age int,gender varchar(20),place varchar(20),salary int) ")
#c.execute("insert into employee values(123,'meenu',23,'female','ekm',20000)")
#c.execute("insert into employee values(124,'anamika',24,'female','tvm',30000)")
# c.execute("insert into employee values(125,'anu',2,'female','hammi',40000)")
# con.commit()
print("before update")
c.execute("select * from employee")
k=c.fetchall()
print(k)

c.execute("update employee set name='anu' where id=125")
con.commit()
print("after update")
c.execute("select * from employee")
k=c.fetchall()
print(k)

print("after update")
c.execute("select * from employee")
k=c.fetchall()
print(k)
c.execute("delete from employee where id=124")
con.commit()
print("after delete")
c.execute("select * from employee")
k=c.fetchall()
print(k)



#con.close()
# con.execute("select * from employee where name like 'a__'")
# c.execute("select * from employee")
# k=c.fetchall()
# print(k)

