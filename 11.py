# 11.	WAP to find out Greatest of three numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    print(f"{num1} is the greatest among {num1}, {num2}, and {num3}")
elif (num2 >= num3):
    print(f"{num2} is the greatest among {num1}, {num2}, and {num3}")
else:
    print(f"{num3} is the greatest among {num1}, {num2}, and {num3}")