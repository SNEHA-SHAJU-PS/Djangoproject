#example for menu
# 1.add
# 2.sub
# 3.mul
# 4.div
# 5.exit

print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.exit")

ch=int(input("enter a choice"))
n=int(input("enter a num"))
b=int(input("enter a num"))

if(ch==1):
    a=add(n,b)
    print(a)
elif(ch==2):
    s=sub(n,b) 
    print(s)
elif(ch==3):
    p=mul(n,b)
    print(p)
elif(ch==4):
    q=div(n,b)
    print(q)
else:
    exit()