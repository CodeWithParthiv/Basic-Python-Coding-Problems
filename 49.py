# 49.	WAP to print Pyramid pattern using numbers

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Print numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Move to the next line after each row
    print()

    