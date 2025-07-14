# 68.	WAP to find out Triplets with a given sum

# example-> Triplets meaning three numbers in a list that add up to a specific sum.

list1 = list(map(int, input("Enter the elements of the list separated by space: ").split()))

target_sum = int(input("Enter the target sum: "))
triplets = []

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        for k in range(j + 1, len(list1)):
            if list1[i] + list1[j] + list1[k] == target_sum:
                triplets.append((list1[i], list1[j], list1[k]))

if triplets:
    print("Triplets with the given sum:", triplets)
else:
    print("No triplets found with the given sum.")

