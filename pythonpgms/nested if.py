#check wheather a number is divisible by 3 and2
# not by 3 and2
n=int(input())
if(n%2==0):
    if(n%3==0):
        print("divisible by 2 and 3")
    else:
        print("divisible by 2 not by 3")
else:
    if(n%3==0):
        print("num divisible by 3 and not by 2")
    else:
        print("not divisible by 2 and 3")
