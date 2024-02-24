
class Person:

    def __init__(self):
        self.__name=input("Enter the name")
        self.age=int(input("Enter the age"))
    def display(self):
        print(self.__name,self.age)



p=Person()
#print(p.__name,p.age)
p.display()