# 40.	WAP Octal to binary conversion

num = input("Enter an octal number: ")

binary = []

# Process each digit of the octal number
for digit in num:
    bin_group = format(int(digit), '03b')  # Convert to 3-bit binary
    binary.append(bin_group)

# Join all binary groups to form the final binary number
binary_result = ''.join(binary)
print("Binary equivalent:", binary_result)



# 🔢 Input:
# num = "53"
# 🔁 Step-by-step Execution:

# num = input("Enter an octal number: ")  # User inputs: "53"
# binary = []
# State:

# num = "53"
# binary = []

# 🔄 Loop Over Each Octal Digit:
# 1️⃣ First digit: '5'

# bin_group = format(int('5'), '03b')  # format(5, '03b') → '101'
# binary.append('101')
# State:

# binary = ['101']

# 2️⃣ Second digit: '3'

# bin_group = format(int('3'), '03b')  # format(3, '03b') → '011'
# binary.append('011')
# State:

# binary = ['101', '011']

# 🔚 After the loop:

# binary_result = ''.join(binary)  # '101' + '011' → '101011'
# print("Binary equivalent:", binary_result)

# ✅ Final Output:
# Binary equivalent: 101011