# 34.	WAP to Replace all 0’s with 1 in a given integer

n = int(input("Enter an integer: "))

temp = str(n)

if('0' not in temp):
    print(f"No 0's found in {n}.")
else:
    temp = temp.replace('0', '1')
    n = int(temp)
    print(f"After replacing all 0's with 1's, the integer is: {n}")