# def add():
#     n1=int(input("enter a no"))
#     n2=int(input("enter a no"))
#     sum=n1+n2
#     print(sum)
# add()
# add()


#define a funtion to find the factorial of a number
def fact():
    i=1
    n=int(input("enter a numb"))
    fact=1
    while(i<=n):
        print(i,end=" ")
        fact=fact*i
        i=i+1
    print("fact=",fact)
fact()
# fact()

#print message
def msg():
    n=input('enter a msg')
    print("hello",n)
msg()
# msg()

#check wheather the number is even or not
def even():
    a=int(input())
    if(a%2==0):
       print("num is even")
    else:
       print("num is not even")
even()

#
d={101:['arun',23,'ekm'],102:['meera']}
sum=0
avg=0
for i in d.values():
    sum=sum+i[1]
avg=sum/3
print(avg)


#
avg=0
sum=0
for i in d.values():
    sum=sum+i['age']
    avg=sum/3
    print(avg)
