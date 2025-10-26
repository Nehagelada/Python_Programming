#25. Find if a character is alphabet and if so, vowel/consonant.
char=input("Enter a single character ")
if char == 'a' or char =='e' or char =='i' or char =='o' or char =='u' or char =='A' or char =='E' or char =='I' or char =='O' or char =='U':
    print(f"{char} character is a vowel")
elif (char>='a' and char<='z') or (char>='A' and char<='Z'):
    print(f"{char} character is a consonant")
else:
    print(f"You entered invalid character")