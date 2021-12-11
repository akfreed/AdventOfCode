from utility import Vector
from pathfinding import *


def get_input():
    with open('day11.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    graph = Graph()
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            graph.add_node(Vector(x, y), int(val))
    graph.auto_link_diagonal()
    return graph


def flash_closure(graph, starting_nodes):
    if not starting_nodes:
        return

    graph.reset_distances()

    to_visit = PriorityQueue(0)
    for n in starting_nodes:
        to_visit.put(n)

    while to_visit.empty() is False:
        node = to_visit.get()
        if node.visited:
            continue
        node.visited = True

        for edge in node.edges:
            neighbor = edge.to
            neighbor.data += 1
            if not neighbor.visited and neighbor.data > 9:
                to_visit.put(neighbor)


def day11a():
    print("    Part A")
    graph = get_input()
    num_flashes = 0
    for i in range(100):
        for vector in graph.nodes.values():
            vector.data += 1
        starting_nodes = [v for v in graph.nodes.values() if v.data > 9]
        flash_closure(graph, starting_nodes)
        # Reset energy and count flashes.
        for vector in graph.nodes.values():
            if vector.data > 9:
                vector.data = 0
                num_flashes += 1
    print(f"Number of flashes: {num_flashes}")
    assert num_flashes == 1647
    return num_flashes


def day11b():
    print("\n    Part B")
    graph = get_input()
    i = 1
    while True:
        for vector in graph.nodes.values():
            vector.data += 1
        starting_nodes = [v for v in graph.nodes.values() if v.data > 9]
        flash_closure(graph, starting_nodes)
        # Reset energy and check if every squid flashed.
        sync_flash = True
        for vector in graph.nodes.values():
            if vector.data > 9:
                vector.data = 0
            else:
                sync_flash = False
        if sync_flash:
            break

        i += 1

    print(f"First synchronized flash: {i}")
    assert i == 348
    return i


if __name__ == '__main__':
    day11a()
    day11b()
