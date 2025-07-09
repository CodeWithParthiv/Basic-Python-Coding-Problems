# 43.	WAP to find out Permutations in which n people can occupy r seats in a theatre

# permutation -> nPr
# Formula: nPr = n! / (n - r)!

n = int(input("Enter the total number of people (n): "))
r = int(input("Enter the number of seats (r): "))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
def permutations(n, r):
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)

result = permutations(n, r)