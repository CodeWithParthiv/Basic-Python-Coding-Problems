# 2.	WAP to check A character is an alphabet or not

ch = input("Enter a character: ")

if len(ch) != 1 or not ch.isalpha():
    print("Not a valid character.")
elif ch.isalpha():
    print(ch, "is an alphabet.")