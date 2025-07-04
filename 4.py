# 4.	WAP to identify A number is positive or negative

num = int(input("Enter a number: "))

if(num > 0):
    print(f"{num} is a positive number.")
elif(num < 0):
    print(f"{num} is a negative number.")
else:
    print("The number is zero, which is neither positive nor negative.")

    