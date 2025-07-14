# 69.	WAP to find out Number of even and odd elements in an array

list = list(map(int, input("Enter the elements of the list separated by space: ").split()))

even_count = 0
odd_count = 0

for num in list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)