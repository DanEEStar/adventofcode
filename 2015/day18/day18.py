from __future__ import print_function


def read_grid():
    grid = []
    with open('input.txt') as input:
        for line_number, line in enumerate(input, 0):
            line_state = []
            for s in line:
                if s == '#':
                    line_state.append(True)
                else:
                    line_state.append(False)
            grid.append(line_state)

    grid = set_corners_on(grid)
    return grid


def calc_num_alive_neighbours(grid, x, y):
    n = 0
    for iy in range(max(0, y-1), min(100, y+2)):
        for ix in range(max(0, x-1), min(100, x+2)):
            if ix == x and iy == y:
                continue
            #print(ix, iy, grid[iy][ix])
            n += grid[iy][ix]
    return n


def calc_next_cell_state(current_state, num_neighbours):
    if num_neighbours == 3:
        return True
    elif num_neighbours == 2:
        return current_state
    return False


def print_grid(grid):
    for line in grid:
        for state in line:
            if state:
                print('#', end='')
            else:
                print('.', end='')
        print('')


def create_next_grid_state(grid):
    next_grid = []
    for x in range(100):
        line = []
        for y in range(100):
            line.append(calc_next_cell_state(grid[y][x], calc_num_alive_neighbours(grid, x, y)))
        next_grid.append(line)

    next_grid = set_corners_on(next_grid)

    return next_grid


def set_corners_on(grid):
    grid[0][0] = True
    grid[0][99] = True
    grid[99][0] = True
    grid[99][99] = True

    return grid


def main():
    grid = read_grid()

    #print(calc_num_alive_neighbours(grid, 1, 1))

    for x in range(100):
        next_grid = create_next_grid_state(grid)
        grid = next_grid

    print_grid(grid)

    num_alive = 0
    for x in range(100):
        for y in range(100):
            num_alive += grid[x][y]

    print(num_alive)


if __name__ == '__main__':
    main()

