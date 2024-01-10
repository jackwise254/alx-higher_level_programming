def print_square(size):
    """
    Prints a square with the character #.

    Args:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)

# Example usage:
print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)

# Uncomment the line below to see the exception being raised
# print_square(-1)

