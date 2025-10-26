#30. Find whether roots of quadratic equation are real, equal, or imaginary.
a=int(input("Enter a value of a "))
b=int(input("Enter a value of b "))
c=int(input("Enter a value of c "))
D=0
print(f"Quadratic Equation:-{a}x^2+{b}x+{c}=0 ")
D=b**2-4*a*c
if D>0:
    print("Roots are Real and Unequal")
elif D==0:
    print("Root are Real and Equal")
else:
    print("Root are Imaginary(Complex)")

