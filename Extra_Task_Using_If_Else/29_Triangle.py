#29. Find whether a triangle is scalene, isosceles, or equilateral.
a=int(input("Enter first side of triangle "))
b=int(input("Enter second side of triagle "))
c=int(input("Enter third side of triangle "))
if (a+b>c) and (b+c>a) and (a+c>b):
    if a==b==c:
        print("Equilateral Triangle")
    elif a==b or b==c or a==c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")