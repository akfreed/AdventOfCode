from utility import Vector, render_map, inclusive_range


def get_input():
    with open('day05.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    lines = [line.split(' -> ') for line in lines]
    coords = []
    for line in lines:
        x, y = [int(n) for n in line[0].split(',')]
        v1 = Vector(x, y)
        x, y = [int(n) for n in line[1].split(',')]
        v2 = Vector(x, y)
        coords.append((v1, v2))
    return coords


def day5a():
    print("    Part A")
    coords = get_input()
    # Filter out diagonal lines.
    coords = [coord for coord in coords if coord[0].x == coord[1].x or coord[0].y == coord[1].y]
    grid = {}
    for coord in coords:
        # Horizontal lines.
        if coord[0].x == coord[1].x:
            for y in inclusive_range(coord[0].y, coord[1].y):
                v = Vector(coord[0].x, y)
                if v in grid:
                    grid[v] += 1
                else:
                    grid[v] = 1
        # Vertial lines.
        elif coord[0].y == coord[1].y:
            for x in inclusive_range(coord[0].x, coord[1].x):
                v = Vector(x, coord[0].y)
                if v in grid:
                    grid[v] += 1
                else:
                    grid[v] = 1
        else:
            assert False

    # Count the intersections.
    count = 0
    for key in grid:
        if grid[key] > 1:
            count += 1
    print(count)
    return count


def day5b():
    print("\n    Part B")
    coords = get_input()
    grid = {}
    for coord in coords:
        # horizontal
        if coord[0].x == coord[1].x:
            start = coord[0].y if coord[0].y < coord[1].y else coord[1].y
            end = (coord[0].y if coord[0].y > coord[1].y else coord[1].y) + 1
            for y in range(start, end):
                v = Vector(coord[0].x, y)
                if v in grid:
                    grid[v] += 1
                else:
                    grid[v] = 1

        # vertical
        elif coord[0].y == coord[1].y:
            start = coord[0].x if coord[0].x < coord[1].x else coord[1].x
            end = (coord[0].x if coord[0].x > coord[1].x else coord[1].x) + 1
            for x in range(start, end):
                v = Vector(x, coord[0].y)
                if v in grid:
                    grid[v] += 1
                else:
                    grid[v] = 1

        # diagonal
        else:
            assert abs(coord[0].x - coord[1].x) == abs(coord[0].y - coord[1].y)
            for x, y in zip(inclusive_range(coord[0].x, coord[1].x), inclusive_range(coord[0].y, coord[1].y)):
                v = Vector(x, y)
                if v in grid:
                    grid[v] += 1
                else:
                    grid[v] = 1

    count = 0
    for key in grid:
        if grid[key] > 1:
            count += 1
    print(count)
    return count


if __name__ == '__main__':
    count = day5a()
    assert count == 5084
    count = day5b()
    assert count == 17882
