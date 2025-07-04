# 1.	WAP to check A character is a vowel or consonant

ch = input("Enter a character: ")

if(len(ch) != 1 or not ch.isalpha()):
    print("Please enter a single alphabet character.")

elif(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
    ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print(ch, "is a vowel")
    
else:
    print(ch, "is a consonant")