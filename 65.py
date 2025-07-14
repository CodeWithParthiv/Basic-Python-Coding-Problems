# 65.	WAP to Remove duplicate elements in an array

list = list(map(int, input("Enter the elements of the array separated by space: ").split()))

removed_duplicates_list = set(list)
print("Array after removing duplicates:", removed_duplicates_list)