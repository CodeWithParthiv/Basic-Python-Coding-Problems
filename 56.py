# WAP to Check if two arrays are the same or not

list1 = list(map(int, input("Enter 5 elements for the first array separated by space: ").split()))
list2 = list(map(int, input("Enter 5 elements for the second array separated by space: ").split()))

if list1 == list2:
    print("The two arrays are the same.")
else:
    print("The two arrays are not the same.")

