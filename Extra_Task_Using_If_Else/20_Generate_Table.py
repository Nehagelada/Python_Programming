#20. Generate the multiplication table of a number.
table=int(input("Enter a number to print a table "))
for i in range(1,10+1):
    print(f"{table} * {i} = {table*i} ")