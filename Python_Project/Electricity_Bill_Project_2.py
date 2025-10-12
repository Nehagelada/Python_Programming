rate=0
fix=50
surcharge=0
discount=0
hour=0
peak=0
late_price=0
total_pay=0

print("-----------------ADD DETAILS----------------")
name=input("Enter Your Name ")
unit=int(input("Enter a unit "))
if unit>0:
    peak_hour=input("Do You want to add peak hour(y/Y or n/N) ")
    if peak_hour=='y' or peak_hour=='Y':
        peak=int(input("Enter a Peak Hour "))
        if peak>50:
            hour=(peak-50)*2
        else:
            hour=0
            print("Please enter greater than 50 peak hour\n")

    late_fee=input("Do you want to add penalty(y/Y or n/N) ")
    if late_fee=='y' or late_fee=='Y':
        late_price=100
    else:
        late_price=0


   
    if unit<=100:
        rate=unit*5
    elif unit<=200:
        rate=(100*5)+(unit-100)*7
    elif unit<=300:
        rate=(100*5)+(100*7)+(unit-200)*10
    else:
        rate=(100*5)+(100*7)+(100*10)+(unit-300)*15
        if unit>500:
            surcharge=(unit-500)*0.10
        else:
            surcharge=0

    if unit<=50:
        discount=rate*5/100
    else:
        discount=0


    if unit<50:
        message="Your Electricity Consumption is Low"
    elif unit>=50 and unit<=200:
        message="Your Electricity Consumption is Medium"
    elif unit>200 and unit<500:
        message="Your Electricity Consumption is High"
    elif unit>=500:
        message="Your Electricity Consumption is Very High"



    print(" ")
    print("\n------------------------------")
    print("Electricity Bill")
    print("-------------------------------")
    print(f"You enter unit is {unit}\n")
    print(f"Total Amount is {rate}")
    print(f"Fix Meter Charges is {fix}")
    print(f"Peak Hour is {hour}")
    print(f"Surcharge is {surcharge}")
    print(f"Discount is {discount}")
    print(f"Late Penalty is {late_price}")
    print(f"{message}")
    print("----------------------------------")
    total_pay=(rate+fix+hour+surcharge+late_price-discount)
    print(f"Final Bill To Pay {total_pay}")

else:
    print("You entered a invalid input please check it.....")