# 53.	WAP to print Pascal triangle

#         1 
#        1 1 
#       1 2 1 
#      1 3 3 1 
#     1 4 6 4 1
#    1 5 10 10 5 1
#   1 6 15 20 15 6 1

n = int(input("Enter the number of rows for Pascal's triangle: "))
for i in range(n):
    for j in range(n - i + 1):
        print(" ", end="")
    for j in range(i + 1):
        if j == 0 or j == i:
            print("1", end=" ")
        else:
            # Calculate the value using the binomial coefficient formula
            coeff = 1
            for k in range(1, j + 1):
                coeff = coeff * (i - k + 1) // k
            print(coeff, end=" ")
    print()  # Move to the next line after each row

