#40. Generate a half pyramid with numbers.
row=int(input("How many rows you want "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(f"{j}",end=" ")
    print()

