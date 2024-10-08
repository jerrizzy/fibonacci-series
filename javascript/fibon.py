def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize the first two numbers in the sequence
    a, b = 0, 1

    # Calculate the nth number iteratively
    # Calculate the nth number iteratively
    for i in range(2, n + 1):
        a, b = a, a + b
    return b
