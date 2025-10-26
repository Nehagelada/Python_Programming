#44. Shopping discount calculator (10% if bill > 1000).
discount=0
final_amount=0
name=input("Enter Your name ")
bill=int(input("Enter Your Bill Amount "))
if bill > 1000 :
    discount=bill * 0.10
    final_amount=bill-discount
else:
    discount = 0
    final_amount = bill
print("-----------------------------")
print(f"Total Amount:- {bill}")
print(f"Total Discount:- {discount}")
print("-----------------------------")
print(f"Final Bill To Pay:- {final_amount}")
