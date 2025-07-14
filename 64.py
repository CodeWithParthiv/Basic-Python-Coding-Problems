# 64.	WAP to print and count Repeating elements in an array

# Input array from the user
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Dictionary to store frequency of each element
freq = {}

# Counting frequency of each element
for num in arr:
    freq[num] = freq.get(num, 0) + 1                           #freq.get(num, 0) initializes the count to 0 if num is not already in freq else get the value of current num and increase the value by 1                                 increments the count by 1

# List to store non-repeating elements
repeating = []

# Identifying non-repeating elements
for num in freq:
    if freq[num] > 1:
        repeating.append(num)

# Output
print("Repeating elements are:", repeating)
print("Total number of Repeating elements:", len(repeating))