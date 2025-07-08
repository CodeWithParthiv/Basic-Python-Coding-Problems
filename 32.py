# 32.	WAP to print Armstrong numbers between two intervals

# Armstrong logic -> The sum of the cubes of its digits is equal to the number itself. Ex- 153 = 1^3 + 5^3 + 3^3


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

armstrong_numbers = []

def is_armstrong(n):
    digits = len(str(n))
    sum_of_cubes = 0

    temp = n
    while temp > 0:
        last_digit = temp % 10
        sum_of_cubes += last_digit ** digits
        temp //= 10

    if sum_of_cubes != n:
        return False
    
    return True

for num in range(start, end + 1):
    if is_armstrong(num):
        armstrong_numbers.append(num)
    else:
        continue

print(f"The Armstrong numbers between {start} and {end} are: {armstrong_numbers}")