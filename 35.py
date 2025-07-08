# 35.	WAP Binary to decimal conversion

num = int(input("Enter a binary number: "))


temp = num
decimal = 0
    
exp = 0
while temp:
    digit = temp % 10
    decimal = decimal + digit * (2 ** exp)
    temp = temp // 10
    exp += 1
        
    
print(f"The decimal equivalent of binary {num} is: {decimal}")

