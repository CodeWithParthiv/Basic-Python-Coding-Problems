# 24.	WAP to identify an user given number is Perfect number or not

# Perfect number logic -> A Perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself). For example, 6 is a Perfect number because its divisors are 1, 2, and 3, and 1 + 2 + 3 = 6.

num = int(input("Enter a number: "))
sum = 0
temp = num

for i in range(1, temp):
    if temp % i == 0:
        sum += i

if num == sum:
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is not a Perfect number")