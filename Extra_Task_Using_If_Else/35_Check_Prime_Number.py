#35. Check whether a number is prime.
count=0
num=int(input("Enter a number to check it is prime or not "))
for i in range(1,num+1):
    if num % i == 0:
        count+=1
if count == 2:
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")