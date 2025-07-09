# 41.	WAP to Convert digit/number to words

def number_to_words(num):
    if num < 0:
        return "minus " + number_to_words(-num)
    elif num == 0:
        return "zero"

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", 
            "sixty", "seventy", "eighty", "ninety"]
    
    def words(n):
        if n < 10:
            return units[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + ('' if n % 10 == 0 else ' ' + units[n % 10])
        elif n < 1000:
            return units[n // 100] + ' hundred' + ('' if n % 100 == 0 else ' and ' + words(n % 100))
        elif n < 10000:
            return units[n // 1000] + ' thousand' + ('' if n % 1000 == 0 else ' ' + words(n % 1000))
        else:
            raise ValueError("Number out of range")

    return words(num)

num = int(input("Enter a number: "))
print("Number in words:", number_to_words(num))