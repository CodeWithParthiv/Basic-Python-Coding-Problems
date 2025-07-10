# 50.	WAP to print Diamond pattern using stars

rows = int(input("Enter the number of rows (odd number): "))
if rows % 2 == 0:
    print("Please enter an odd number.")
else:
    for i in range(rows):
        for j in range(rows):
            if j == rows // 2 - i or j == rows // 2 + i or (i > rows // 2 and (j == i - rows // 2 or j == rows - 1 - (i - rows // 2))):
                print("*", end="")
            else:
                print(" ", end="")
        print()

