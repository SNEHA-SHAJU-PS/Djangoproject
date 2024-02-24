#global
# x=10
# def f():
#     x=20
#     print(x)
# f()
# print(x)

#local->

# def f():
#     #global x
#     x=80
#     print(x)
# f()
# print(x)

#non  local-->
# def outer():
#     x=10
#     def inner():
#         x=20
#         print(x)
#     print(x)
#     inner()
#     print(x)
# outer()

#built in-->

from math import pi
print(pi)
def f():
    print(pi)
def g():
    def h():
        print(pi)
        h()
g()
f()