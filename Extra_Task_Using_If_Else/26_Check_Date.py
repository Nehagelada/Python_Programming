#26. Print whether a given date (dd, mm, yyyy) is valid or not.
date = int(input("Enter Date: "))
month = int(input("Enter Month: "))
year = int(input("Enter year: "))

if (year % 400 == 0) and (year % 4 == 0 or year % 100 !=0):
    leap=True
else:
    leap=False

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    days=31
elif month==4 or month==6 or month==9 or month==11:
    days=30
elif month==2:
    if leap:
        days=29
    else:
        days=28
else:
    month=0

if month>=1 and month<=12 and date>=1 and date<=days:
    print(f"[{date}/{month}/{year}] it is a valid date")
else:
    print(f"[{date}/{month}/{year}] it is not a valid date ")


