from utility import *
from pathfinding import *


def get_input_a():
    with open('day15.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    goal = None
    graph = Graph()
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            graph.add_node(Vector(x, y), int(val))
            goal = Vector(x, y)

    return graph, goal


def get_input_b():
    with open('day15.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    goal = None
    graph = Graph()
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            for j in range(5):
                for i in range(5):
                    risk = int(val) + i + j
                    while risk > 9:
                        risk -= 9
                    pos = Vector(x + i * len(line), y + j * len(lines))
                    graph.add_node(pos, risk)
                    goal = pos.clone()

    return graph, goal


def link_manhattan(self, condition=None):
    for position in self.nodes:
        if position.up() in self.nodes:
            if condition is None or condition(self.nodes[position.up()]):
                self.add_edge(position, position.up(), directed=True, cost=self.nodes[position.up()].data, direction=Direction.UP)
        if position.left() in self.nodes:
            if condition is None or condition(self.nodes[position.left()]):
                self.add_edge(position, position.left(), directed=True, cost=self.nodes[position.left()].data, direction=Direction.LEFT)
        if position.down() in self.nodes:
            if condition is None or condition(self.nodes[position.down()]):
                self.add_edge(position, position.down(), directed=True, cost=self.nodes[position.down()].data, direction=Direction.DOWN)
        if position.right() in self.nodes:
            if condition is None or condition(self.nodes[position.right()]):
                self.add_edge(position, position.right(), directed=True, cost=self.nodes[position.right()].data, direction=Direction.RIGHT)


def link_manhattan2(self, condition=None):

    for position in self.nodes:
        if position.up() in self.nodes:
            if condition is None or condition(self.nodes[position.up()]):
                self.add_edge(position, position.up(), directed=True, cost=self.nodes[position.up()].data, direction=Direction.UP)
                self.add_edge(position, position.up(), directed=True, cost=self.nodes[position.up()].data, direction=Direction.UP)
        if position.left() in self.nodes:
            if condition is None or condition(self.nodes[position.left()]):
                self.add_edge(position, position.left(), directed=True, cost=self.nodes[position.left()].data, direction=Direction.LEFT)
        if position.down() in self.nodes:
            if condition is None or condition(self.nodes[position.down()]):
                self.add_edge(position, position.down(), directed=True, cost=self.nodes[position.down()].data, direction=Direction.DOWN)
        if position.right() in self.nodes:
            if condition is None or condition(self.nodes[position.right()]):
                self.add_edge(position, position.right(), directed=True, cost=self.nodes[position.right()].data, direction=Direction.RIGHT)


def day15a():
    print("    Part A")
    graph, goal = get_input_a()
    link_manhattan(graph)
    path = graph.find_path(Vector(0, 0), goal)[1:]
    print(sum([v.data for v in path]))


def day15b():
    print("\n    Part B")
    graph, goal = get_input_b()
    link_manhattan(graph)
    path = graph.find_path(Vector(0, 0), goal)[1:]
    print(path)
    print(sum([v.data for v in path]))


if __name__ == '__main__':
    day15a()
    day15b()
