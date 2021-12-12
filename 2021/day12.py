from pathfinding import *


def get_input_a():
    with open('day12.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    g = Graph()
    for line in lines:
        v1, v2 = line.split('-')
        if v1 not in g.nodes:
            g.add_node(v1)
        if v2 not in g.nodes:
            g.add_node(v2)
    for line in lines:
        v1, v2 = line.split('-')
        g.add_edge(v1, v2, directed=False)
    for node in g.nodes.values():
        node.visited = 0
    return g


def get_input_b():
    return get_input_a()


def dfs(g):
    g.reset_distances()
    start_node = g.nodes["start"]
    return dfs_r(g, start_node)


def dfs_r(g, node):
    if node.identifier == "end":
        return 1

    sub = 0

    if node.identifier == "start" or node.identifier.lower() == node.identifier:
        node.visited = True

    for edge in node.edges:
        neighbor = edge.to

        if not neighbor.visited:
            sub += dfs_r(g, neighbor)

    node.visited = False
    return sub


def dfs2(g):
    g.reset_distances()
    start_node = g.nodes["start"]
    return dfs_r2(g, start_node, False)


def dfs_r2(g, node, mulligan_used: bool):
    if node.identifier == "end":
        return 1

    sub = 0

    if node.identifier == "start" or node.identifier.lower() == node.identifier:
        node.visited += 1

    for edge in node.edges:
        neighbor = edge.to

        if neighbor.visited == 0:
            if neighbor.identifier != "start":
                sub += dfs_r2(g, neighbor, mulligan_used)
        elif mulligan_used is False and neighbor.identifier != "start":
            sub += dfs_r2(g, neighbor, True)

    if node.identifier == "start" or node.identifier.lower() == node.identifier:
        node.visited -= 1
    return sub


def day12a():
    print("    Part A")
    g = get_input_a()
    num_paths = dfs(g)
    print(num_paths)
    assert num_paths == 4104


def day12b():
    print("\n    Part B")
    g = get_input_b()
    num_paths = dfs2(g)
    print(num_paths)
    assert num_paths == 119760


if __name__ == '__main__':
    day12a()
    day12b()
