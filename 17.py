# 17.	WAP to find out Factorial of a number

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result = result * i
        return result

num = int(input("Enter a number to find its factorial: "))
fact = factorial(num)

print(f"The factorial of {num} is: {fact}")