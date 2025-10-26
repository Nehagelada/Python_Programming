#39. Print a square number pattern using loops.
row=int(input("How many row you want "))
for i in range(1,row+1):
    for j in range(1,row+1):
        print(f"{j}",end=" ")
    print()