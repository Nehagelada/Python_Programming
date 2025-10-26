#23. Check whether a given number lies in a range [x, y].
x=int(input("Enter your starting range:- "))
y=int(input("Enter your ending range:- "))
num=int(input("Enter a number to check range:- "))
if num>=x and num<=y:
    print(f"Number {num} is in the range[{x},{y}]")
else:
    print(f"Number {num} is out of the range[{x},{y}]")
