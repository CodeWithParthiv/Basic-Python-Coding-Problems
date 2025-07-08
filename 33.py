# 33.	“Can a number be expressed as a sum of two prime numbers”—WAP to exaplain?

n = int(input("Enter a number: "))

if(n < 2):
    print("Please enter a number greater than or equal to 2.")
    exit()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range (2,n):
    if is_prime(i):
        if (i+i == n):
            print(f"{n} can be expressed as the sum of two prime numbers: {i} + {i}")
        for j in range(i+1, n):
            if is_prime(j):
                if (i + j == n):
                    print(f"{n} can be expressed as the sum of two prime numbers: {i} + {j}")

print(f"{n} cannot be expressed as the sum of two prime numbers.")





