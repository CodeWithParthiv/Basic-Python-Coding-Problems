# 39.	WAP Binary to octal conversion

num = input("Enter a binary number: ")

# Reverse the binary string to process from right to left
temp = num[::-1]
octal = []

# Process every group of 3 bits
while temp:
    group = temp[:3]  # Take first 3 bits
    group_sum = 0
    
    for i in range(len(group)):
        if group[i] == '1':
            group_sum += 2 ** i
    
    octal.append(str(group_sum))
    temp = temp[3:]  # Remove the processed bits

# Since we processed in reverse, reverse the final octal digits
octal_result = ''.join(octal[::-1])
print("Octal equivalent:", octal_result)
