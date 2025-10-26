#37. Count how many vowels and consonants in a word.
vowel=0
consonants=0
word=input("Enter a Word ")
length=len(word)
print(f"Total Length is {length}")
for ch in word:
    if ch =='a' or ch == 'e' or ch == 'i'or ch == 'o' or ch == 'u'or ch == 'A'or ch == 'E' or ch == 'I' or ch == 'O'or ch == 'U':
        vowel+=1
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        consonants+=1
print(f"Total Vowels is {vowel}")
print(f"Total Consonants is {consonants}")   
     
    
