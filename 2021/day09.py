from utility import Vector
from pathfinding import *


def get_input():
    with open('day09.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    grid = {}
    for y, line in enumerate(lines):
        for x, num in enumerate(line):
            pos = Vector(x, y)
            grid[pos.clone()] = int(num)
    return grid


def find_lows(grid):
    lows = []
    for pos in grid:
        h = grid[pos]
        if pos.left() not in grid or h < grid[pos.left()]:
            if pos.right() not in grid or h < grid[pos.right()]:
                if pos.up() not in grid or h < grid[pos.up()]:
                    if pos.down() not in grid or h < grid[pos.down()]:
                        lows.append(pos.clone())
    return lows


def count_basin(graph, low):
    graph.calc_distances(low)
    return len([vertex for vertex in graph.nodes.values() if vertex.distance != inf])


def day9a():
    print("    Part A")
    grid = get_input()
    lows = find_lows(grid)
    lows_val = sum([grid[low] + 1 for low in lows])
    print(lows_val)
    assert lows_val == 564


def day9b():
    print("\n    Part B")
    grid = get_input()
    lows = find_lows(grid)
    graph = Graph()
    for node in grid:
        graph.add_node(node, grid[node])
    graph.auto_link_manhattan(lambda vertex: True if vertex.data != 9 else False)

    basins = sorted([count_basin(graph, low) for low in lows], reverse=True)
    result = basins[0] * basins[1] * basins[2]
    print(result)
    assert result == 1038240


if __name__ == '__main__':
    day9a()
    day9b()
