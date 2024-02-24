#1,2,..100
# for i in range(1,101):
#     print(i)

#1,3,5..99

# for i in range(1,100,2):
#
#       print(i,end=" ")

#2,4,...100

# for i in range(2,101,2):
#
#       print(i,end=" ")

#1,4,9,16...100

# for i in range(1,11):
#
#
#       print(i**2,end=" ")

#1 to 10
# sum=0
# product=1
# for i in range(1,11):
#       sum=sum+i
#       product=product*i
#       print(i)
# print("sum",sum)
# print("prod",product)

#2,4..10
# sum=0
# product=1
# for i in range(2,11,2):
#       sum=sum+i
#       product=product*i
#       print(i)
# print("sum",sum)
# print("prod",product)

#5,10,15...
# sum=0
# product=1
# for i in range(5,26,5):
#       sum=sum+i
#       product=product*i
#       print(i)
# print("sum",sum)
# print("prod",product)

#1,8,15...
# sum=0
# product=1
# for i in range(1,37,7):
#       sum=sum+i
#       product=product*i
#       print(i)
# print("sum",sum)
# print("prod",product)

#accessing through index value
# s="hello"
# for i in range(0,len(s)):
#       print(s[i])

#even index position characters only
# s="hello"
# for i in range(0,len(s),2):
#       print(s[i])

#multiplication table of number
#2*1=2
# 2*2=4
# 2*3=6
# ......
# 2*10=20

# i=1
# n=int(input("enter a number"))
# while(i<=10):
#       print(n,"*",i,"=",n*i)
#       i=i+1

#or for loop
# n=int(input("enter a number"))
# for i in range(1,11):
#       print(n,"*",i,"=",n*i)
#
#prit pattern
# n=input("enter a number")
# for i in range(1,11):
#
#      print(n*i)

#write program to find all 3 digit numbers that are divisible by 3
#

# for i in range(100,1000 ):
#     if(i%3==0):
#
#       print(i)

#write a pgm to count  a num of strings ,int ,float in sequence
# l=["banana",'a',1,9.8,3.4,7.2,6,9,10]
# a=0
# b=0
# c=0
# for i in l:
#     #print(i)
#     if(type(i)==int):
#        a=a+1
#     elif(type(i)==float):
#         b=b+1
#     elif(type(i)==str):
#         c=c+1
# print("count of int", a)
# print("count of float",b)
# print("count of str",c)

#print each char in reverse order
l=["banana",'orange','apple','pineapple','cherry']

  for i in range(-1,-1,-1):
               print(i)