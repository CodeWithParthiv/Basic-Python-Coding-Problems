# 48.	WAP to print Pyramid pattern using stars

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Print stars
    for j in range(2 * i - 1):
        print("*", end=" ")
    
    # Move to the next line after each row
    print()



