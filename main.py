NUM_ROWS = 5
NUM_COLS = 5
EMPTY_SYMBOL = "O"
FILLED_SYMBOL = "X"
START_POINT_ROWS = 2
START_POINT_COLS = 2


def get_empty_grid(NUM_COLS, NUM_ROWS, EMPTY_SYMBOL):
    grid = []

    for x in range(NUM_ROWS):
        grid.append([])
        for y in range(NUM_COLS):
            grid[x].append(EMPTY_SYMBOL)
    return grid


def plot_grid(grid):
    for i in range(NUM_ROWS):
        print(grid[i])


def replace_grid(grid, START_POINT_COLS, FISTART_POINT_ROWS):
    grid[START_POINT_COLS][FISTART_POINT_ROWS] = FILLED_SYMBOL
    return grid


# def look_around(grid, START_POINT_COLS, START_POINT_ROWS):
#     grid[START_POINT_COLS-1][START_POINT_ROWS-1],
#     grid[START_POINT_COLS-1][START_POINT_ROWS],
#     grid[START_POINT_COLS-1][START_POINT_ROWS+1],
#     grid[START_POINT_COLS][START_POINT_ROWS-1],
#     grid[START_POINT_COLS][START_POINT_ROWS+1],
#     grid[START_POINT_COLS+1][START_POINT_ROWS-1],
#     grid[START_POINT_COLS-1][START_POINT_ROWS],
#     grid[START_POINT_COLS+1][START_POINT_ROWS+1] = FILLED_SYMBOL

#     return grid

# ------------------------------------MAIN-----------------------------------------
def main():
    # Plot
    grid = get_empty_grid(NUM_COLS, NUM_ROWS, EMPTY_SYMBOL)

    replace_grid(grid, START_POINT_COLS, START_POINT_ROWS)

    # print(grid)

    plot_grid(grid)


if __name__ == '__main__':
    main()