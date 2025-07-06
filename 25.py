# 25.	WAP to identify Friendly pair or not (amicable or not)

# Friendly pair (Amicable numbers) logic -> Two numbers are called amicable if the sum of the proper divisors of each number is equal to the other number. For example, 220 and 284 are amicable numbers because the sum of the proper divisors of 220 is 284, and the sum of the proper divisors of 284 is 220.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def sum_of_proper_divisors(n):
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors

sum1 = sum_of_proper_divisors(num1)
sum2 = sum_of_proper_divisors(num2)

if sum1 == num2 and sum2 == num1:
    print(f"{num1} and {num2} are amicable numbers")
else:
    print(f"{num1} and {num2} are not amicable numbers")