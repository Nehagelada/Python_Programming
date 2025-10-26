#43. Ticket price calculation with age-based discount.
price=100
age=int(input("Enter Your Age "))
if age < 5 :
    discount=price-100
    print(f"Total Rupees is {discount}")
    print("Ticket Price for small children is 100% Free")
elif age >=5 and age <= 12:
    discount=price-50
    print(f"Total Rupees is {discount}")
    print("Ticket Price half for kids is 50% Free")
elif age >=13 and age <= 59:
    discount=price
    print(f"Total Rupees is {discount}")
    print("Ticket Price for adults is 0% Free")
elif age >=60:
    discount=price-30
    print(f"Total Rupees is {discount}")
    print("Ticket Price for senior citizen is 30% Free")

    


