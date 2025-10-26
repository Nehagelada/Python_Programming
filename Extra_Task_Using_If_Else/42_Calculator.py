#42. Menu-driven program: Calculator (+, -, *, /).
print("-----------------Menu---------------")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
ch=int(input("Enter your choice from above menu "))
if ch >= 1 and ch <=5:
    match ch:
        case 1: 
            n1=int(input("Enter a fisrt number "))
            n2=int(input("Enter a second number "))
            add=n1+n2
            print("-------------------------------")
            print(f"Addition of two numbers is {add}")
        case 2:
            n1=int(input("Enter a fisrt number "))
            n2=int(input("Enter a second number "))
            sub=n1-n2
            print("-------------------------------")
            print(f"Subtraction of two numbers is {sub}")
        case 3:
            n1=int(input("Enter a fisrt number "))
            n2=int(input("Enter a second number "))
            mul=n1*n2
            print("-------------------------------")
            print(f"Multiplication of two numbers is {mul}")
        case 4:
            n1=int(input("Enter a fisrt number "))
            n2=int(input("Enter a second number "))
            if n2 == 0:
                print("Cannot divide by zero! Try again.")
            else:
                print("-------------------------------")
                div=n1/n2
                print(f"Division of two numbers is {div}")
        case 5:
            exit()
else:
    print("You Entered Invalid Number!!!!")    



