#38. Print a pattern of stars (triangle).
row=int(input("How many row you want "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()