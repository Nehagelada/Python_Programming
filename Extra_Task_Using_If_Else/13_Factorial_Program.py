#13. Find the factorial of a number using a loop.
fact=1
num=int(input("Enter a number "))
if num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
         fact=fact*i
    print(f"Factorial of {num} is {fact}")

