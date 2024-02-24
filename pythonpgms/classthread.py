import time
from threading import Thread

class A(Thread):
    def run(self):
        for i in range(1,6):
            print("hi")
            time.sleep(1)

class B(Thread):
    def run(self):
        for i in range(1,6):
            print("hlo")
            time.sleep(1)

a=A() #thread object
a.start()

b=B() #thread object
b.start()
