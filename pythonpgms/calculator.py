#calculator pgm
# a=int(input())
# b=int(input())
# op=input("enter the operator +,*,-,/")
# if(op=="+"):
#     print("sum",a+b)
# elif(op=="-"):
#     print("sub",a-b)
# elif(op=="*"):
#     print("mul",a*b)
# elif(op=="/"):
#     print("div",a/b)
# else:
#     print('invalid op')

#input month name,find the no of days in a month
#list
l1=('januvary','march','may','july','august','october','december')#31 days
l2=('april','june','september','november')#30 days
l3=('februvary')#28 days
month_name=input("enter month name")
if(month_name in l1):
    print("31 days in month",month_name)
elif(month_name in l2):
    print("30 days in month",month_name)
elif(month_name in l3):
    print("28 days in month",month_name)
else:
    print("invalid month")