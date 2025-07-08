# 37.	WAP Decimal to octal conversion

num = int(input("Enter a decimal number: "))

temp = num
octal = []

remainder = []

while temp > 8:
    digit = temp % 8
    remainder.append(str(digit))
    temp = temp // 8

remainder.append(str(temp))
remainder.reverse()
octal_str = ''.join(remainder)

print(f"The octal equivalent of decimal {num} is: {octal_str}")
