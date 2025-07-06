# 18.	WAP to find out Fibonacci series up to n terms

def fibonacci(n):
    fib_series = []
    a = 0
    b = 1
    fib_series.append(a)
    fib_series.append(b)

    for i in range(2, n):
        c = a + b
        fib_series.append(c)
        a = b
        b = c
    return fib_series

num = int(input("Enter the number of terms for Fibonacci series: "))
fib_series = fibonacci(num)
print(f"The Fibonacci series up to {num} terms is: {fib_series}")


# 18.	WAP to find out Fibonacci series up to n

def fibonacci(n):
    fib_series = []
    a = 0
    b = 1
    fib_series.append(a)
    fib_series.append(b)

    for i in range(2, n):
        c = a + b
        if c > n:
            break
        fib_series.append(c)
        a = b
        b = c
    return fib_series

num = int(input("Enter the maximum value for Fibonacci series: "))
fib_series = fibonacci(num)
print(f"The Fibonacci series up to {num} is: {fib_series}")


    