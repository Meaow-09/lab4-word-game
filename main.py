def fibonacci(n):
    """
    Compute the nth Fibonacci number using recursion.

    Args:
        n: Non-negative integer position in the Fibonacci sequence

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case: F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # Example usage
    print("Fibonacci sequence:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")

