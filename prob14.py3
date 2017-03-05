class Searcher:
    counter = 0
    grid = []
    def __init__(self, count, grid):
        self.counter = count
        self.grid = grid
    def search(self, x, y):
        #end condition
        if x == len(self.grid[0]) - 1 and y == len(self.grid) - 1:
            self.counter += 1
            return
        #can we go right
        if (x+1) < len(self.grid[0]):
            if self.grid[y][x+1] != '#':
                self.search(x+1, y)
            else:
                return
        if (y+1) < len(self.grid):
            if self.grid[y+1][x] != '#':
                self.search(x, y+1)
    def getCounter(self):
        return self.counter
while True:
    x, y = [int(a) for a in input().split()]
    if x == 0 and y == 0:
        break
    grid = []
    for __ in range(y):
        grid.append(list(input()))
    s = Searcher(0, grid)
    s.search(0,0)
    print(s.getCounter())
