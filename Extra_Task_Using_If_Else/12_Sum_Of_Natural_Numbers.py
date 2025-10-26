#12. Print the sum of first N natural numbers.
i=1
sum=0
num=int(input("Enter that number till which to sum of that numbers:- "))
while i<=num:
    print(i,end=" ")
    sum+=i
    i+=1
print(f"\nSum Of Natural Numbers is {sum}")