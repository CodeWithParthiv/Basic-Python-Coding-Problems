# 6.	WAP to Swap two numbers without third variable

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")


# Swapping using arithmetic operations use xor operator

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
print(f"After swapping: num1 = {num1}, num2 = {num2}")

