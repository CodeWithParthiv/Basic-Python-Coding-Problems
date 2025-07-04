# 3.	WAP to find out Ascii values of a character

ch = input("Enter a character: ")
if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet character.")

elif( ch.isalpha() ):
    ascii_value = ord(ch)                           # Get ASCII value using ord()
    print(f"The ASCII value of '{ch}' is {ascii_value}.")