import math
import itertools


class Base:
    pass


class Pair(Base):
    def __init__(self, left, right):
        assert isinstance(left, Base)
        assert isinstance(right, Base)
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        self.parent = None

    def __str__(self):
        #return repr(self)
        return f"[{self.left},{self.right}]"

    def __repr__(self):
        return f"Pair<{hex(id(self))}>({repr(self.left)},{repr(self.right)})"

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()


class Num(Base):
    def __init__(self, val):
        assert isinstance(val, int)
        self.val = val
        self.parent = None

    def __str__(self):
        #return repr(self)
        return f"{self.val}"

    def __repr__(self):
        return f"Num<{hex(id(self))}>({repr(self.val)})"

    def magnitude(self):
        return self.val


def build(line):
    assert line[0] == '['
    if line[1] == '[':
        p1, line = build(line[1:])
    else:
        p1 = Num(int(line[1]))
        line = line[2:]

    assert line[0] == ','

    if line[1] == '[':
        p2, line = build(line[1:])
    else:
        p2 = Num(int(line[1]))
        line = line[2:]

    assert line[0] == ']'
    ret = Pair(p1, p2)
    p1.parent = ret
    p2.parent = ret
    return ret, line[1:]


def get_input_a():
    with open('day18.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    ps = []
    for line in lines:
        p, l = build(line)
        assert l == ''
        #assert str(p) == line
        ps.append(p)
    return ps


def get_input_b():
    return get_input_a()


def prev_num(p):
    if p.parent is None:
        return None
    if p is p.parent.right:
        cur = p.parent.left
        while isinstance(cur, Pair):
            cur = cur.right
        return cur

    cur = p.parent.parent
    prev = p.parent
    while cur is not None and prev is cur.left:
        prev = cur
        cur = cur.parent
    if cur is None:
        return None
    cur = cur.left
    while isinstance(cur, Pair):
        cur = cur.right
    return cur


def next_num(p):
    if p.parent is None:
        return None
    if p is p.parent.left:
        cur = p.parent.right
        while isinstance(cur, Pair):
            cur = cur.left
        return cur

    cur = p.parent.parent
    prev = p.parent
    while cur is not None and prev is cur.right:
        prev = cur
        cur = cur.parent
    if cur is None:
        return None
    cur = cur.right
    while isinstance(cur, Pair):
        cur = cur.left
    return cur


def add(r1, r2):
    p = Pair(r1, r2)
    r1.parent = p
    r2.parent = p
    reduc(p)
    return p


def reduc(root):
    while True:
        ex = check_explode(root, 0)
        if ex:
            explode(ex)
            continue
        spl = check_split(root)
        if spl:
            split(spl)
            continue
        break


def check_explode(root, depth):
    if isinstance(root, Num):
        return None
    assert isinstance(root, Pair)
    if depth == 4:
        assert isinstance(root.left, Num)
        assert isinstance(root.right, Num)
        return root
    ret = check_explode(root.left, depth + 1)
    if ret:
        return ret
    return check_explode(root.right, depth + 1)


def explode(root):
    assert isinstance(root, Pair)
    assert isinstance(root.left, Num)
    assert isinstance(root.right, Num)
    assert root.parent is not None
    left = prev_num(root.left)
    if left:
        left.val += root.left.val
    right = next_num(root.right)
    if right:
        right.val += root.right.val

    n = Num(0)
    n.parent = root.parent
    if root is root.parent.left:
        root.parent.left = n
    else:
        root.parent.right = n


def check_split(root):
    if isinstance(root, Num):
        if root.val >= 10:
            return root
        return None
    ret = check_split(root.left)
    if ret:
        return ret
    return check_split(root.right)


def split(root):
    assert isinstance(root, Num)
    assert root.parent is not None
    left = Num(root.val // 2)
    right = Num(math.ceil(root.val / 2))
    p = Pair(left, right)
    left.parent = p
    right.parent = p
    p.parent = root.parent
    if root is root.parent.left:
        root.parent.left = p
    else:
        root.parent.right = p


def day18a():
    print("    Part A")
    ps = get_input_a()
    agg = ps[0]
    for i in range(1, len(ps)):
        p = ps[i]
        agg = add(agg, p)
    print(agg)
    print(agg.magnitude())



def day18b():
    print("\n    Part B")
    ps = get_input_b()
    asdf = len(ps)
    ss = []
    for i, j in itertools.combinations(range(asdf), 2):
        ps = get_input_b()
        ss.append(add(ps[i], ps[j]).magnitude())
    for i, j in itertools.combinations(range(asdf), 2):
        ps = get_input_b()
        ss.append(add(ps[j], ps[i]).magnitude())

    print(max(ss))
    # 4517 is too low



if __name__ == '__main__':
    day18a()
    day18b()
