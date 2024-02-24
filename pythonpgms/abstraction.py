from abc import ABC,abstractmethod
class Vehicle(ABC):
    def start_engine(self):
        print("Starting Engine")
    def accelerate(self):
        print("Accelerating")
    def apply_brake(self):
        print("Applies Break")
    @abstractmethod
    def change_gear(self):
        pass
    def stop_engine(self):
        print("Stops the engine")

class Car(Vehicle):
    def f1(self):
        print("Function inside car")
    def change_gear(self):
        print("Changig gear automatically")

class Truck(Vehicle):
    def f2(self):
        print("Function inside truck")
    def change_gear(self):
        print("Changing gear manually")

c=Car()
c.change_gear()
t=Truck()
t.change_gear()


#--->abstract met hod

from abc import ABC,abstractmethod
class Employee(ABC):#Abstract class
    def __init__(self):
        self.empid=int(input("Enter the emp id"))
        self.first_name=input("Enter the firstname")
        self.last_name=input("Enter the lastname")
    def fullname(self):
        return self.first_name+' '+self.last_name
    @abstractmethod
    def getsalary(self):
        pass

class Fulltime(Employee):
    def __init__(self):
        super().__init__()
        self.salary=int(input("Enter the salary"))

    def getsalary(self):
        return self.salary

class Hourly(Employee):
    def __init__(self):
        super().__init__()
        self.hours=int(input("Enter the hours"))
        self.rate=int(input("Enter the rate"))

    def getsalary(self):
        return self.hours*self.rate
l=[]
while(1):
    print('1.Add Employee')
    print('2.Salary Details')
    print('3.Exit')
    ch=int(input("Enter your Choice"))
    if ch==1:
        type=input("enter the type of Employee")
        if(type=="fulltime"):
            e=Fulltime()
            l.append(e)
        elif(type=="hourly"):
            l.append(e)
        else:
            pass
    elif ch==2:
        name=input("Enter the name of Employee")
        for i in l:
            if(i.first_name==name):
                print(i.fullname(),':',i.getsalary())
                break
        else:
            print("Employee Does not Exist")
    else:
        exit()