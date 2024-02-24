# class A:
#     pass
#
# a=A()
# b=A()
#
# print(type(a))
# print(type(b))
#
# n=10
# m=[1,2,3]
# print(type(n))
# print(type(m))
#Q)
# class employee:
#     def __init__(self,n,a,s,i):
#         self.name=n
#         self.age=a
#         self.salary=s
#         self.empid=i
# e1=employee("arun",25,20000,100)
# print(type(e1))
# print(e1.name,e1.age,e1.salary,e1.empid)
# e2=employee("anu",23,15000,101)
# print(type(e2))
# print(e2.name,e2.age,e2.salary,e2.empid)


# class employee:
#     def __init__(self,n,a,s,i):
#         self.name=("enter name")
#         self.age=("enter age")
#         self.salary=("enter salry")
#         self.empid=("enter empid")
#
#         def show(self):
#             print(self.name,self.age,self.salary,self,empid)
#     e1=employee()
#     e1.show()
#     #print(e1.name, e1.age, e1.salary, e1.empid)
#     e2=employee()
#     e2.show()
#     #print(e2.name,e2.age,e2.salary,e2.empid)


# Q
# DEFINE A Class named book with attriuttes title author price
# and methods gettitle(),getauthor(),getprice(),
# setitle(),setauthor(),setprice()
# creates 2 objcts of class book


# class Book:
#         def __init__(self):
#             self.title = input("enter the title")
#             self.author = input("enter the name of author")
#             self.price = int(input("enter the price "))
#
#         def gettitle(self):
#             print(self.title)
#
#         def getauthor(self):
#             print(self.author)
#
#         def getprice(self):
#             print(self.price)
#
#         def setitle(self):
#             self.title = input("enter the new title")
#
#         def setauthor(self):
#             self.author = input("enter the new author name")
#
#         def setprice(self):
#             self.price = int(input("enter the new price"))
# b1=Book()
# b1.gettitle()
# b1.getauthor()
# b1.getprice()
# b1.setitle()
# b1.setauthor()
# b1.setprice()
#
# b2=Book()
# b2.gettitle()
# b2.getauthor()
# b2.getprice()
# b2.setitle()
# b2.setauthor()
# b2.setprice()

#Q
# create a class named circle with property radius and methods getarea()and getperimeter()
# area=3.14*r**2,per=2*3.14*r


# class Circle:
#     def __init__(self):
#         self.radius=int(input("enter the radius of the circle"))
#     def getarea(self):
#         r=self.radius
#         area=3.14*r**2
#         print(area)
#     def getperi(self):
#         r=self.radius
#         peri=2*3.14*r
#         print(peri)
# c1=Circle()
# c1.getarea()
# c1.getperi()
#
# c2=Circle()
# c2.getarea()
# c2.getperi()

#Q
# create a class named account and properties account name,acc num,balance
# methods withdraw(),deposit(),showbalance()

# class Account:
#     def __init__(self):
#         self.actname=input("enter the account name")
#         self.actnumbr=int(input("enter the account number"))
#         self.balance=int(input("enter the balance"))
#     def withdraw(self):
#         amount=int(input("enter the amount to withdraw"))
#         self.balance=self.balance-amount
#         print("current balance",self.balance)
#     def deposit(self):
#         amount=int(input("enter the amount to deposit"))
#         self.balance=self.balance+amount
#         print("current balance",self.balance)
#     def showbalance(self):
#         print("balance",self.balance)
# a1=Account()
# a1.withdraw()
# a1.deposit()
# a1.showbalance()
#
# a2=Account()
# a2.withdraw()
# a2.deposit()
# a2.showbalance()
#
# #or
# l=[]
# while(1):
#     print('1.create Account')
#     print('2.withdraw account')
#     print('3.deposit')
#     print('4.show balance')
#     print('5.exit')
#     ch=int(input("enter your choice"))
#     if ch==1:
#         a=Account()
#         l.append(a)
#         for i in l:
#             print(i)
#             print(i.actname,i.actnumbr,i.balance)
#     elif ch==2:
#         number=int(input("enter the account number"))
#         for i in l:
#             if(i.actnumbr==number):
#                i.withdraw()
#                break
#             else:
#                print("account does not exit")
#
#     elif ch==3:
#         number=int(input("enter the account number"))
#         for i in l:
#             if(i.actnumbr==number):
#                i.deposit()
#                break
#             else:
#                print("account does not exit")
#
#
#     elif ch==4:
#         number=int(input("enter the account number"))
#         for i in l:
#             if(i.actnumbr == number):
#                i.showbalance()
#                break
#             else:
#                print("account does not exit")
#     elif ch==5:
#         exit()

#Q
#USED MENU DRIVEN CODE IN BOOOK CLASS
class Library:
    def _init_(self):
        print("Enter the Book Details")
        self.bookid = int(input("Enter the Book Number"))
        self.title = input("Enter the title")
        self.author = input("Enter the author")
        self.price = int(input("Enter the price"))

    def showbooks(self):
        print("TITLE", self.title, "AUTHOR", self.author, "PRICE", self.price)

    def updatebook(self):

        # self.title = input("Enter the new title")
        # self.author = input("Enter the new author")
        # self.price = int(input("Enter the new price"))
        # print("Book is updated")
        attr = input("Enter the value to be updated")
        if (attr == "title"):
            self.title = input("Enter the new title")
        elif (attr == "author"):
            self.author = input("Enter the new author")
        elif (attr == "price"):
            self.price = int(input("Enter the new price"))
        else:
            self.title = input("Enter the new title")
            self.author = input("Enter the new author")
            self.price = int(input("Enter the new price"))

    def deletebook(self):
        l.remove(self)
        print("Book is Deleted")


l = []
while (1):
    print('1.ADD Books')
    print('2.BOOK DETAIL')
    print('3.UPDATE BOOK')
    print('4.DELETE BOOK')
    print('5.SHOW ALL BOOKS')
    print('6.EXIT')
    ch = int(input("Enter the choice"))
    if ch == 1:
        b = Library()
        l.append(b)
        for i in l:
            print(i)
            print(i.title,i.author,i.price,i.bookid)
    elif ch == 2:
        bid = int(input("Enter the bookid"))
        for i in l:
            if (i.bookid == bid):
                i.showbooks()
                break
        else:
            print("BOOK IS NOT AVAILABLE")
    elif ch == 3:
        bid = int(input("Enter the bookid"))
        for i in l:
            if (i.bookid == bid):
                i.updatebook()
                break
        else:
            print("BOOK IS NOT AVAILABLE")
    elif ch == 4:
        bid = int(input("Enter the bookid"))
        for i in l:
            if (i.bookid == bid):
                i.deletebook()
                break
        else:
            print("BOOK IS NOT AVAILABLE")


    elif ch == 5:
        print("BOOK LIST")
        for i in l:
            i.showbooks()
    else:
        exit()


