import copy
import os

CYCLES = 3
NUM_ROWS = 6
NUM_COLS = 6
EMPTY_SYMBOL = "O"
FILL_SYMBOL = "X"


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


# ------------------------------------MAIN-----------------------------------------

def main():
    grid = get_empty_grid(NUM_COLS, NUM_ROWS, EMPTY_SYMBOL)
    calculater_grid = copy.deepcopy(grid)

    ####### Blinker
    grid[2][1] = 'X'
    grid[2][2] = 'X'
    grid[2][3] = 'X'

    # ####### Glider
    # grid[3][1] = 'X'
    # grid[4][2] = 'X'
    # grid[4][3] = 'X'
    # grid[2][3] = 'X'
    # grid[3][3] = 'X'

    print_grid(grid)

    for z in range(CYCLES):
        for x in range(NUM_ROWS):
            for y in range(NUM_COLS):

                if grid[x][y] == FILL_SYMBOL:
                    around_point = []
                    points = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

                    for x_offset, y_offset in points:

                        # if x + x_offset in range(NUM_ROWS) and y + y_offset in range(NUM_COLS):
                        #     around_point.append(grid[x + x_offset][y + y_offset])

                        if x+x_offset >= 0 or x+x_offset <= NUM_COLS and y+y_offset >= 0 or y+y_offset <= NUM_ROWS:
                            around_point.append(grid[x+x_offset][y+y_offset])

                    x_counter = around_point.count(FILL_SYMBOL)

                    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                    if x_counter < 2:
                        calculater_grid[x][y] = EMPTY_SYMBOL

                    # Any live cell with two or three live neighbours lives on to the next generation.
                    if 2 <= x_counter <= 3:
                        calculater_grid[x][y] = FILL_SYMBOL

                    # Any live cell with more than three live neighbours dies, as if by overpopulation.
                    if x_counter > 3:
                        calculater_grid[x][y] = EMPTY_SYMBOL

                # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                elif grid[x][y] == EMPTY_SYMBOL:
                    around_point = []
                    points = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

                    for x_offset, y_offset in points:

                        if x + x_offset in range(NUM_ROWS) and y + y_offset in range(NUM_COLS):
                            around_point.append(grid[x + x_offset][y + y_offset])

                        # if x+x_offset >= 0 or x+x_offset <= NUM_COLS and y+y_offset >= 0 or y+y_offset <= NUM_ROWS:
                        #     around_point.append(grid[x+x_offset][y+y_offset])

                    x_counter = around_point.count(FILL_SYMBOL)

                    if x_counter == 3:
                        calculater_grid[x][y] = FILL_SYMBOL

        print()
        for i in range(NUM_ROWS):
            print(calculater_grid[i])
        grid = copy.deepcopy(calculater_grid)


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main()