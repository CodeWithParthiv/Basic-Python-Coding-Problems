# 14.	WAP to find out Sum of N natural numbers

n = int(input("Enter a natural number: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("The sum of the first", n, "natural numbers is:", sum)