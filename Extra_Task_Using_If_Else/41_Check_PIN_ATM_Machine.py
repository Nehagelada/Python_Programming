#41. ATM machine: check PIN and balance withdrawal.
pin=1234
balance=100000
user_num=int(input("Enter your ATM pin number "))
if user_num == pin:
    name=input("Enter Your name ")
    withdrawal=int(input("Enter your withdrawal amount "))
    if withdrawal >= balance:
        print("You will have to compulsory keep 2000 in your bank.....")
        if withdrawal > balance:
            print("Do not withdrawal,Amount is inefficient!!!!!!")
    else:
        amount=balance-withdrawal
        print(f"\nTotal Amount is {balance}")
        print(f"Withdrawal Amount is {withdrawal}")
        print(f"After Withdrawal Total Amount is {amount}")
else:
    print("Invalid Pin number,please enter valid pin number!!!")
