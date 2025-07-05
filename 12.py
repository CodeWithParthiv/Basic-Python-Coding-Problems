# 12.	WAP to find out Number of digits in an integer

num = int(input("Enter an integer: "))
count = 0
while num != 0:
    lastdigit = num % 10
    count += 1
    num = num // 10
print(f"The number of digits in the integer is: {count}")