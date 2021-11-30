from utility import Vector, render_map


BUG = '#'
NOT_BUG = '.'


def getInput1():
    with open('day24.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    pos = Vector(0, 0, 0)
    grid = {}
    for line in lines:
        for c in line:
            grid[pos] = c
            pos = pos.right()
        pos = pos.down()
        pos.x = 0
    return grid


def getInput2():
    with open('day24.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    pos = Vector(0, 0, 0)
    grid = {}
    for line in lines:
        for c in line:
            grid[pos] = c
            pos = pos.right()
        pos = pos.down()
        pos.x = 0
    del grid[Vector(2, 2, 0)]
    return grid


def countNeighbors(grid, pos):
    count = 0
    for neighbor in (pos.up(), pos.left(), pos.down(), pos.right()):
        if neighbor in grid and grid[neighbor] == BUG:
            count += 1
    return count


def countNeighbors2(grid, pos):
    count = 0
    for neighbor in (pos.up(), pos.left(), pos.down(), pos.right()):
        if neighbor in grid:
            if grid[neighbor] == BUG:
                count += 1

        if neighbor.y == -1:
            p = Vector(2, 1, neighbor.z + 1)
            if p in grid and grid[p] == BUG:
                count += 1
        elif neighbor.y == 5:
            p = Vector(2, 3, neighbor.z + 1)
            if p in grid and grid[p] == BUG:
                count += 1
        if neighbor.x == -1:
            p = Vector(1, 2, neighbor.z + 1)
            if p in grid and grid[p] == BUG:
                count += 1
        elif neighbor.x == 5:
            p = Vector(3, 2, neighbor.z + 1)
            if p in grid and grid[p] == BUG:
                count += 1

    if pos.x == 1 and pos.y == 2:
        for asdf in range(5):
            neighbor = Vector(0, asdf, pos.z - 1)
            if neighbor in grid and grid[neighbor] == BUG:
                count += 1
    if pos.x == 3 and pos.y == 2:
        for asdf in range(5):
            neighbor = Vector(4, asdf, pos.z - 1)
            if neighbor in grid and grid[neighbor] == BUG:
                count += 1

    if pos.x == 2 and pos.y == 1:
        for asdf in range(5):
            neighbor = Vector(asdf, 0, pos.z - 1)
            if neighbor in grid and grid[neighbor] == BUG:
                count += 1
    if pos.x == 2 and pos.y == 3:
        for asdf in range(5):
            neighbor = Vector(asdf, 4, pos.z - 1)
            if neighbor in grid and grid[neighbor] == BUG:
                count += 1

    return count


def show(grid):
    keys = list(grid.keys())
    keys.sort(key=lambda t: (t.z, t.y, t.x))

    zPrev = None
    yPrev = None
    for key in keys:
        if key.z != zPrev:
            print('\n\nlevel {}'.format(key.z), end='')
            zPrev = key.z

        if key.y != yPrev:
            print()
            yPrev = key.y

        print(grid[key], end='')
        if key.x == 1 and key.y == 2:
            print('?', end='')


def scoreGrid(grid):
    keys = list(grid.keys())
    keys.sort(key=lambda t: (t.y, t.x))
    bit = 1
    score = 0
    for key in keys:
        if grid[key] == BUG:
            score += bit
        bit *= 2
    return score


def checkLevel(grid, upper, lower):
    addUpper = False
    addLower = False
    for y in range(5):
        for x in range(5):
            if x == y == 2:
                continue
            if grid[Vector(x, y, upper)] == BUG:
                addUpper = True
            if grid[Vector(x, y, lower)] == BUG:
                addLower = True
    if addUpper:
        addEmptyGrid(grid, upper + 1)
        upper += 1
    if addLower:
        addEmptyGrid(grid, lower - 1)
        lower -= 1
    return upper, lower


def gameOfLife1(grid):
    dictSet = set()
    dictSet.add(scoreGrid(grid))

    while True:
        numBugs = 0
        newGrid = {}
        for pos in grid:
            numNeighbors = countNeighbors(grid, pos)
            if grid[pos] == BUG:
                if numNeighbors != 1:
                    newGrid[pos] = NOT_BUG
                else:
                    newGrid[pos] = grid[pos]
                    numBugs += 1
            else:
                if numNeighbors == 1 or numNeighbors == 2:
                    newGrid[pos] = BUG
                    numBugs += 1
                else:
                    newGrid[pos] = grid[pos]

        score = scoreGrid(newGrid)
        print('score: {}, num bugs: {}'.format(score, numBugs))

        if score in dictSet:
            print(score)
            break
        dictSet.add(score)
        grid = newGrid


def gameOfLife2(grid):
    dictSet = set()
    dictSet.add(scoreGrid(grid))
    rmap = { '#': '#', '.': '.'}
    #render_map(grid, rmap)
    #print()
    minute = 0
    upperlevel = 1
    lowerlevel = -1
    numBugs = None
    while minute < 200:
        upperlevel, lowerlevel = checkLevel(grid, upperlevel, lowerlevel)
        #print('================================')
        #show(grid)

        numBugs = 0
        newGrid = {}
        for pos in grid:
            numNeighbors = countNeighbors2(grid, pos)
            if grid[pos] == BUG:
                if numNeighbors != 1:
                    newGrid[pos] = NOT_BUG
                else:
                    newGrid[pos] = grid[pos]
                    numBugs += 1
            else:
                if numNeighbors == 1 or numNeighbors == 2:
                    newGrid[pos] = BUG
                    numBugs += 1
                else:
                    newGrid[pos] = grid[pos]
        #print()
        print('minute {} : {} bugs'.format(minute, numBugs))
        #render_map(newGrid, rmap)
        #print()
        grid = newGrid
        # if numBugs == 0:
        #     break

        minute += 1
    #print('================================')
    #show(grid)
    print(numBugs)


def day24a():
    grid = getInput1()
    gameOfLife1(grid)


def addEmptyGrid(grid, level):
    for y in range(5):
        for x in range(5):
            if x == y == 2:
                continue
            grid[Vector(x, y, level)] = NOT_BUG
    return grid


def day24b():
    grid = getInput2()
    addEmptyGrid(grid, 1)
    addEmptyGrid(grid, -1)
    gameOfLife2(grid)


if __name__ == '__main__':
    #day24a()
    day24b()
