NUM_ROWS = 6
NUM_COLS = 6
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


def replace_grid(grid, START_POINT_COLS, START_POINT_ROWS):
    grid[START_POINT_COLS][START_POINT_ROWS] = FILL_SYMBOL
    return grid


# ------------------------------------MAIN-----------------------------------------
def main():
    grid = get_empty_grid(NUM_COLS, NUM_ROWS, EMPTY_SYMBOL)
    calculater_grid = grid
    grid = replace_grid(grid, START_POINT_COLS, START_POINT_ROWS)

    # grid[1][1] = 'X'
    # grid[1][2] = 'X'
    # grid[1][6] = 'X'
    # grid[1][7] = 'X'
    # # grid[2][7] = 'X'
    # grid[1][8] = 'X'
    grid[2][3] = 'X'
    grid[2][4] = 'X'

    print_grid(grid)

    for x in range(NUM_ROWS):
        for y in range(NUM_COLS):

            if grid[x][y] == FILL_SYMBOL:
                around_point = [
                    grid[x - 1][y - 1],
                    grid[x - 1][y],
                    grid[x - 1][y + 1],
                    grid[x][y - 1],
                    grid[x][y + 1],
                    grid[x + 1][y - 1],
                    grid[x + 1][y],
                    grid[x + 1][y + 1]
                ]

                x_counter = around_point.count(FILL_SYMBOL)

                print(x_counter)

                if x_counter == 2:
                    calculater_grid[x][y] = FILL_SYMBOL

    for i in range(NUM_ROWS):
        print(calculater_grid[i])


if __name__ == '__main__':
    main()