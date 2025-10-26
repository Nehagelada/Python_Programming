#22. Find the largest of three numbers using nested if.
n1=int(input("Enter a 1st number "))
n2=int(input("Enter a 2nd number "))
n3=int(input("Enter a 3rd number "))
if n1>n2:
    if n1>n3:
        print(f"{n1} number is largest number than {n2} and {n3}")
    else:
        print(f"{n3} number is largest number than {n1} and {n2}")
else:
    if n2>n3:
        print(f"{n2} number is largest number than {n1} and {n3}")
    else:
        print(f"{n3} number is largest number than {n1} and {n2}")