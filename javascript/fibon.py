def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize the first two numbers in the sequence
    a, b = 0, 1

    # Calculate the nth number iteratively
    # range method use a start2, and stop value n+1
    # the way range works is it stops one number short of the stop value
    # but we want to include the stop value in the iteration so we add 1 to n
    for i in range(2, n + 1):
        a, b = a, a + b
    return b
