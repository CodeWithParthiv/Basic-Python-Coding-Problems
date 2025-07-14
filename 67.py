# 67.	WAP to find out Maximum scalar product of two vectors

vector1 = list(map(int, input("Enter the elements of the first vector separated by space: ").split()))
vector2 = list(map(int, input("Enter the elements of the second vector separated by space: ").split()))

scalar_product = sum(a * b for a, b in zip(sorted(vector1, reverse=True), sorted(vector2)))
print("Maximum scalar product of the two vectors:", scalar_product)