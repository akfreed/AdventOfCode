from pathfinding import Graph
from utility import Vector


def getInput(path):
    with open(path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    graph = Graph()
    doors = {}
    keys = {}
    origins = []
    pos = Vector(0, 0)

    for line in lines:
        for c in line:
            if c == '.':
                pass
            elif c in uppercase:
                doors[c] = pos
            elif c in lowercase:
                keys[c] = pos
            elif c == '@':
                origins.append(pos)

            if c != '#':
                graph.addNode(pos, c)
            pos = pos.right()
        pos = pos.down()
        pos.x = 0

    graph.autoLinkManhattan()

    return graph, doors, keys, origins


def getDag(graph, doors, keys, origin):
    combined = list(keys.values()) + list(doors.values()) + [origin]
    graph.reduceMap(combined)

    graph.calcDistances(origin)

    dag = {}
    for keyPos in keys.values():
        node = graph.nodes[keyPos]
        tracePath = set()
        traceNode = node.parent
        while traceNode.parent is not None:
            tracePath.add(traceNode.data)
            traceNode = traceNode.parent
        dag[node.data] = tracePath

    expandDag(dag)

    return dag


def expandDag(dag):
    # transitive closure. We want all doors to be turned into all necessary keys.
    done = False
    while not done:
        done = True
        for k in dag:
            requisiteDoors = []
            for parent in dag[k]:
                # is it a capital letter? (a door)
                if parent == parent.upper():
                    requisiteDoors.append(parent)
                    done = False
            for door in requisiteDoors:
                d = door.lower()
                dag[k].add(d)
                dag[k] |= dag[d]
            for door in requisiteDoors:
                dag[k] -= {door}


def Reachable(heldKeys, keyPrereqs, keyLocations):
    available = []
    for key in keyPrereqs:
        # if key not held already...
        if key not in heldKeys:
            # all pre-reqs satisfied
            if all([required in heldKeys for required in keyPrereqs[key]]):
                available.append((key, keyLocations[key]))
    return available


def StepsTo(robotLocations, goal, distancePairs):
    # copy list
    robotLocations = robotLocations[:]

    for i in range(len(robotLocations)):
        if goal in distancePairs[robotLocations[i]]:
            distance = distancePairs[robotLocations[i]][goal]
            robotLocations[i] = goal
            return distance, robotLocations
    assert False


def GetCost(robotLocations, heldKeys, keyPrereqs, keyLocations, distancePairs, cache):
    """
    Based on Reddit user mkeeter (https://www.reddit.com/user/mkeeter/) reply to
    https://www.reddit.com/r/adventofcode/comments/ecsw02/2019_day_18_missing_a_critical_step_of_the/
    """
    if len(heldKeys) == len(keyLocations):
        return 0, []

    state = (tuple(robotLocations), tuple(sorted(heldKeys)))
    if state not in cache:
        ways = []
        for key, keyLocation in Reachable(heldKeys, keyPrereqs, keyLocations):
            distance, newLocations = StepsTo(robotLocations, keyLocation, distancePairs)
            cost, sequence = GetCost(newLocations, heldKeys + [key], keyPrereqs, keyLocations, distancePairs, cache)
            cost += distance
            sequence = [key] + sequence
            ways.append((cost, sequence))
        m = min(ways, key=lambda t: t[0])
        cache[state] = m
    return cache[state]


def day18a():
    graph, doors, keys, origins = getInput('day18a.txt')
    origin = origins[0]

    dag = getDag(graph, doors, keys, origin)

    print('key requirements:')
    for k in sorted(dag):
        print("{} : {}".format(k, dag[k]))
    print()

    graph.reduceMap(list(keys.values()) + [origin])
    distancePairs = graph.calcDistancePairs(list(keys.values()) + [origin])

    cost, sequence = GetCost([origin], [], dag, keys, distancePairs, {})
    print('Part 1 shortest path:')
    print(cost)
    print(sequence)
    print()


def day18b():
    # Get DAG from part1 (it's the same)
    graph, doors, keys, origins = getInput('day18a.txt')
    dag = getDag(graph, doors, keys, origins[0])

    graph, doors, keys, origins = getInput('day18b.txt')

    graph.reduceMap(list(keys.values()) + origins)
    distancePairs = graph.calcDistancePairs(list(keys.values()) + origins)

    cost, sequence = GetCost(origins, [], dag, keys, distancePairs, {})
    print('Part 2 shortest path:')
    print(cost)
    print(sequence)


if __name__ == '__main__':
    day18a()
    day18b()
