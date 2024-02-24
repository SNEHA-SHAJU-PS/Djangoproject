import sqlite3
con=sqlite3.connect("librarydb")
# sql_command="""create table book(bookid int primary key,
#                                          title varchar(20),
#                                          author varchar(20),
#                                            price int)"""
#
# con.execute(sql_command)
# print("Table Created successfully")
# con.execute("insert into book values(101,'Anu','tvm',25)")
# con.execute("insert into book values(102,'Aii','tvmu',59)")
# con.execute("insert into book values(102,'Aoi','tvmo',58)")
# con.commit()
# print("data inserted successfully")
#  k=con.execute('select * from book')
#  #print(k.fetchall())
# # for i in k:
# #     print(i)
print("before update")
k=con.execute('select * from book')
print(k.fetchall())

# con.execute("update book set title='jkl',price=300 where bookid=102")
# con.commit
con.execute('delete from book where bookid=101')
con.commit()

# print("after update")
# k=con.execute('select * from book')
# print(k.fetchall())
print("after delete")
k=con.execute('select * from book')
print(k.fetchall())