#required arguments

# def f(n,a):
#     a=int(input("age="))
#     n=int(inpu("name="))
#     print("name is",n)
#     print("age is",a)
#arbitary arguments
def f(*args):
    print(args)
f(*args:7,8)
f(*args:7,8,9)
f(*args:1,2,3,4,5,6,7,8,9,10)
