#28. Check if a person is child, teenager, adult, or senior citizen.
age=int(input("Enter Your Age "))
if age>0 and age<=12:
    print("You are Child")
elif age>=13 and age<=19:
    print("You are Teenager")
elif age>=20 and age<=59:
    print("You are Adult")
else:
    print("You are Senior")