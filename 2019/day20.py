from pathfinding import Graph
from utility import Vector


def getInput():
    with open('day20.txt', 'r') as file:
        lines = file.readlines()

    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    letters = {}
    graph = Graph()
    pos = Vector(0, 0)
    for line in lines:
        for c in line:
            if c == '.':
                graph.addNode(pos)
            elif c in uppercase:
                letters[pos] = c

            pos = pos.right()

        pos = pos.down()
        pos.x = 0

    graph.autoLinkManhattan()

    portals = {}
    for pos in letters:
        if pos.up() in letters:
            moniker = letters[pos.up()] + letters[pos]
            if pos.down() in graph.nodes:
                newPortal = pos.down()
            elif pos.up().up() in graph.nodes:
                newPortal = pos.up().up()
            else:
                assert False
            if moniker not in portals:
                portals[moniker] = newPortal
            else:
                portals[moniker] = (portals[moniker], newPortal)
        elif pos.left() in letters:
            moniker = letters[pos.left()] + letters[pos]
            if pos.right() in graph.nodes:
                newPortal = pos.right()
            elif pos.left().left() in graph.nodes:
                newPortal = pos.left().left()
            else:
                assert False
            if moniker not in portals:
                portals[moniker] = newPortal
            else:
                portals[moniker] = (portals[moniker], newPortal)

    for port in portals:
        if port == 'AA' or port == 'ZZ':
            continue
        graph.addEdge(portals[port][0], portals[port][1], directed=False)

    return graph, portals


def day20a():
    graph, portals = getInput()
    origin = portals['AA']
    goal = portals['ZZ']
    graph.calcDistances(origin, goal)
    print(graph.nodes[goal].distance)


def isInner(pos: Vector):
    return pos.x >= 10 and pos.x <= 125 and pos.y >= 10 and pos.y <= 125


def getInput2():
    with open('day20.txt', 'r') as file:
        lines = file.readlines()

    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # 30 should be enough. 25 is not enough
    depth = 30

    print("adding nodes...")
    graph = Graph()
    letters = {}
    pos = Vector(0, 0, 0)
    for line in lines:
        for c in line:
            if c == '.':
                dpos = pos.clone()
                for i in range(depth):
                    dpos.z = i
                    graph.addNode(dpos.clone())

            elif c in uppercase:
                letters[pos] = c

            pos = pos.right()

        pos = pos.down()
        pos.x = 0

    print("linking nodes...")
    graph.autoLinkManhattan()

    portals = {}
    for pos in letters:
        if pos.up() in letters:
            moniker = letters[pos.up()] + letters[pos]
            if pos.down() in graph.nodes:
                newPortal = pos.down()
            elif pos.up().up() in graph.nodes:
                newPortal = pos.up().up()
            else:
                assert False
            if moniker not in portals:
                portals[moniker] = newPortal
            else:
                if isInner(portals[moniker]):
                    assert isInner(newPortal) is False
                    portals[moniker] = (newPortal, portals[moniker])
                else:
                    assert isInner(newPortal)
                    portals[moniker] = (portals[moniker], newPortal)

        elif pos.left() in letters:
            moniker = letters[pos.left()] + letters[pos]
            if pos.right() in graph.nodes:
                newPortal = pos.right()
            elif pos.left().left() in graph.nodes:
                newPortal = pos.left().left()
            else:
                assert False
            if moniker not in portals:
                portals[moniker] = newPortal
            else:
                if isInner(portals[moniker]):
                    assert isInner(newPortal) is False
                    portals[moniker] = (newPortal, portals[moniker])
                else:
                    assert isInner(newPortal)
                    portals[moniker] = (portals[moniker], newPortal)

    print("linking portals...")
    for port in portals:
        if port == 'AA' or port == 'ZZ':
            continue
        for i in range(depth - 1):
            # connect inner to outer
            inner = portals[port][1].clone()  # inner, this level
            inner.z = i
            outer = portals[port][0].clone()  # outer, this level
            outer.z = i + 1
            graph.addEdge(inner, outer, directed=False)

    return graph, portals


def day20b():
    print("building map...")
    graph, portals = getInput2()
    origin = portals['AA']
    goal = portals['ZZ']
    print("pathfinding...")
    graph.calcDistances(origin, goal)
    print(graph.nodes[goal].distance)


if __name__ == '__main__':
    day20a()
    day20b()
