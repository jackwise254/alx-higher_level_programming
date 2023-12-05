def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in row:
            print("{:d}".format(number), end=" ")
        print()

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

