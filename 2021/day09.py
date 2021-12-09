from utility import Vector
from pathfinding import *


def get_input_a():
    with open('day09.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    grid = {}
    for y, line in enumerate(lines):
        for x, num in enumerate(line):
            pos = Vector(x, y)
            grid[pos.clone()] = int(num)
    return grid


def get_input_b():
    return get_input_a()


def find_mins(grid):
    mins = []
    for pos in grid:
        h = grid[pos]
        if pos.left() not in grid or h < grid[pos.left()]:
            if pos.right() not in grid or h < grid[pos.right()]:
                if pos.up() not in grid or h < grid[pos.up()]:
                    if pos.down() not in grid or h < grid[pos.down()]:
                        mins.append(pos.clone())
    return mins


def day9a():
    print("    Part A")
    grid = get_input_a()
    mins = find_mins(grid)
    agg = 0
    for m in mins:
        agg += 1
        agg += grid[m]
    print(agg)


def count_basin(g, m):
    g.reset_distances()
    agg = 0
    start_node = g.nodes[m]

    start_node.visited = False
    start_node.distance = 0

    to_visit = PriorityQueue(0)
    to_visit.put(start_node)

    while to_visit.empty() is False:
        node = to_visit.get()
        if node.visited:
            continue
        node.visited = True
        agg += 1

        for edge in node.edges:
            neighbor = edge.to

            if not neighbor.visited:
                cost = edge.cost + node.distance
                if cost < neighbor.distance:
                    neighbor.distance = cost
                    neighbor.parent = node
                to_visit.put(neighbor)
    return agg



def day9b():
    print("\n    Part B")
    grid = get_input_b()
    mins = find_mins(grid)
    g = Graph()
    for node in grid:
        g.add_node(node, grid[node])

    for position in g.nodes:
        if position.up() in g.nodes and g.nodes[position.up()].data != 9:
            g.add_edge(position, position.up(), directed=True, cost=1, direction=Direction.UP)
        if position.left() in g.nodes and g.nodes[position.left()].data != 9:
            g.add_edge(position, position.left(), directed=True, cost=1, direction=Direction.LEFT)
        if position.down() in g.nodes and g.nodes[position.down()].data != 9:
            g.add_edge(position, position.down(), directed=True, cost=1, direction=Direction.DOWN)
        if position.right() in g.nodes and g.nodes[position.right()].data != 9:
            g.add_edge(position, position.right(), directed=True, cost=1, direction=Direction.RIGHT)

    basins = sorted([count_basin(g, m) for m in mins], reverse=True)
    print(basins)
    print(basins[0] * basins[1] * basins[2])
    # not


if __name__ == '__main__':
    day9a()
    day9b()
