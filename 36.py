# 36.	WAP Decimal to binary conversion

num = int(input("Enter a decimal number: "))

temp = num
binary = []

while temp > 0:
    digit = temp % 2
    binary.append(str(digit))
    temp = temp // 2

binary.reverse()
binary_str = ''.join(binary)

print(f"The binary equivalent of decimal {num} is: {binary_str}")

