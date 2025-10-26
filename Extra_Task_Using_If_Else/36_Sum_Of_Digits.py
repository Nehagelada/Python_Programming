# 36. Print the sum of digits of a number.
sum=0
num=int(input("How many numbers you want "))
print("Enter a numbers ")
for i in range(1,num+1):
    digit=int(input())
    sum+=digit
print(f"Total sum of digits {sum}")