# 29.	WAP to find out Power of a number

num = int(input("Enter the base number: "))
power = int(input("Enter the power: "))

result = 1

for i in range(1, power + 1):
    result = result * num

print(f"{num} raised to the power of {power} is {result}")