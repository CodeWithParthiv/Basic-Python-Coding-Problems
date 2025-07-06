# 30.	WAP to find out Factors of a number

num = int(input("Enter a number to find its factors: "))
factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print(f"The factors of {num} are: {factors}")