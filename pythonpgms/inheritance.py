# class person:
#     def __init__(self):
#         self.name=input("enter the name")
#         self.age=int(input("enter the age"))
#     def show(self):
#         print(self.name,self.age)
# class employee(person):
#     def __init__(self):
#         super().__init__()
#         self.empid=int(input("enter the id"))
#         self.salary=int(input("enter the salary"))
#     def show1(self):
#         #print(self.name,self.age,self.empid,self.salary)
#         super().show()
#         print(self.empid,self.salary)
#
#
# e=employee()
#e.show()

#OR
# class person:
#     def getdetails(self):
#         self.name=input("enter the name")
#         self.age=int(input("enter the age"))
#
# class employee(person):
#     def getdetails1(self):
#         super().getdetails()
#         self.empid=int(input("enter the id"))
#         self.salary=int(input("enter the salary"))
#
# class department(employee):
#     def getdetails2(self):
#         super().getdetails1()
#         self.dname=input("enter the name")
#         self.dhead=input("enter the name of head")
#
#     def showdetails2(self):
#
#         print(self.dname,self.dhead)
#
# d=department
# d.getdetails2()
# d.showdetails2()


#Q
# class hospital:
#     def getdetails(self):
#         self.hosname=input("enter the hosname")
#         self.location=input("enter the location")
#         self.phone=int(input("enter the phone"))
#     def displaydetails(self):
#         print(self.hosname,self.location,self.phone)
# class department(hospital):
#     def getdetails1(self):
#         super().getdetails()
#         self.dname=input("enter the dname")
#         self.doctorname=input("enter the doctorname")
#     def displaydetails1(self):
#         super().displaydetails()
#         print(self.doctorname,self.dname)
#
# class patient(department):
#     def getdetails2(self):
#         super().getdetails1()
#         self.patientname=input("enter the patientname")
#         self.age=int(input("enter the age"))
#         self.gender=input("enter the gender")
#         self.phone=int(input("enter the phone"))
#     def displaydetails2(self):
#         super().displaydetails1()
#         print(self.patientname,self.age,self.gender,self.phone)
#
# p=patient()
# p.getdetails2()
# p.displaydetails2()

#Q
#HIERARCHUCAL
# class Vehicle:
#     def getdetails(self):
#         print("Enter the details")
#         self.name=input("Enter the name")
#         self.model=input("Enter the model")
#         self.year=int(input("Enter the year"))
#     def displaydetails(self):
#         print("VehicleName",self.name,"Model",self.model,"Year",self.year,end=" ")
#
#
# class Car(Vehicle):
#     def getdetails1(self):
#         super().getdetails()
#         self.mileage=int(input("Enter the mileage"))
#
#     def displaydetails1(self):
#         super().displaydetails()
#         print("Mileage", self.mileage,end=" ")
#
#
# class Bike(Vehicle):
#     def getdetails2(self):
#         super().getdetails()
#         self.CC = int(input("Enter the CC"))
#
#     def displaydetails2(self):
#         super().displaydetails()
#         print("CC", self.CC, end=" ")
#
# c=Car()
# c.getdetails1()
# c.displaydetails1()
#
# b=Bike()
# b.getdetails2()
# b.displaydetails2()

#Q HYBRID
# class Company:
#     def getdetails(self):
#         self.cname=input("Enter the companyname")
#
#     def displaydetails(self):
#         print("Companyname",self.cname,end=" ")
# class Development(Company):
#     def getdetails1(self):
#         Company.getdetails(self)
#         self.developername=input("Enter the developername")
#         self.developerid=input("Enter the developerid")
#
#     def displaydetails1(self):
#         Company.displaydetails(self)
#         print("Developername",self.developername,"DeveloperId",self.developerid,end="")
#
#
# class Testing(Company):
#     def getdetails2(self):
#
#         self.Testername = input("Enter the testername")
#         self.Testerid = input("Enter the testerid")
#
#     def displaydetails2(self):
#         print("Testername",self.Testername,"TesterId", self.Testerid, end="")
#
# class Project(Development,Testing):
#     def getdetails3(self):
#         Development.getdetails1(self)
#         Testing.getdetails2(self)
#         self.Projectname = input("Enter the Projectname")
#
#     def displaydetails3(self):
#         Development.displaydetails1(self)
#         Testing.displaydetails2(self)
#         print("Projectname", self.Projectname)
#
# p=Project()
# p.getdetails3()
# p.displaydetails3()

 