# 21.	WAP to identify an user given number is Palindrome or not

# Palindrome logic -> A number is called a Palindrome if it remains the same when its digits are reversed. For example, 121, 12321, etc.

num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if num == rev:
    print(f"{num} is a Palindrome number")
else:
    print(f"{num} is not a Palindrome number")


# With python short cut

num = input("Enter a number: ")
if num == num[::-1]:
    print(f"{num} is a Palindrome number")
else:
    print(f"{num} is not a Palindrome number")