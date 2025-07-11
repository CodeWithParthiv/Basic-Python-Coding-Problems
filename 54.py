# 54.	WAP to find out Smallest and largest element in an array

list = []
small = 0
max = 0
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    list.append(element)

for number in list:
    if small == 0 or number < small:
        small = number
    if max == 0 or number > max:
        max = number

print(f"The smallest element in the array is: {small}")
print(f"The largest element in the array is: {max}")
