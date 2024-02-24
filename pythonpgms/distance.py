#transport company charges according to the following list
#distance rate
# 1-50=8rs per km
# 51-100=10 rs per km
# >100=12 rs per km

a=int(input('enter a distance'))
if(1<=a<=50):
    fare=a*8
elif(51<=a<=100):
    fare=a*10
elif(a>100):
    fare=a*12
else:
    print("invalid")
print("fare is",fare)

