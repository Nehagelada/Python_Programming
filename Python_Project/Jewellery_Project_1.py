print("---------------KALYAN JWELLERS--------------")
print(" ")
name=input("Enter Your Name:- ")
gender=input("Enter Your Gender(f/m and F/M):- ")
age=int(input("Enter Age:- "))
product=input("Enter a product name:- ")
gram=int(input("Enter a product gram:- "))
print("Current Gold Price(1 gram):- 11,190")
print("----------------------------------")
gold=gram*11190
print("Total Gold Rate:- ",gold)
print(" ")
print("Making Charges(1 gram):- 845")
charge=gram*845
print("Total Making Charges:- ",charge)
print("-------------------------------------")
total=gold+charge
print("Total Amount:- ",total)



if gender=='M'and gender=='m':
    if age>=65:
        if total>210000 and total<310000:
            print("Discount is 20%")
            discount=gold*20/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}")
        elif total>310000 and total<510000:
            print("Discount is 30%") 
            discount=gold*30/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}") 
        elif total>510000:
            print("Discount is 35%") 
            discount=gold*35/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}")  
    else:
        if total>210000 and total<310000:
            print("Discount is 10%")
            discount=gold*10/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}")
        elif total>310000 and total<510000:
            print("Discount is 20%") 
            discount=gold*20/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}") 
        elif total>510000:
            print("Discount is 25%") 
            discount=gold*25/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}") 

if gender=='F' or gender=='f':
    if age>=65:
        if total>210000 and total<310000:
            print("Discount is 20%")
            discount=gold*20/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}")
        elif total>310000 and total<510000:
            print("Discount is 30%") 
            discount=gold*30/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}") 
        elif total>510000:
            print("Discount is 35%") 
            discount=gold*35/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}")  
    else:
        if total>210000 and total<310000:
            print("Discount is 10%")
            discount=gold*10/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}")
        elif total>310000 and total<510000:
            print("Discount is 20%") 
            discount=gold*20/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}") 
        elif total>510000:
            print("Discount is 25%") 
            discount=gold*25/100
            final=total-discount
            print(f"Your final paying bill is {total}-{discount} = {final}") 

        

    