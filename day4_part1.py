from copy import deepcopy
    
def grid_shape(grid: list[list[str]]) -> tuple[int, int]:
    nrows = len(grid)
    ncols = len(grid[0])
    for row in grid:
        if len(row) != ncols:
            raise ValueError("All grid rows must be equal!")
    return nrows, ncols


def count_adjacents(grid: list[list[str]], pos: tuple[int, int]) -> int:
    nrows, ncols = grid_shape(grid)
    count = 0
    for dx in [-1, 0, +1]:
        for dy in [-1, 0, +1]:
            i, j = pos[0] + dx, pos[1] + dy
            if (i, j) == pos or not (0 <= i < nrows) or not (0 <= j < ncols):
                continue
            count += 1 if grid[i][j] == "@" else 0
    return count


def update_grid(grid: list[list[str]]):
    nrows, ncols = grid_shape(grid)
    new_grid = deepcopy(grid)
    removed = 0
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] != "@":
                continue
            nadjs = count_adjacents(grid, pos=(i, j))
            if nadjs < 4:
                new_grid[i][j] = "X"
                removed += 1
    return removed, new_grid


def print_grid(grid: list[list[str]]):
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    with open("day4_input.txt", "r") as file:
        txt = file.read()
        grid = [list(row) for row in txt.split()]
        nrows, ncols = grid_shape(grid)

    count, new_grid = update_grid(grid)
    print_grid(new_grid)

    print("Grid shape:", (nrows, ncols))
    print("Number of accessible rolls:", count)
