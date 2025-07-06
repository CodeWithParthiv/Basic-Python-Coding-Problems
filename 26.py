# 26.	WAP to identify Automorphic number or not

# Automorphic number logic -> An Automorphic number is a number whose square ends with the same digits as the number itself. For example, 5 is an Automorphic number because 5^2 = 25, which ends with 5.
# example -> 5, 6, 25, 76 are Automorphic numbers

num = int(input("Enter a number: "))

square = num ** 2
temp = str(square)

if temp.endswith(str(num)):
    print(f"{num} is an Automorphic number")
else:
    print(f"{num} is not an Automorphic number")






