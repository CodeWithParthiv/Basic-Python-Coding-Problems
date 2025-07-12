# 58.	WAP to identify Second smallest element in an array

list = list(map(int, input("Enter the elements of the array separated by space: ").split()))

if len(list) < 2:
    print("Array must contain at least two elements.")

else:
    first = second = float('inf')
    
    for number in list:
        if number < first:
            second = first
            first = number
        elif number < second and number != first:
            second = number
    
    if second == float('inf'):
        print("There is no second smallest element.")
    else:
        print("The second smallest element is:", second)

# [ 1 7 -9 8 -90 0 5 6 4 3 2 ]



