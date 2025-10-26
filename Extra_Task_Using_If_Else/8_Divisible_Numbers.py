#8. Find whether a number is divisible by 5 and 11.
num=int(input("Enter a number "))
if (num%5==0 and num%11==0):
    print(f"{num} number is divisble for both")
elif num%5==0:
    print(f"{num} number is divisble by only 5")
elif num%11==0:
    print(f"{num} number is divisble by only 11")
else:
    print(f"{num} number is not divisble either 5 and 11")