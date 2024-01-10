def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.

    Returns:
    - list of lists: New matrix with elements rounded to 2 decimal places.

    Raises:
    - TypeError: If the matrix is not a list of lists of integers or floats,
                 if each row of the matrix does not have the same size,
                 or if the divisor is not a number.
    - ZeroDivisionError: If the divisor is equal to zero.
    """
    # Check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round to 2 decimal places
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = matrix_divided(matrix, 3)
print(result)

