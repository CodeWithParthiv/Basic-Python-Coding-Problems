# 52.	WAP to print Floyd’s triangle

n = int(input("Enter the number of rows for Floyd's triangle: "))
num = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=' ')
        num += 1
    print()  # Move to the next line after each row

