from math import inf
from utility import Direction
from queue import PriorityQueue


class Vertex:
    def __init__(self, identifier, data=None):
        self.identifier = identifier
        self.data = data
        self.edges = []
        self.visited = False
        self.distance = inf
        self.heuristic = 0
        self.parent = None

    def __repr__(self):
        return "<Vertex> " + repr(self.identifier)

    def __eq__(self, other):
        return self.distance == other.distance and self.heuristic == other.heuristic

    def __ne__(self, other):
        return self.distance != other.distance and self.heuristic != other.heuristic

    def __lt__(self, other):
        return self.distance + self.heuristic < other.distance + other.heuristic

    def __gt__(self, other):
        return self.distance + self.heuristic > other.distance + other.heuristic

    def __le__(self, other):
        return self.distance + self.heuristic <= other.distance + other.heuristic

    def __ge__(self, other):
        return self.distance + self.heuristic >= other.distance + other.heuristic


class Edge:
    def __init__(self, to: Vertex, cost=1, direction=None):
        self.to = to
        self.cost = cost
        self.direction = direction

    def __repr__(self):
        return '<Edge> to: {}   cost: {}'.format(repr(self.to), repr(self.cost))


class Graph:
    def __init__(self):
        self.nodes = {}
        self.nodeOrder = []

    def addNode(self, identifier, data=None):
        node = Vertex(identifier, data)
        self.nodes[node.identifier] = node
        self.nodeOrder.append(node)

    def addEdge(self, id1, id2, directed=True, cost=1, direction=None):
        """Add an edge from the first to the second node.
        :param id1: The identifier for the first node. Can also be the node itself (instead of the identifier)
        :param id2: The identifier for the second node. Can also be the node itself (instead of the identifier)
        :param directed: If False, automatically adds the link in the other direction. This could possibly mess up edge ordering if that matters.
        """
        if isinstance(id1, Vertex):
            node1 = id1
        else:
            node1 = self.nodes[id1]

        if isinstance(id2, Vertex):
            node2 = id2
        else:
            node2 = self.nodes[id2]

        node1.edges.append(Edge(node2, cost, direction))
        if not directed:
            node2.edges.append(Edge(node1, cost, direction))

    def removeEdge(self, id1, id2, directed=True):
        """Remove the edge from the first to the second node.
        Only removes 1 edge (if there are redundant edges)
        :param id1: The identifier for the first node. Can also be the node itself (instead of the identifier)
        :param id2: The identifier for the second node. Can also be the node itself (instead of the identifier)
        :param directed: If False, automatically removes the link in the other direction.
        :return: True if successful, False if the edge didn't exist. If directed=False and one of the edges doesn't exist, returns False
        """
        # resolve id to a node instance
        if isinstance(id1, Vertex):
            node1 = id1
        else:
            node1 = self.nodes[id1]

        if isinstance(id2, Vertex):
            node2 = id2
        else:
            node2 = self.nodes[id2]

        # search for the edge to remove in the node's edge list
        toRemove = None
        for edge in node1.edges:
            if edge.to.identifier == node2.identifier:
                toRemove = edge
                break
        # if no edge found, fail
        if toRemove is None:
            return False

        # remove the edge
        node1.edges.remove(toRemove)

        if directed is False:
            toRemove = None
            for edge in node2.edges:
                if edge.to.identifier == node1.identifier:
                    toRemove = edge
                    break
            # if no edge found, fail
            if toRemove is None:
                return False

            # remove the edge
            node2.edges.remove(toRemove)

        return True

    def autoLinkManhattan(self):
        """Automatically add edges to each node to the
        north, west, south, and east nodes, (if they exist) in that order.

        The node idenfier should be a 2-coordinate Vector
        """
        for position in self.nodes:
            if position.up() in self.nodes:
                self.addEdge(position, position.up(), directed=True, cost=1, direction=Direction.UP)
            if position.left() in self.nodes:
                self.addEdge(position, position.left(), directed=True, cost=1, direction=Direction.LEFT)
            if position.down() in self.nodes:
                self.addEdge(position, position.down(), directed=True, cost=1, direction=Direction.DOWN)
            if position.right() in self.nodes:
                self.addEdge(position, position.right(), directed=True, cost=1, direction=Direction.RIGHT)

    def autoLinkDiagonal(self):
        """Automatically add edges to each node to the
        north, northwest, west, southwest, south, southeast, east, and northeast nodes, (if they exist) in that order.

        The node idenfier should be a 2-coordinate Vector
        """
        for position in self.nodes:
            if position.up() in self.nodes:
                self.addEdge(position, position.up(), directed=True, cost=1, direction=Direction.UP)
            if position.up().left() in self.nodes:
                self.addEdge(position, position.up().left(), directed=True, cost=1, direction=Direction.UP_LEFT)
            if position.left() in self.nodes:
                self.addEdge(position, position.left(), directed=True, cost=1, direction=Direction.LEFT)
            if position.down().left() in self.nodes:
                self.addEdge(position, position.down().left(), directed=True, cost=1, direction=Direction.DOWN_LEFT)
            if position.down() in self.nodes:
                self.addEdge(position, position.down(), directed=True, cost=1, direction=Direction.DOWN)
            if position.down().right() in self.nodes:
                self.addEdge(position, position.down().right(), directed=True, cost=1, direction=Direction.DOWN_RIGHT)
            if position.right() in self.nodes:
                self.addEdge(position, position.right(), directed=True, cost=1, direction=Direction.RIGHT)
            if position.up().right() in self.nodes:
                self.addEdge(position, position.up().right(), directed=True, cost=1, direction=Direction.UP_RIGHT)

    def resetDistances(self):
        for node in self.nodes.values():
            node.visited = False
            node.distance = inf
            node.parent = None

    def calcDistances(self, startNodeId, toFindId=None):
        self.resetDistances()

        if isinstance(startNodeId, Vertex):
            startNode = startNodeId
        else:
            startNode = self.nodes[startNodeId]

        startNode.visited = False
        startNode.distance = 0

        toVisit = PriorityQueue(0)
        toVisit.put(startNode)

        while toVisit.empty() is False:
            node = toVisit.get()
            if node.visited:
                continue
            node.visited = True
            if toFindId is not None and node.identifier == toFindId:
                return

            for edge in node.edges:
                neighbor = edge.to

                if not neighbor.visited:
                    cost = edge.cost + node.distance
                    if cost < neighbor.distance:
                        neighbor.distance = cost
                        neighbor.parent = node
                    toVisit.put(neighbor)

    def findPath(self, startId, endId, recalcDistance=True):
        if recalcDistance:
            self.calcDistances(startId, toFindId=endId)

        if isinstance(endId, Vertex):
            endNode = endId
        else:
            endNode = self.nodes[endId]

        if endNode.distance == inf:
            return []

        path = []
        trace = endNode
        while trace is not None:
            path.append(trace)
            trace = trace.parent
        path.reverse()
        return path

    def calcDistancePairs(self, nodeIds):
        distances = {}
        for fromId in nodeIds:
            self.calcDistances(fromId)
            myDistances = {}
            for toId in nodeIds:
                if fromId == toId:
                    continue
                dist = self.nodes[toId].distance
                if dist != inf:
                    myDistances[toId] = dist
            distances[fromId] = myDistances
        return distances

    def reduceMap(self, nodeIds):
        distances = self.calcDistancePairs(nodeIds)
        # if shortest_dist(a->b) + shortest_dist(b->c) == shortest_dist(a->c) then b is between a and c
        toRemove = set()
        for a in nodeIds:
            for b in nodeIds:
                if a == b or b not in distances[a]:
                    continue
                for c in nodeIds:
                    if a == c or b == c or c not in distances[b] or c not in distances[a]:
                        continue
                    if distances[a][b] + distances[b][c] == distances[a][c]:
                        toRemove.add((a, c))

        for fromId, toId in toRemove:
            del distances[fromId][toId]

        # keep only the given nodes
        self.nodes = {identifier: self.nodes[identifier] for identifier in nodeIds}

        # clear edges
        for node in self.nodes.values():
            node.edges = []

        # reattach edges
        for fromId in distances:
            for toId in distances[fromId]:
                self.addEdge(fromId, toId, directed=True, cost=distances[fromId][toId])
