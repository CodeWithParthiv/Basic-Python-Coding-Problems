# 45.	WAP to find out Roots of a quadratic equation

import cmath

def find_roots(a, b, c):
    """Find the roots of a quadratic equation ax^2 + bx + c = 0."""
    # Calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    
    # Calculate the two roots using the quadratic formula
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    
    return root1, root2

# Input coefficients a, b, and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Find the roots
roots = find_roots(a, b, c)
print(f"The roots of the quadratic equation are: {roots[0]} and {roots[1]}")