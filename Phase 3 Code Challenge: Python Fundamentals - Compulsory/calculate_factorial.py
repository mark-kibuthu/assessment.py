def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial