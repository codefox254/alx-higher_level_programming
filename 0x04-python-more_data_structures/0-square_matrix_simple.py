#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []

        # Iterate through each element in the row, compute its square, and append to the result row
        for element in row:
            result_row.append(element ** 2)

        # Append the result row to the result matrix
        result_matrix.append(result_row)

    return result_matrix

# Example usage:
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = square_matrix_simple(input_matrix)
print(result)
