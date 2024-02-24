# a toy vendor supplies 3 types of toys
# battery based toys,key based toys,electric based toys
# vendor gives a discount 10% an ordrs for battery based toy ,rs=more than 1000
# vendor gives a discount 5% an order for key based toy,rs= more than 100
#  vendor gives a discount 10% an order for electric toy,rs=more than 500
# numeric code  1,2,3 used for battery, key ,eletric toys
#  write the pgm that reads the product code and order amount
# and prints out the net amount that the customer is required to pay after the discount.

productcode=int(input("enter a product code 1,2,3 used battery,key,electrical toys respectively   "))
if(productcode==1):
    n = int(input("enter product rate"))
    if(n>1000):
        dis=n*10/100
        print("amount",n-dis)
    else:
        print("zero discount payment amount is",n)
elif(productcode==2):
    if(n>100):
        dis=n*5/100
        print("amount",n-dis)
    else:
        print("zero discount payment amount is",n)
elif(productcode==3):
    if(n>500):
        dis=n*10/100
        print("amount",n-dis)
    else:
        print("zero discount payment amount is",n)
else:
    print("product not available")
