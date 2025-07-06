# 19.	WAP to find out Leap year or not

year = int(input("Enter a year to check if it is a leap year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")

