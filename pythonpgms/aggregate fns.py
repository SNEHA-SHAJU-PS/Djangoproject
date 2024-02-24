import sqlite3
con=sqlite3.connect("shopdb")

# con.execute("create table product(p_id int primary key,p_name varchar(20),price int)")
# con.execute("""create table order1(order_id int primary key,address varchar(20),product_id int,
#             Foreign Key(product_id) References product(p_id))""")
# con.execute("insert into product values(1,'product1',1000)")
# con.execute("insert into product values(2,'product2',300)")
# con.execute("insert into product values(3,'product3',500)")
# con.execute("insert into product values(4,'product4',600)")
# con.execute("insert into product values(5,'product5',2000)")
# con.commit()
#
# con.execute("insert into order1 values(1,'ekm',3)")
# con.execute("insert into order1 values(2,'tvm',5)")
#
# con.commit()
#
# k=con.execute("select * from product")
# print(k.fetchall())
#
# k = con.execute("select * from order1")
# print(k.fetchall())
# k=con.execute("select * from product")
# print(k.fetchall())
# print("Inner join Results")
# k = con.execute("select order_id,p_name,price from product inner join order1 on product.p_id=order1.product_id")
# print(k.fetchall())
# print("Left join Results")
# k = con.execute("select order_id,p_name,price from product left join order1 on product.p_id=order1.product_id")
# print(k.fetchall())
print("cross join results")
k=con.execute("select order_id,p_name,price from product cross join order1")
#print(k.fetchall())
 for i in k:
    print(i)