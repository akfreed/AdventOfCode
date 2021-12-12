from pathfinding import *


def get_input():
    with open('day12.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    graph = Graph()
    for line in lines:
        v1, v2 = line.split('-')
        if v1 not in graph.nodes:
            graph.add_node(v1)
        if v2 not in graph.nodes:
            graph.add_node(v2)
        v1, v2 = line.split('-')
        graph.add_edge(v1, v2, directed=False)
    # Use an int for visited instead of bool (for Part B).
    for node in graph.nodes.values():
        node.visited = 0
    return graph


def dfs(g, node, mulligan_used: bool):
    if node.identifier == "end":
        return 1

    if node.identifier.lower() == node.identifier:
        node.visited += 1

    num_paths = 0
    for edge in node.edges:
        neighbor = edge.to

        if neighbor.visited == 0:
            num_paths += dfs(g, neighbor, mulligan_used)
        elif mulligan_used is False and neighbor.identifier != "start":
            num_paths += dfs(g, neighbor, True)

    if node.identifier.lower() == node.identifier:
        node.visited -= 1
    return num_paths


def day12a():
    print("    Part A")
    graph = get_input()
    num_paths = dfs(graph, graph.nodes["start"], True)
    print(num_paths)
    assert num_paths == 4104
    return num_paths


def day12b():
    print("\n    Part B")
    graph = get_input()
    num_paths = dfs(graph, graph.nodes["start"], False)
    print(num_paths)
    assert num_paths == 119760
    return num_paths


if __name__ == '__main__':
    day12a()
    day12b()
