#single thread  of execution

def f1():
    for i in range(1,6):
        print("hello")

def f2():
    for i in range(1,6):
        print("hi")
f1()
f2()

#multithreading

import time
import threading
def f1():
    for i in range(1,6):
        print("hello")
        time.sleep(1) #used small time gap in the working pgm tym

def f2():
    for i in range(1,6):
        print("hi")
        time.sleep(1)
f1()
f2()

t1=threading.thread(target=f1,args=[])#creating thread object t1 using thread constructor and assigns
#funtn f1 as target
t2=threading.thread(target=f1,args=[])#creating thread object t2 using thread constructor and assigns
#funtn f2 as target
t1.start()#to start operation of thread we must call its start()funtion
t2.start()#to start operation of thread we must call its start()funtion
