# worked on by Luke
import math
minX = 0
minY = 0
maxX = 0
maxY = 0
myString = list(input())
tuples = []
counter = 0
direction = "R"
tuples.append([0,0])
if str.upper(myString[0]) == "R":
    direction = "R"
elif str.upper(myString[0]) == "L":
    direction = "L"
elif str.upper(myString[0]) == "D":
    direction = "D"
elif str.upper(myString[0]) == "U":
    direction = "U"
for index in range(1, len(myString)):
    # now go
    if direction == "R":
        mX = tuples[index - 1][0] + 1
        tuples.append([mX, tuples[index-1][1]])
        if mX > maxX:
            maxX = mX
        elif mX < minX:
            minX = mX
    elif direction == "L":
        mX = tuples[index - 1][0] - 1
        tuples.append([mX, tuples[index-1][1]])
        if mX > maxX:
            maxX = mX
        elif mX < minX:
            minX = mX
    elif direction == "D":
        mY = tuples[index - 1][1] + 1
        tuples.append([tuples[index-1][0], mY])
        if mY > maxY:
            maxY = mY
        elif mY < minY:
            minY = mY
    elif direction == "U":
        mY = tuples[index - 1][1] - 1
        tuples.append([tuples[index-1][0], mY])
        if mY > maxY:
            maxY = mY
        elif mY < minY:
            minY = mY
    
    if str.upper(myString[index]) == "R":
        direction = "R"
    elif str.upper(myString[index]) == "L":
        direction = "L"
    elif str.upper(myString[index]) == "D":
        direction = "D"
    elif str.upper(myString[index]) == "U":
        direction = "U"
grid = [[" " for y in range(maxY - minY + 1)] for x in range(maxX - minX + 1)]
for index in range(len(myString)):
    T = tuples[index]
    if minX < 0:
        T[0] += math.fabs(minX)
    if minY < 0:
        T[1] += math.fabs(minY)
    grid[int(T[0])][int(T[1])] = myString[index]
#finished by Carter
inverted_grid = [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]
for r in inverted_grid:
    print(''.join(r))
