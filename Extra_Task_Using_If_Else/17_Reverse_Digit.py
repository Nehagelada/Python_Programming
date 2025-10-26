#17. Reverse the digits of a number using a loop.
rem=0
rev=0
num=int(input("Enter a number "))
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(f"Reverse Number is {rev}")

