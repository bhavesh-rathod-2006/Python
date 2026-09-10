a=input("enter first side of triangle to form a valid t riangle ")
b=input("enter first side of triangle to form a valid t riangle ")
c=input("enter first side of triangle to form a valid t riangle ")


if a==b==c:
     print("the triangle is equilateral ")
elif a==b!=c or c==a!=b or b==c!=a:
     print("The triangle is Isosceles ") 
else:
    if a+b>c and a+c>b and  b+c>a :
            print("The triangle is Scalene ")    
    else:
        print("these three sides are not form a valid triangle")    