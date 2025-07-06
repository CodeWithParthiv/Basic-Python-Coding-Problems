# 15.	WAP to find out Sum of numbers in a given range

startnum = int(input("Enter the starting number of the range: "))
endnum = int(input("Enter the ending number of the range: "))
sum = 0

for i in range(startnum, endnum + 1):
    sum += i

print("The sum of numbers from", startnum, "to", endnum, "is:", sum)