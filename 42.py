# 42.	WAP to find out Number of days in a given month of a given year

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    """Return the number of days in a given month of a given year."""
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    
    # Days in each month
    days_in_months = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 
                       31, 31, 30, 31, 30, 31]
    
    return days_in_months[month - 1]

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print(f"Number of days in month {month} of year {year}: {days_in_month(month, year)}")