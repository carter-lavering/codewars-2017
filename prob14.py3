# made by Luke
# CORRECT SOLUTION - POST COMPETITION
class Searcher:
    counter = 0
    grid = []
    def __init__(self, grid):
        self.grid = grid
    def search(self, x, y):
        preValUp = 0
        preValLeft = 0
        if y-1 >= 0:
            preValUp = self.grid[y-1][x]
        if x-1 >= 0:
            preValLeft = self.grid[y][x-1]
        #change #'s to 0's
        if preValUp == '#':
            preValUp = 0
        elif preValLeft == '#':
            preValLeft = 0
        #set value to preValLeft + preValRight
        if self.grid[y][x] != '#':
            self.grid[y][x] = preValUp + preValLeft
    def runSearch(self):
        for i in range(len(self.grid[0])):
            for j in range(len(self.grid)):
                if i != 0 or j != 0:
                    self.search(j, i)
                else:
                    if self.grid[j][i] == '#':
                        self.grid[len(self.grid) - 1][len(self.grid[0]) - 1] = 0
                        return
                    else:
                        self.grid[j][i] = 1
    def getEnd(self):
        if self.grid[len(self.grid) - 1][len(self.grid[0]) - 1] == '#':
            return 0
        return self.grid[len(self.grid) - 1][len(self.grid[0]) - 1]
    def getGrid(self):
        return self.grid
while True:
    x, y = [int(a) for a in input().split()]
    if x == 0 and y == 0:
        break
    grid = []
    for __ in range(y):
        grid.append(list(input()))
    # set up grid with 0's
    for i in range(y):
        for j in range(x):
            if grid[i][j] == '.':
                grid[i][j] = 0
    s = Searcher(grid)
    s.runSearch()
    print(s.getEnd())
    #print(s.getGrid())
