# 13.	WAP to find out Sum of digits of a number

num = int(input("Enter an integer: "))
sum = 0
while num != 0:
    lastdigit = num % 10
    sum = sum + lastdigit
    num = num // 10
print(f"The sum of number of digits in the integer is: {sum}")