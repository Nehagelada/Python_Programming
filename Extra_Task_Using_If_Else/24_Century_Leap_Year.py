#24. Check whether a year is a century leap year.
year=int(input("Enter a year to check it is leap year or century year:- "))
if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is a both leap and century year")
    else:
        print(f"{year} is only leap a year but not a century year")
else:
     print(f"{year} is only century a year but not a leap year")