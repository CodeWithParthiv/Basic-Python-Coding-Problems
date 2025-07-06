# 22.	WAP to identify an user given number is Armstrong number or not

# Armstrong logic -> An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

num = int(input("Enter a number: "))
temp = num
num_digits = len(str(num))
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    temp //= 10

if num == armstrong_sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")