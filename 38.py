# 38.	WAP Octal to decimal conversion

num = int(input("Enter an octal number: "))

temp = num
decimal = 0
    
exp = 0
while temp:
    digit = temp % 10
    decimal = decimal + digit * (8 ** exp)
    temp = temp // 10
    exp += 1
        
    
print(f"The decimal equivalent of octal {num} is: {decimal}")