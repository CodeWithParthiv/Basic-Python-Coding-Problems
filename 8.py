# 8.	WAP to find out LCM of two numbers

def calculate_lcm_iterative(a, b):
    greater = max(a, b)
    while True:
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


lcm_result = calculate_lcm_iterative(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm_result}")