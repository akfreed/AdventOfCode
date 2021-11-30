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

    def add_node(self, identifier, data=None):
        node = Vertex(identifier, data)
        self.nodes[node.identifier] = node
        self.nodeOrder.append(node)

    def add_edge(self, id1, id2, directed=True, cost=1, direction=None):
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

    def remove_edge(self, id1, id2, directed=True):
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
        to_remove = None
        for edge in node1.edges:
            if edge.to.identifier == node2.identifier:
                to_remove = edge
                break
        # if no edge found, fail
        if to_remove is None:
            return False

        # remove the edge
        node1.edges.remove(to_remove)

        if directed is False:
            to_remove = None
            for edge in node2.edges:
                if edge.to.identifier == node1.identifier:
                    to_remove = edge
                    break
            # if no edge found, fail
            if to_remove is None:
                return False

            # remove the edge
            node2.edges.remove(to_remove)

        return True

    def auto_link_manhattan(self):
        """Automatically add edges to each node to the
        north, west, south, and east nodes, (if they exist) in that order.

        The node idenfier should be a 2-coordinate Vector
        """
        for position in self.nodes:
            if position.up() in self.nodes:
                self.add_edge(position, position.up(), directed=True, cost=1, direction=Direction.UP)
            if position.left() in self.nodes:
                self.add_edge(position, position.left(), directed=True, cost=1, direction=Direction.LEFT)
            if position.down() in self.nodes:
                self.add_edge(position, position.down(), directed=True, cost=1, direction=Direction.DOWN)
            if position.right() in self.nodes:
                self.add_edge(position, position.right(), directed=True, cost=1, direction=Direction.RIGHT)

    def auto_link_diagonal(self):
        """Automatically add edges to each node to the
        north, northwest, west, southwest, south, southeast, east, and northeast nodes, (if they exist) in that order.

        The node idenfier should be a 2-coordinate Vector
        """
        for position in self.nodes:
            if position.up() in self.nodes:
                self.add_edge(position, position.up(), directed=True, cost=1, direction=Direction.UP)
            if position.up().left() in self.nodes:
                self.add_edge(position, position.up().left(), directed=True, cost=1, direction=Direction.UP_LEFT)
            if position.left() in self.nodes:
                self.add_edge(position, position.left(), directed=True, cost=1, direction=Direction.LEFT)
            if position.down().left() in self.nodes:
                self.add_edge(position, position.down().left(), directed=True, cost=1, direction=Direction.DOWN_LEFT)
            if position.down() in self.nodes:
                self.add_edge(position, position.down(), directed=True, cost=1, direction=Direction.DOWN)
            if position.down().right() in self.nodes:
                self.add_edge(position, position.down().right(), directed=True, cost=1, direction=Direction.DOWN_RIGHT)
            if position.right() in self.nodes:
                self.add_edge(position, position.right(), directed=True, cost=1, direction=Direction.RIGHT)
            if position.up().right() in self.nodes:
                self.add_edge(position, position.up().right(), directed=True, cost=1, direction=Direction.UP_RIGHT)

    def reset_distances(self):
        for node in self.nodes.values():
            node.visited = False
            node.distance = inf
            node.parent = None

    def calc_distances(self, startNodeId, to_find_id=None):
        self.reset_distances()

        if isinstance(startNodeId, Vertex):
            start_node = startNodeId
        else:
            start_node = self.nodes[startNodeId]

        start_node.visited = False
        start_node.distance = 0

        to_visit = PriorityQueue(0)
        to_visit.put(start_node)

        while to_visit.empty() is False:
            node = to_visit.get()
            if node.visited:
                continue
            node.visited = True
            if to_find_id is not None and node.identifier == to_find_id:
                return

            for edge in node.edges:
                neighbor = edge.to

                if not neighbor.visited:
                    cost = edge.cost + node.distance
                    if cost < neighbor.distance:
                        neighbor.distance = cost
                        neighbor.parent = node
                    to_visit.put(neighbor)

    def find_path(self, startId, end_id, recalc_distance=True):
        if recalc_distance:
            self.calc_distances(startId, to_find_id=end_id)

        if isinstance(end_id, Vertex):
            end_node = end_id
        else:
            end_node = self.nodes[end_id]

        if end_node.distance == inf:
            return []

        path = []
        trace = end_node
        while trace is not None:
            path.append(trace)
            trace = trace.parent
        path.reverse()
        return path

    def calc_distance_pairs(self, node_ids):
        distances = {}
        for fromId in node_ids:
            self.calc_distances(fromId)
            my_distances = {}
            for toId in node_ids:
                if fromId == toId:
                    continue
                dist = self.nodes[toId].distance
                if dist != inf:
                    my_distances[toId] = dist
            distances[fromId] = my_distances
        return distances

    def reduce_map(self, node_ids):
        distances = self.calc_distance_pairs(node_ids)
        # if shortest_dist(a->b) + shortest_dist(b->c) == shortest_dist(a->c) then b is between a and c
        to_remove = set()
        for a in node_ids:
            for b in node_ids:
                if a == b or b not in distances[a]:
                    continue
                for c in node_ids:
                    if a == c or b == c or c not in distances[b] or c not in distances[a]:
                        continue
                    if distances[a][b] + distances[b][c] == distances[a][c]:
                        to_remove.add((a, c))

        for from_id, to_id in to_remove:
            del distances[from_id][to_id]

        # keep only the given nodes
        self.nodes = {identifier: self.nodes[identifier] for identifier in node_ids}

        # clear edges
        for node in self.nodes.values():
            node.edges = []

        # reattach edges
        for from_id in distances:
            for to_id in distances[from_id]:
                self.add_edge(from_id, to_id, directed=True, cost=distances[from_id][to_id])
