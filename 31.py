# 31.	WAP to print Prime numbers in a given range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

prime_numbers = []

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n

for num in range(start, end + 1):
    if is_prime(num):
        prime_numbers.append(num)
    else:
        continue

print(f"The prime numbers between {start} and {end} are: {prime_numbers}")