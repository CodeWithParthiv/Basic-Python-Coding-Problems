# 28.	WAP to identify Abundant number or not

# Abundant number logic -> An Abundant number is a number for which the sum of its proper divisors (excluding itself) is greater than the number. For example, 12 is an Abundant number because its divisors are 1, 2, 3, 4, and 6, and 1 + 2 + 3 + 4 + 6 = 16, which is greater than 12.

num = int(input("Enter a number: "))
sum_of_divisors = 0
temp = num

for i in range(1, temp):
    if temp % i == 0:
        sum_of_divisors += i

if sum_of_divisors > num:
    print(f"{num} is an Abundant number")
else:
    print(f"{num} is not an Abundant number")