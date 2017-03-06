def add_left_and_up(array, x, y):
    """Set array[y][x] the sum of the cells to the left and above."""
    if x == y == 0:  # Upper-left corner
        array[y][x] = 1
    elif array[y][x] == '#':  # Is "#" (wall and thus no paths)
        array[y][x] = 0
    else:
        # These if statements make sure that if it's 0, it doesn't
        # accidentally take the last item of the list by indexing -1.
        if x == 0:
            left = 0
        else:
            left = array[y][x-1]
        if y == 0:
            up = 0
        else:
            up = array[y-1][x]
        array[y][x] = left + up

out = []
while True:
    cols, rows = (int(n) for n in input().split())
    if cols == rows == 0:  # If input is "0 0"
        break
    # This takes input rows many times, turns it into a list with each
    # character as an item (that's what list() does to strings), and sticks all
    # those into a list.
    grid = [list(input()) for __ in range(rows)]
    for y in range(cols):
        for x in range(rows):
            add_left_and_up(grid, x, y)
    out.append(grid[-1][-1])
print('\n'.join(str(x) for x in out), end='')
