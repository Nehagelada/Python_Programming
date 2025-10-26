#46. Count how many words, digits, and special characters in a string.
string=input("Enter a string ")
words=0
digit=0
special_char=0
for ch in string:
    if ch.isalpha():
        words+=1
    elif ch.isdigit():
        digit+=1
    else:
        special_char+=1
    
print(f"Total Words:- {words}")
print(f"Total Digits:- {digit}")
print(f"Total Special Character:- {special_char}")
