# This function calculates the nth Fibonacci number using an iterative approach.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# We're calculating the 14th Fibonacci number (index 14, considering the start index is 0).
fib_number = fibonacci(14)
print(f"The 14th Fibonacci number is: {fib_number}")