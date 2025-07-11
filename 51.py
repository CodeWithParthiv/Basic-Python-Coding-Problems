# 51.	WAP to print Diamond pattern using numbers

rows = int(input("Enter the number of rows: "))
# Upper part of the diamond
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print(i + 1, end="")
    print()
# Lower part of the diamond
for i in range(rows - 2, -1, -1):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print(i + 1, end="")
    print()

