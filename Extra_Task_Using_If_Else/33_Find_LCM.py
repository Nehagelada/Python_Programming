#33. Find the LCM of two numbers using loops.
lcm=0
n1=int(input("Enter a first number to find lcm "))
n2=int(input("Enter a second number to find lcm "))
#LCM hamesha dono numbers me se bada ya uske equal hota hai
max_num=max(n1,n2)
#USING WHILE LOOP TO PRINT MULTIPLES
count=1
limit=10
print(f"\nMultiples of Maximum Number are {max_num}")
while count<=limit:
    print(max_num * count,end=" ")
    count+=1
'''
#USING FOR LOOP TO PRINT MULTIPLES
print(f"\nMultiples of Maximum Number ({max_num}):")
for j in range(1, 11):   # 10 multiples print karne ke liye
    print(max_num * j, end=" ")
'''

while True:
    if max_num % n1 == 0 and max_num % n2 == 0:
        lcm = max_num
        break
    else:
        max_num += 1
  
print(f"\nLeast Common Multiple of {n1} and {n2} is {lcm}")


