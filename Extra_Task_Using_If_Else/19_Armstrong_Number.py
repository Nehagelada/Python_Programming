#19. Check whether a number is an Armstrong number (e.g., 153 → 1³+5³+3³ = 153).
arm=0
num=int(input("Enter a number "))
temp=num
count = len(str(num)) 
while num>0:
    r=num%10
    arm=arm+ pow(r,count) 
    num=num//10
if temp==arm:
    print("Number is a  Armstrong")
else:
    print("Number is not a Armstrong")

