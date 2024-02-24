#1,3,..99(sum,product)
# i=1
# product=1
# sum=0
# while(i<=100):
#     print(i)
#
#     sum=sum+i
#     product=product*i
#     i=i+2
#
# print("product=",product)
# print("sum=",sum)

 #5,10,15
# i=5
# product=1
# sum=0
# while(i<=100):
#     print(i)
#
#     sum=sum+i
#     product=product*i
#     i=i+5
#
# print("product=",product)
# print("sum=",sum)

#7,15,23,21.
# i=7
# product=1
# sum=0
# while(i<=100):
#     print(i)
#
#     sum=sum+i
#     product=product*i
#     i=i+8
#
# print("product=",product)
# print("sum=",sum)

#evn numbrs 200 to 300
# i=200
# product=i
# sum=0
# while(i<=300):
#      sum=sum+i
#      product=product*i
#      i=i+2
# print("sum",sum)
# print("product",product)
#1,4,9,16
# i=1
# product=1
# sum=0
# while(i<=10):
#      print(i**2)
#      sum=sum+i
#      product=product*i
#      i=i+1
# print("sum",sum)
# print("product",product)

#1,2,4,7,11...37
# i=1
# k=1
# product=1
# sum=0
# while(i<=100):
#         print(i)
#         sum=sum+i
#         product=product*i
#         i=i+k
#         k=k+1
# print("sum",sum)
# print("product",product)

#2,5,10,17,26,37...
# i=2
# k=3
# product=1
# sum=0
# while(i<=100):
#         print(i)
#         sum=sum+i
#         product=product*i
#         i=i+k
#         k=k+2
# print("sum",sum)
# print("product",product)

#sum and product of num divisible by 3(1 to 100)
# i=1
# sum=0
# product=1
# while(i<=100):
#     if(i%3==0):
#         print(i,end=" ")
#         sum=sum+i
#         product=product*i
#     i=i+1
# print("sum=",sum)
# print("product=",product)
#sum and product of num divisible by 5 and 7(1 to 100)
i=1
sum=0
product=1
while(i<=100):
    if(i%5==0 and i%7==0):
        print(i,end=" ")
        sum=sum+i
        product=product*i
    i=i+1
print(product,"pro")
print(sum,"sum")

