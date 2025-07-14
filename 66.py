# 66.	WAP to find out Minimum scalar product of two vectors

import numpy as np

vector1 = list(map(int, input("Enter the elements of the first vector separated by space: ").split()))
vector2 = list(map(int, input("Enter the elements of the second vector separated by space: ").split()))

scaler_product = sum(a * b for a, b in zip(sorted(vector1), sorted(vector2, reverse=True)))

print("Minimum scalar product of the two vectors:", scaler_product)

