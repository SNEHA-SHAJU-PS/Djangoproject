#0,1,1,2,3,5,8,13,21,34
a=0
b=1
print(a,b,end=" ")
while((a+b)<=34):
    print(a+b,end="  ")
    a,b=b,a+b