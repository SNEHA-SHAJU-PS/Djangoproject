n=int(input("enter the number"))
count=0
for i in range(2,n):
    if(n%i==0):
        count=count+1
        break
if(count==0):
        print("prime number")
else:
        print("not prime number")