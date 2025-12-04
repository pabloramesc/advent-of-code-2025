from day4_part1 import grid_shape, update_grid, print_grid

with open("day4_input.txt", "r") as file:
    txt = file.read()
    grid = [list(row) for row in txt.split()]
    nrows, ncols = grid_shape(grid)

print("Initial state:")
print_grid(grid)

count = 0
while True:
    removed, grid = update_grid(grid)
    if removed == 0:
        break

    print(f"\nRemove {removed} rolls of paper:")
    print_grid(grid)

    # Clean the grid
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == "X":
                grid[i][j] = "."
                
    count += removed
    
print(f"\nRemoved a total of {count} rolls.")
