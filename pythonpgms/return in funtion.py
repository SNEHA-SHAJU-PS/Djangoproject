#using return funtion

# def add():
#     n1=int(input())
#     n2=int(input())
#     sum=n1+n2
#     return sum
# s=add()
#
# print(s)

#multiple operations using python
# def op():
#     n1=int(input())
#     n2=int(input())
#     sum=n1+n2
#     dif=n1-n2
#     return sum,dif
# s,d=op()
#
# print(s)
# print(d)


#write a funtion to calculate simple intersting(using return statement)
# s1=p*n*r/100
# p=amount 1000
# n=year 2
# r=rate 10

def interst():
    p=int(input('amount'))
    n=int(input('year'))
    r=int(input('rate'))
    s1=p*n*r/100
    return s1
s=interst()
print(s)