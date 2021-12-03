import math
import functools


def lcm(*args):
    """Return the LCM of multiple numbers.
    The numpy version of LCM is susceptible to overflow.
    There must be at least 2 arguments.
    """
    assert len(args) >= 2
    return functools.reduce(lambda a, b: a * b // math.gcd(a, b), args)


def float_approx_equals(f1, f2, tolerance=0.00001):
    return True if abs(f1 - f2) < tolerance else False


def str2ascii(str):
    return [ord(c) for c in str]


def congruence(a, b, m):
    """Solve a linear congruence--a function of the form ax === b mod m
    Here === means 'equivalent'
    Solve for x with a, b, and m given.
    Note that (ax + c) % m = b can be rearranged into this form.
    b mod m is a congruence class (all the numbers n | n % m == b)
    Iterative search scales linearly for big values of a, b, and m.
    from https://www.johndcook.com/blog/2008/12/10/solving-linear-congruences/
    This recursive solution works by solving the subproblem my === -b mod a, which is easier because a < m
        if y solves this problem, then x = (my + b)/a solves the original problem.
        my === 0 mod m
        my + b === b mod m
        a(my + b)/a === b mod m
        ax = b mod m where x === (my + b)/a
    a and m must be relatively prime for this method (e.g. gcd(a, m)==1)
        If b is not divisible by gcd(a, m), there are no solutions.
        If b is divisible by gcd(a, m), there are gcd(a, m) solutions.
        Thus if gcd(a, m)==1 there is exactly 1 solution.
    :param a: The coeficient of x. MUST be relatively prime with m. (e.g. gcd(a, m)==1)
    :param b: The resulted value after mod
    :param m: The mod. MUST be relatively prime with a.
    :return: x that solves ax % m == b
    """
    a %= m
    b %= m
    if m == 1:
        return 1
    y = congruence(m, -b, a)
    x = ((m * y + b) // a) % m
    return x


class Direction:
    UP    = NORTH = 0
    LEFT  = WEST  = 2
    DOWN  = SOUTH = 4
    RIGHT = EAST  = 6
    UP_LEFT    = NORTHWEST = 1
    DOWN_LEFT  = SOUTHWEST = 3
    DOWN_RIGHT = SOUTHEAST = 5
    UP_RIGHT   = NORTHEAST = 7


def turn_left_90(direction):
    return (direction + 2) % 8


def turn_right_90(direction):
    return (direction - 2 + 8) % 8


def turn_left_45(direction):
    return (direction + 1) % 8


def turn_right_45(direction):
    return (direction - 1 + 8) % 8


class Turtle:
    def __init__(self):
        self.pos = Vector(0, 0)
        self.direction = Direction.NORTH

    def turn_left_90(self):
        self.direction = turn_left_90(self.direction)

    def turn_right_90(self):
        self.direction = turn_right_90(self.direction)

    def turn_left_45(self):
        self.direction = turn_left_45(self.direction)

    def turn_right_45(self):
        self.direction = turn_right_45(self.direction)

    @staticmethod
    def direction_as_vector(direction):
        if direction == Direction.NORTH:
            return Vector(0, -1)
        elif direction == Direction.EAST:
            return Vector(1, 0)
        elif direction == Direction.SOUTH:
            return Vector(0, 1)
        elif direction == Direction.WEST:
            return Vector(-1, 0)
        elif direction == Direction.NORTHWEST:
            return Vector(-1, 1)
        elif direction == Direction.SOUTHWEST:
            return Vector(-1, -1)
        elif direction == Direction.SOUTHEAST:
            return Vector(1, -1)
        elif direction == Direction.NORTHEAST:
            return Vector(1, 1)
        else:
            assert False

    def forward(self, amount):
        self.pos += self.direction_as_vector(self.direction) * amount

    def backward(self, amount):
        self.pos -= self.direction_as_vector(self.direction) * amount

    def to_front(self, amount):
        return self.pos + self.direction_as_vector(self.direction) * amount

    def to_back(self, amount):
        return self.pos + self.direction_as_vector(self.direction) * amount

    def to_left(self, amount):
        return self.pos + self.direction_as_vector(turn_left_90(self.direction)) * amount

    def to_right(self, amount):
        return self.pos + self.direction_as_vector(turn_right_90(self.direction)) * amount


class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __repr__(self):
        rep = '('
        first = True
        for i in range(4):
            if i >= len(self.coords):
                break

            if first:
                first = False
            else:
                rep += ', '
            rep += str(self.coords[i])
        if len(self.coords) > 4:
            rep += ', ...'
        rep += ')'
        return rep

    def __iter__(self):
        return self.coords.__iter__()

    def __hash__(self):
        return hash(tuple(self.coords))

    @property
    def x(self):
        return self.coords[0]

    @x.setter
    def x(self, val):
        self.coords[0] = val

    @property
    def y(self):
        return self.coords[1]

    @y.setter
    def y(self, val):
        self.coords[1] = val

    @property
    def z(self):
        return self.coords[2]

    @z.setter
    def z(self, val):
        self.coords[2] = val

    def __eq__(self, other):
        assert len(self.coords) == len(other.coords)
        return tuple(self.coords) == tuple(other.coords)

    def __ne__(self, other):
        assert len(self.coords) == len(other.coords)
        return tuple(self.coords) != tuple(other.coords)

    def __lt__(self, other):
        assert len(self.coords) == len(other.coords)
        return tuple(self.coords) < tuple(other.coords)

    def __gt__(self, other):
        assert len(self.coords) == len(other.coords)
        return tuple(self.coords) > tuple(other.coords)

    def __le__(self, other):
        assert len(self.coords) == len(other.coords)
        return tuple(self.coords) <= tuple(other.coords)

    def __ge__(self, other):
        assert len(self.coords) == len(other.coords)
        return tuple(self.coords) >= tuple(other.coords)

    def __add__(self, other):
        assert len(self.coords) == len(other.coords)
        return Vector(*[c1 + c2 for c1, c2 in zip(self.coords, other.coords)])

    def __sub__(self, other):
        assert len(self.coords) == len(other.coords)
        return Vector(*[c1 - c2 for c1, c2 in zip(self.coords, other.coords)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            assert len(self.coords) == len(other.coords)
            return Vector(*[c1 * c2 for c1, c2 in zip(self.coords, other.coords)])
        return Vector(*[c * other for c in self.coords])

    def __truediv__(self, other):
        if isinstance(other, Vector):
            assert len(self.coords) == len(other.coords)
            return Vector(*[c1 / c2 for c1, c2 in zip(self.coords, other.coords)])
        return Vector(*[c / other for c in self.coords])

    def __iadd__(self, other):
        assert len(self.coords) == len(other.coords)
        self.coords = [c1 + c2 for c1, c2 in zip(self.coords, other.coords)]
        return self

    def __isub__(self, other):
        assert len(self.coords) == len(other.coords)
        self.coords = [c1 - c2 for c1, c2 in zip(self.coords, other.coords)]
        return self

    def __imul__(self, other):
        if isinstance(other, Vector):
            assert len(self.coords) == len(other.coords)
            self.coords = [c1 * c2 for c1, c2 in zip(self.coords, other.coords)]
        else:
            self.coords = [c * other for c in self.coords]
        return self

    def __itruediv__(self, other):
        if isinstance(other, Vector):
            assert len(self.coords) == len(other.coords)
            self.coords = [c1 / c2 for c1, c2 in zip(self.coords, other.coords)]
        else:
            self.coords = [c / other for c in self.coords]
        return self

    def clone(self):
        return Vector(*[_ for _ in self.coords])

    def length(self):
        return math.sqrt(sum([c ** 2 for c in self.coords]))

    def distance(self, other):
        return (self - other).length()

    def normalize(self):
        length = self.length()
        self.coords = [c / length for c in self.coords]

    def dot(self, other):
        assert len(self.coords) == len(other.coords)
        return sum([c1 * c2 for c1, c2 in zip(self.coords, other.coords)])

    def cross(self, other):
        """I only know how to do this with 3D vectors
        :type other: Vector
        """
        assert len(self.coords) == len(other.coords) == 3
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)

    def midpoint(self, other):
        assert len(self.coords) == len(other.coords)
        return (self + other) / 2

    def left(self):
        ret = Vector(*self.coords)
        ret.coords[0] -= 1
        return ret

    def right(self):
        ret = Vector(*self.coords)
        ret.coords[0] += 1
        return ret

    def up(self):
        ret = Vector(*self.coords)
        ret.coords[1] -= 1
        return ret

    def down(self):
        ret = Vector(*self.coords)
        ret.coords[1] += 1
        return ret


def render_map(tileMap, valueToStrMapping, defaultTile=None, originMark=None):
    """
    :tileMape: A dictionary. Key is of type Vector. Value can be anything (typically a character).
    :valueToStrMapping: If the value type of tileMap is a character, this can be None. Otherwise it is a dictionary where passing in the value type will yield a character to be printed.
    :defaultTile: A character. If provided, this will be printed if a coordinate does not appear in the tileMap (key set).
    :originMark: A character. If given, this character is printed at coordinate (0, 0).
    """
    # find bounds
    xmin = min([vector.x for vector in tileMap.keys()])
    xmax = max([vector.x for vector in tileMap.keys()])
    ymin = min([vector.y for vector in tileMap.keys()])
    ymax = max([vector.y for vector in tileMap.keys()])

    out = ''

    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            vector = Vector(x, y)
            if vector in tileMap:
                tile = tileMap[vector]
            elif defaultTile is not None:
                tile = defaultTile
            else:
                assert False

            if originMark is not None and vector.x == 0 and vector.y == 0:
                out += originMark
            else:
                if isinstance(tile, str):
                    out += tile
                else:
                    out += valueToStrMapping[tile]
        out += '\n'
    print(out, end='')
