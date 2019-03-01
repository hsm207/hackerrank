# Problem description: http://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/


def longest_path(matrix, row, column):
    current_val = matrix[row][column]
    if row + 1 < len(matrix) and matrix[row + 1][column] - current_val == 1:
        return 1 + longest_path(matrix, row + 1, column)

    if column + 1 < len(matrix[0]) and matrix[row][column + 1] - current_val == 1:
        return 1 + longest_path(matrix, row, column + 1)

    if row - 1 >= 0 and matrix[row - 1][column] - current_val == 1:
        return 1 + longest_path(matrix, row - 1, column)

    if column - 1 >= 0 and matrix[row][column - 1] - current_val == 1:
        return 1 + longest_path(matrix, row, column - 1)
    # dead end is counted as 1 because we did not count our starting point
    return 1


matrix = [
    [1, 2, 9],
    [5, 3, 8],
    [4, 6, 7]
]

paths = []

for row in range(len(matrix)):
    for col in range(len(matrix)):
        long_path = longest_path(matrix, row, col)
        paths.append(long_path)

print(max(paths))