NUM_ROWS = 5
NUM_COLS = 5
EMPTY_SYMBOL = "O"
FILL_SYMBOL = "X"
START_POINT_ROWS = 2
START_POINT_COLS = 2

def get_empty_grid(num_cols, num_rows, empty_symbol):
    grid = []

    for x in range(num_rows):
        row = []
        for _ in range(num_cols):
            row.append(empty_symbol)
        grid.append(row)
    return grid

def print_grid(grid):
    for i in range(NUM_ROWS):
        print(grid[i])

def replace_grid(grid, START_POINT_COLS, FISTART_POINT_ROWS):
    grid[START_POINT_COLS][FISTART_POINT_ROWS] = FILL_SYMBOL
    return grid

# ------------------------------------MAIN-----------------------------------------
def main():
    # Plot
    grid = get_empty_grid(NUM_COLS, NUM_ROWS, EMPTY_SYMBOL)

    replace_grid(grid, START_POINT_COLS, START_POINT_ROWS)

    # around_point = [
    # grid[START_POINT_COLS-1][START_POINT_ROWS-1],
    # grid[START_POINT_COLS-1][START_POINT_ROWS],
    # grid[START_POINT_COLS-1][START_POINT_ROWS+1],
    # grid[START_POINT_COLS][START_POINT_ROWS-1],
    # grid[START_POINT_COLS][START_POINT_ROWS+1],
    # grid[START_POINT_COLS+1][START_POINT_ROWS-1],
    # grid[START_POINT_COLS-1][START_POINT_ROWS],
    # grid[START_POINT_COLS+1][START_POINT_ROWS+1]
    # ]

    for i in range(len(around_point)):
        around_point[i] = FILL_SYMBOL

    print(around_point)

    # print(grid)
    # print_grid(grid)

if __name__ == '__main__':
    main()