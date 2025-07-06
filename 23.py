# 23.	WAP to identify an user given number is Strong number or not

# Strong number logic -> A Strong number is a number whose sum of the factorials of its digits is equal to the number itself. For example, 145 is a Strong number because 1! + 4! + 5! = 145.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number: "))
temp = num
strong_sum = 0

while temp > 0:
    digit = temp % 10
    strong_sum += factorial(digit)
    temp //= 10

if num == strong_sum:
    print(f"{num} is a Strong number")
else:
    print(f"{num} is not a Strong number")