#27. Calculate electricity bill using slab system.
rate=0
fix=50
surcharge=0
discount=0
hour=0
late_fee=0
final_amount=0
print("-----------------ADD DETAILS------------------")
name=input("Enter a name ")
unit=int(input("Enter a unit "))
peak_hour=input("Do you want to add peak hour(y/Y) ")
if peak_hour=="y" or peak_hour=="Y":
    peak=int(input("Enter a peak hour "))
    if unit>50:
        hour=(peak-50)*2
    else:
        hour=0
        print("Please enter greater than 50 unit to calculate the peak hour")
penalty=input("Do you want to add penalty (y/Y) ")
if penalty=="y" or penalty=="Y":
    late_fee=100
else:
    late_fee=0

if unit>0:

    if unit>0 and unit<=100:
        rate=unit*5
    elif unit>=101 and unit<=200:
        rate=(100*5)+(unit-100)*7
    elif unit>=201 and unit<=300:
        rate=(100*5)+(100*7)+(unit-200)*10
    else:
        if unit>=300:
            rate=(100*5)+(100*7)+(100*10)+(unit-300)*15
        

    #Surcharge
    if unit>500:
        surcharge=(unit-500)*0.10
    else:
        surcharge=0

    #Discount
    if unit<=50:
        discount=(unit-50)*5/100
    else:
        dicount=0
    
    #Consumption Message
    if unit<=50:
        message="Very Low Consumption"
    elif unit>50 and unit<=100:
        message="Low Consumption"
    elif unit>=101 and unit<=200:
        message="Medium Consumption"
    elif unit>=201 and unit<=300:
        message="High Consumption"
    else:
        message="Very High Consumption"

    print("--------------------------------------")
    print(f"Total Unit {unit}")
    print()
    print(f"Total Amount {rate}")
    print(f"Fixed Meter Charges {fix}") 
    print(f"Surcharge {surcharge}")
    print(f"Discount {discount}")
    print(f"Peak Hour {hour}")
    print(f"Late Penalty Fee {late_fee}")
    print(f"{message}")
    print("--------------------------------------")
    final_amount=rate+fix+surcharge+hour+late_fee-dicount
    print(f"Final Amount To Pay {final_amount}")
else:
    print("You Entered Invalid Input!!!!!!")