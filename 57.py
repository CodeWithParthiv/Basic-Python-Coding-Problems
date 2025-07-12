# 57.	WAP to find out Sum of positive square elements in an array

# explaination-> In an array we will find the sum of all positive square elements.
# Example: if array is [1, 2, 3, 4, 5, 6, -7, -8, -9]
# # The positive square elements are 1, 4, 9, 16, 25, 36
# # The sum of these elements is 91

list = list(map(int, input("Enter elements for the array separated by space: ").split()))

sum_of_squares = sum(x**2 for x in list if x > 0)

print("The sum of positive square elements in the array is:", sum_of_squares)