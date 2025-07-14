# 70.	WAP to find out Frequency of each element of an array

list = list(map(int, input("Enter the elements of the array separated by space: ").split()))

frequency = {}

for element in list:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print("Frequency of each element in the array:")
for element, count in frequency.items():
    print(f"Element {element}: {count} time(s)")