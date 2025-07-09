# 44.	WAP to find out Number of integers which has exactly 9 divisors

def count_divisors(n):
    """Count the number of divisors of a number."""
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
    return count

def count_numbers_with_nine_divisors(limit):
    """Count how many integers up to a limit have exactly 9 divisors."""
    count = 0
    for i in range(1, limit + 1):
        if count_divisors(i) == 9:
            count += 1
            print(f"Number with 9 divisors: {i}")
    return count

limit = int(input("Enter the limit up to which to count integers with exactly 9 divisors: "))
result = count_numbers_with_nine_divisors(limit)
print(f"Total numbers with exactly 9 divisors up to {limit}: {result}")