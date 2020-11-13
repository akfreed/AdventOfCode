from pathfinding import Graph


def getInput():
    """:return: A map where key orbits value."""
    with open('day6.txt', 'r') as f:
        orbits = [line.strip().split(')') for line in f.readlines()]
        orbits = {pair[1]: pair[0] for pair in orbits}
    return orbits


def day6ab(orbits: dict):
    """:param orbits: A map where key orbits value."""

    graph = Graph()
    graph.addNode('COM')
    for key in orbits:
        graph.addNode(key, orbits[key])
    for key in orbits:
        graph.addEdge(key, orbits[key], directed=False)

    # Total number of direct & indirect orbits is the sum of all nodes distances from COM.
    graph.calcDistances('COM')
    part1_answer = sum([orbit.distance for orbit in graph.nodes.values()])

    # "Orbital transfers" from YOU to SAN.
    path = graph.findPath('YOU', 'SAN')
    part2_answer = len(path) - 3

    return part1_answer, part2_answer


if __name__ == "__main__":
    part1, part2 = day6ab(getInput())
    print(part1)
    print(part2)
