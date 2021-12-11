from utility import *
from pathfinding import *


def get_input_a():
    with open('day11.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    g = Graph()
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            g.add_node(Vector(x, y), int(val))
    g.auto_link_diagonal()
    return g


def get_input_b():
    return get_input_a()


def bfs(g, starting):
    g.reset_distances()

    to_visit = PriorityQueue(0)
    for n in starting:
        to_visit.put(n)

    while to_visit.empty() is False:
        node = to_visit.get()
        if node.visited:
            continue
        node.visited = True

        for edge in node.edges:
            neighbor = edge.to
            neighbor.data += 1
            if not neighbor.visited:
                if neighbor.data > 9:
                    to_visit.put(neighbor)

    a = True
    for v in g.nodes.values():
        if v.data > 9:
            v.data = 0
        else:
            a = False

    return a


def day11b():
    print("    Part A")
    g = get_input_a()
    agg = 0
    i = 1
    while True:
        for v in g.nodes.values():
            v.data += 1
        starting = [v for v in g.nodes.values() if v.data > 9]
        if starting:
            if bfs(g, starting):
                print(i)
                break

        i += 1
    # not 347








if __name__ == '__main__':
    day11b()
