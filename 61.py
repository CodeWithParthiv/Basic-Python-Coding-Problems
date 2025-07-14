# 61.	WAP to find out Longest palindrome in an array

list = list(map(int, input("Enter the elements of the array separated by space: ").split()))

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def longest_palindrome(arr):
    max_length = 0
    longest_pal = None
    
    for num in arr:
        if is_palindrome(num):
            length = len(str(num))
            if length > max_length:
                max_length = length
                longest_pal = num
                
    return longest_pal

print("Longest palindrome in the array:", longest_palindrome(list))