#31. Print Fibonacci series up to N terms.
a=0
b=1
num=int(input("Enter a ending point to print fibonacci series "))
print(f"{a} {b}",end=" ")
for i in range(2,num):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

    

