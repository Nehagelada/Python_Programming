#18. Check whether a number is a palindrome (e.g., 121 → palindrome).
rem=0
rev=0
num=int(input("Entet a number "))
temp=num
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10

if temp==rev:
    print("Number is Palidrome")
else:
    print("Number is not Palidrome")