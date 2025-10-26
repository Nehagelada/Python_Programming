#49. Simulate a guessing game (user guesses a number until correct).
import random
computer=random.randint(1,100)
status=True
while status:
    user=int(input("Enter a number:- "))
    if user>computer:
        print("Hint : Guess Lower Number")
    elif user<computer:
        print("Hint : Guess Higher Number")
    else:
        print("You Guess is correct!!")
        status=False
