#9. Check whether a character is uppercase, lowercase, digit, or special symbol.
char=input("Enter a single character ")
if char>='A' and char<='Z':
    print(f"Character {char} is in Uppercase")
elif char>='a' and char<='z':
    print(f"Character {char} is in Lowercase")
elif char>='0' and char<='9':
    print(f"Character {char} is a Digit")
else:
    print(f"Character {char} is a Special Character")