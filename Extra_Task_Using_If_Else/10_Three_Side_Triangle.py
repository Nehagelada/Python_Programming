#10. Check if three sides form a valid triangle.
side1=int(input("Enter a 1st angle "))
side2=int(input("Enter a 2nd angle "))
side3=int(input("Enter a 3rd angle "))
traingle=side1+side2+side3
if traingle==180:
    print("You entered sides it is a valid for triangle")
else:
    print("You entered sides are not valid for triangle")