#6. Find the smallest of three numbers.
num1=int(input("Enter 1st number "))
num2=int(input("Enter 2nd number "))
num3=int(input("Enter 3rd number "))
if num1<num2 and num1<num3:
    print(f"First smallest number is a {num1}")
elif num2<num3:
    print(f"Second smallest number is a {num2}")
else:
    print(f"Third smallest number is a {num3}")