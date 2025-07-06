# 27.	WAP to identify Harshad number or not

# Harshad number logic -> A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits. For example, 18 is a Harshad number because 1 + 8 = 9 and 18 is divisible by 9.

num = int(input("Enter a number: "))
temp = num
digit_sum = 0

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10

if num % digit_sum == 0:
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is not a Harshad number")