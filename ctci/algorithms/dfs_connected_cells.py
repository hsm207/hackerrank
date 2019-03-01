# problem description: https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
def getBiggestRegion(grid):
    n_row = len(grid)
    n_col = len(grid[0])

    region_sizes = []
    for row in range(n_row):
        for col in range(n_col):
            region_size = measure_region(grid, row, col)
            region_sizes.append(region_size)

    return max(region_sizes)


def measure_region(grid, row, col):
    # check for out of bounds
    if row not in range(len(grid)) or col not in range(len(grid[0])):
        return 0

    # abort if cell is not 1
    elif grid[row][col] != 1:
        return 0
    else:
        # mark visited cell as 0
        grid[row][col] = 0

        # count this cell and move on
        return 1 + measure_region(grid, row + 1, col) \
               + measure_region(grid, row - 1, col) \
               + measure_region(grid, row, col + 1) \
               + measure_region(grid, row, col - 1) \
               + measure_region(grid, row + 1, col + 1) \
               + measure_region(grid, row - 1, col - 1) \
               + measure_region(grid, row - 1, col + 1) \
               + measure_region(grid, row + 1, col - 1)


grid = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]

getBiggestRegion(grid)
