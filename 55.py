# 55.	WAP to find out Sum of elements in an array

list = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    list.append(element)

print("The sum of elements in the array are:", sum(list))