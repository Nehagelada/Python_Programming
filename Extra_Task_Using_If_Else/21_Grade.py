#21. Input marks and print grade (A, B, C, D, Fail).
marks=int(input("Enter a marks "))
if marks > 0 and marks <= 100:
    if marks >=70:
        print("A grade")
    elif marks>=60 and marks<70:
        print("B grade")
    elif marks>=50 and marks<60:
        print("C garde")
    elif marks>=40 and marks<50:
        print("D grade")
    else:
        print("Fail")
else:
    print("Invalid Number") 