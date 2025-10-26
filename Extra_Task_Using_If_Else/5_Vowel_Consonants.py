#5. Check if a character is a vowel or consonant.
char=input("Enter a single chracter ")
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='I' or char=='E' or char=='O' or char=='U':
    print("Character is Vowel")
elif (char >= 'a' and char <= 'z')or(char>='A' and char<='Z'):
    print("Character is Consonant")
else:
    print("You enter invalid character")