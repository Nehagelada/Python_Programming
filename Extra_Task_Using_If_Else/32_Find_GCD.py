#32. Find the GCD (HCF) of two numbers using loops.
gcd=1
n1=int(input("Enter a first number to find a gcd "))
n2=int(input("Enter a second number to find a gcd "))
min_num=0
min_num=min(n1,n2)
#chhote number tak hi loop chalana (kyunki GCD usse bada nahi ho sakta).
for i in range(1,min_num+1):
    if n1 % i == 0 and n2 % i == 0:
        print(i,end=" ")
        gcd=i
       
print(f"\nGreatest Common Divisor of {n1} and {n2} is {gcd}")
