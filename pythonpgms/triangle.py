#input t he 3 sides of a triangle.find wheather it is equilateral,scalene and isosceles
s1=input('enter side 1')
s2=input("enter side 2")
s3=input("enter side 3")
if(s1==s2==s3):
    print('equilateral triangle')
elif(s1==s2 or s2==s3 or s1==s3):
    print("isosceles triangle")
else:
    print("scalene triangle")