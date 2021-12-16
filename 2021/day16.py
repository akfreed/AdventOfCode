from functools import reduce


def get_input_a():
    with open('day16.txt', 'r') as file:
        return file.readline().strip()


def get_input_b():
    return get_input_a()


def split_header(packet):
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)
    rest = packet[6:]
    return version, type_id, rest


def split_literal(packet):
    agg = ''
    while True:
        agg += packet[1:5]
        if int(packet[0], 2) == 0:
            return int(agg, 2), packet[5:]
        packet = packet[5:]


def split_operator(packet):
    length_type_id = int(packet[0], 2)
    if length_type_id == 0:
        length = int(packet[1:16], 2)
        return length_type_id, length, packet[16:]
    else:
        num_packets = int(packet[1:12], 2)
        return length_type_id, num_packets, packet[12:]


ver_count = 0


class Literal:
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val


class Sum:
    def __init__(self, *args):
        self.children = list(args)

    def eval(self):
        agg = 0
        for c in self.children:
            agg += c.eval()
        return agg


class Product:
    def __init__(self, *args):
        self.children = list(args)

    def eval(self):
        agg = 1
        for c in self.children:
            agg *= c.eval()
        return agg


class Minimum:
    def __init__(self, *args):
        self.children = list(args)

    def eval(self):
        return min([ast.eval() for ast in self.children])


class Maximum:
    def __init__(self, *args):
        self.children = list(args)

    def eval(self):
        return max([ast.eval() for ast in self.children])


class GreaterThan:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return 1 if self.left.eval() > self.right.eval() else 0


class LessThan:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return 1 if self.left.eval() < self.right.eval() else 0


class EqualTo:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return 1 if self.left.eval() == self.right.eval() else 0


def x_ast(type_id, asts):
    if type_id == 0:
        return Sum(*asts)
    if type_id == 1:
        return Product(*asts)
    if type_id == 2:
        return Minimum(*asts)
    if type_id == 3:
        return Maximum(*asts)
    if type_id == 5:
        return GreaterThan(asts[0], asts[1])
    if type_id == 6:
        return LessThan(asts[0], asts[1])
    if type_id == 7:
        return EqualTo(asts[0], asts[1])
    assert False


def parse_packet(packet):
    if packet == '':
        assert False
        #return '', None
    global ver_count
    version, type_id, packet = split_header(packet)
    #print(f"Packet v{version}.")
    ver_count += version
    if type_id == 4:  # literal packet
        literal, packet = split_literal(packet)
        #print(f"    Literal: {literal}")
        return packet, Literal(literal)
    else:
        length_type_id, val, packet = split_operator(packet)
        #print(f"    Operator({type_id}, {length_type_id}): {val}")
        asts = []
        if length_type_id == 0:
            l = len(packet) - val
            while True:
                packet, ast = parse_packet(packet[:])
                asts.append(ast)
                assert len(packet) >= l
                if len(packet) <= l:
                    ast = x_ast(type_id, asts)
                    return packet, ast
        else:
            for i in range(val):
                packet, ast = parse_packet(packet[:])
                asts.append(ast)
            ast = x_ast(type_id, asts)
            return packet, ast


def day16a():
    print("    Part A")
    h = get_input_a()
    b = bin(int(h, 16))[2:]
    global ver_count
    ver_count = 0
    #print(len(h))
    #print(len(b))
    while len(b) % 4 != 0:
        b = '0' + b
    for l in h:
        if l == '0':
            b = '0000' + b
        else:
            break

    #print(b)
    parse_packet(b)
    print(ver_count)



def day16b():
    print("\n    Part B")
    h = get_input_a()
    b = bin(int(h, 16))[2:]
    global ver_count
    ver_count = 0
    #print(len(h))
    #print(len(b))
    while len(b) % 4 != 0:
        b = '0' + b
    for l in h:
        if l == '0':
            b = '0000' + b
        else:
            break

    #print(b)
    _, ast = parse_packet(b)
    #print(ver_count)
    print(ast.eval())



if __name__ == '__main__':
    day16a()
    day16b()
