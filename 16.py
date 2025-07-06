# 16.	WAP to find out Reverse of a given number

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("The reverse of the given number is:", rev)


# short cut of python code

# num = int(input("Enter a number: "))
# print("The reverse of the given number is:", str(num)[::-1])